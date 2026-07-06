#!/usr/bin/env python3
"""
ETH Strategy Verification Script

1. Loads ETH data (Daily & Hourly)
2. Trains ETH-specific HMM via walk-forward retraining
3. Generates TR3 features on the hourly data
4. Runs causal walk-forward backtest (no lookahead)
"""

import sys
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.hmm.eth_model import (
    ETHRegimeDetector,
    lengths_by_year,
    fit_hmm,
    fit_hmm_warm_start,
    HMM_FEATURES,
    relabel_states_by_return,
    compute_daily_features,
)
from src.features.hourly_features import compute_hourly_features
from scripts.run_holdout_ect import apply_ect, metrics_from_trades, TR3 as TR3_CONFIG

# Optimized parameters for ETH (found via optimize_tr3_params.py on 2020-2021)
TR3_ETH = TR3_CONFIG.copy()
TR3_ETH.update({
    "adx_min": 18,
    "r2_min": 0.08,
    "fth_disable_after_atr": 0.4,
    "clv_fail_max": 0.4,
    "be_activate_atr": 1.0,
})


def load_data(daily_path: Path, hourly_path: Path):
    """Load and prepare daily and hourly DataFrames."""
    print(f"Loading Daily: {daily_path}")
    d = pd.read_csv(daily_path)
    if "time" in d.columns and "Date" not in d.columns:
        d = d.rename(columns={"time": "Date"})
    d["Date"] = pd.to_datetime(d["Date"], utc=True)
    d = d.set_index("Date").sort_index()

    print(f"Loading Hourly: {hourly_path}")
    h = pd.read_csv(hourly_path)
    if "time" in h.columns and "Date" not in h.columns:
        h = h.rename(columns={"time": "Date"})
    h["Date"] = pd.to_datetime(h["Date"], utc=True)
    h = h.set_index("Date").sort_index()

    return d, h


def run_strategy(df: pd.DataFrame, states: pd.Series, params: dict):
    """
    Run TR3 strategy on an hourly DataFrame with pre-computed features.

    ``states`` is a daily-indexed Series where state[T] was derived from data
    up to T-1 (already causal).  It is mapped onto the hourly index and used
    directly as the regime filter.
    """
    df = df.copy()

    # Map daily states onto hourly bars — one mapping, no duplicate
    day_idx = df.index.normalize()
    df["regime"] = day_idx.map(states).fillna(0).astype(int)

    R = params

    # Feature aliases
    if "EMA200" not in df.columns and "MOM_ema200" in df.columns:
        df["EMA200"] = df["MOM_ema200"]
    if "ATR14" not in df.columns and "MR_atr14" in df.columns:
        df["ATR14"] = df["MR_atr14"]

    # CLV: (C - L) / (H - L), range [0, 1].  The clv_min threshold (0.55) is
    # calibrated for this formula.  Do NOT use (2C - H - L) / (H - L) here —
    # that gives range [-1, 1] and makes the threshold ~3x too strict.
    if "CLV" not in df.columns:
        rng = (df["High"] - df["Low"]).replace(0, np.nan)
        df["CLV"] = ((df["Close"] - df["Low"]) / rng).fillna(0.5)

    if "ClosePosInRange" not in df.columns:
        rng = (df["High"] - df["Low"]).replace(0, np.nan)
        df["ClosePosInRange"] = ((df["Close"] - df["Low"]) / rng) - 0.5

    thrust = (df["Close"] - df["Close"].shift(1)) >= (R["thrust_atr_mult"] * df["ATR14"])
    breakout = df["Close"] > df["MOM_donchian20_up"]

    ent_reg = df["regime"] == R["allowed_regime"]
    ent_trend = (df["MOM_ema50"] > df["EMA200"]) & (df["Close"] > df["MOM_ema50"])
    ent_mom = breakout | thrust
    ent_clv = df["CLV"] >= R["clv_min"]
    ent_adx = df["ADX14"] >= R["adx_min"]
    ent_r2 = df["R2_ema50"] >= R["r2_min"]

    cond = ent_reg & ent_trend & ent_mom & ent_clv & ent_adx & ent_r2
    entry_sig = cond.shift(1).fillna(False)

    # Pre-compute arrays for the simulation loop
    closes = df["Close"].values
    opens = df["Open"].values
    highs = df["High"].values
    dates = df.index
    atrs = df["ATR14"].values
    ema50s = df["MOM_ema50"].values
    clvs = df["CLV"].values
    sigs = entry_sig.values
    regimes = df["regime"].values

    in_pos = False
    trades = []
    pos = np.zeros(len(df), dtype=float)

    if "ret_oo" not in df.columns:
        df["ret_oo"] = df["Open"].pct_change().fillna(0.0)
    ret_oo = df["ret_oo"].values

    entry_price = 0.0
    entry_idx = 0
    high_since = 0.0
    be_armed = False

    for i in range(1, len(df)):
        if not in_pos:
            if sigs[i]:
                in_pos = True
                entry_idx = i
                entry_price = opens[i]
                high_since = highs[i - 1]
                be_armed = False
        else:
            j = i - 1
            c_prev = closes[j]
            h_prev = highs[j]
            atr_val = atrs[j]
            ema_val = ema50s[j]
            clv_val = clvs[j]

            high_since = max(high_since, h_prev)

            if np.isnan(atr_val) or atr_val == 0:
                pos[i] = 1.0
                continue

            adv_atr = (high_since - entry_price) / atr_val
            exit_now = False
            reason = ""

            # 1. Fail-to-Hold
            use_fth = adv_atr < R["fth_disable_after_atr"]
            if use_fth:
                if clv_val < R["clv_fail_max"]:
                    exit_now = True
                    reason = "fth_clv"
                elif c_prev < (high_since - R["fail_level_atr"] * atr_val):
                    exit_now = True
                    reason = "fth_level"

            # 2. Breakeven
            if not exit_now:
                if adv_atr >= R["be_activate_atr"] and adv_atr < R["be_disable_after_atr"]:
                    be_armed = True
                if adv_atr >= R["be_disable_after_atr"]:
                    be_armed = False

                if be_armed:
                    # be_cushion_atr is negative (e.g. -0.02) — subtract it to
                    # place the stop *above* entry, matching tr3_engine.py sign
                    # convention: be_level = entry - cushion * atr
                    be_level = entry_price - R["be_cushion_atr"] * atr_val
                    if c_prev <= be_level:
                        exit_now = True
                        reason = "breakeven"

            # 3. EMA break
            if not exit_now and c_prev < ema_val:
                if adv_atr >= R["ema_break_relax_after_atr"]:
                    if c_prev < (ema_val - R["ema_break_cushion_atr"] * atr_val):
                        exit_now = True
                        reason = "ema50_relaxed"
                else:
                    exit_now = True
                    reason = "ema50_break"

            # 4. Trailing stop (ratcheting)
            if not exit_now:
                if adv_atr > 2.0:
                    mult = R["trail_mult_2"]
                elif adv_atr > 1.0:
                    mult = R["trail_mult_1"]
                else:
                    mult = R["trail_mult_base"]
                stop = high_since - mult * atr_val
                if c_prev < stop:
                    exit_now = True
                    reason = "trail_atr"

            # 5. Time / no-progress stops
            if not exit_now:
                hold_hrs = (dates[i] - dates[entry_idx]).total_seconds() / 3600
                if hold_hrs > R["time_stop_hours"]:
                    exit_now = True
                    reason = "time_stop"
                elif hold_hrs > R["no_progress_hours"] and adv_atr < R["no_progress_atr"]:
                    exit_now = True
                    reason = "no_progress"

            if exit_now:
                exit_price = opens[i]
                ret = (exit_price / entry_price) - 1.0
                trades.append({
                    "entry_time": dates[entry_idx],
                    "exit_time": dates[i],
                    "net_ret": ret,
                    "holding_hours": (dates[i] - dates[entry_idx]).total_seconds() / 3600,
                    "exit_reason": reason,
                    "regime": regimes[entry_idx],
                })
                in_pos = False

        pos[i] = 1.0 if in_pos else 0.0

    # pos[i]=1 means entered at Open[i]; return accrues at Open[i+1]
    hourly_rets = pd.Series(pos, index=df.index).shift(1).fillna(0.0) * df["ret_oo"]
    return pd.DataFrame(trades), hourly_rets


def run_eth_walkforward(
    daily_df: pd.DataFrame,
    hourly_df: pd.DataFrame,
    train_end: str = "2020-12-31",
    rebalance_days: int = 30,
    window_days: int = 730,
    viterbi_window: int = 60,
) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    """
    Causal walk-forward backtest for ETH.

    Returns
    -------
    trades : pd.DataFrame
    daily_rets : pd.Series  (daily returns from test period onwards)
    active_mask : pd.Series[bool]  (True on days with an open position)
    """
    df = compute_daily_features(daily_df)
    df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()

    test_start_dt = pd.Timestamp(train_end, tz="UTC")
    df_future = df.loc[df.index > test_start_dt]

    if df_future.empty:
        print("No data after train_end — nothing to backtest.")
        empty = pd.Series(dtype=float)
        return pd.DataFrame(), empty, pd.Series(dtype=bool)

    start_date = df_future.index[0]
    end_date = df_future.index[-1]
    current_date = start_date

    states_online_list = []
    dates_online_list = []
    prev_model = None

    print(f"Starting ETH walk-forward from {current_date.date()} …")

    while current_date <= end_date:
        win_start = current_date - pd.Timedelta(days=window_days)
        mask_tr = (df.index >= win_start) & (df.index < current_date)
        df_tr = df.loc[mask_tr]

        if len(df_tr) < 100:
            print(f"  Skipping {current_date.date()}: insufficient history ({len(df_tr)} days).")
            current_date += pd.Timedelta(days=rebalance_days)
            continue

        X_tr = df_tr[HMM_FEATURES].values
        scaler = StandardScaler().fit(X_tr)
        Xs_tr = scaler.transform(X_tr)
        lens = lengths_by_year(df_tr.index)

        if prev_model is None:
            model = fit_hmm(Xs_tr, lens, k=3, seed=42)
        else:
            model = fit_hmm_warm_start(Xs_tr, lens, prev_model=prev_model, k=3, seed=42)

        # Align state labels: 1 = Bullish (highest avg return)
        st_tr = model.predict(Xs_tr)
        df_tr_copy = df_tr.copy()
        df_tr_copy["_temp_state"] = st_tr
        mapping = relabel_states_by_return(df_tr_copy, "_temp_state")

        prev_model = model

        next_rebalance = current_date + pd.Timedelta(days=rebalance_days)
        mask_pred = (df.index >= current_date) & (df.index < next_rebalance)
        df_pred = df.loc[mask_pred]

        if df_pred.empty:
            break

        X_pred = df_pred[HMM_FEATURES].values
        Xs_pred = scaler.transform(X_pred)

        # Sliding Viterbi context from training window
        X_ctx = Xs_tr[-viterbi_window:]
        Xs_comb = np.vstack([X_ctx, Xs_pred])
        ctx_len = len(X_ctx)

        chunk_states = []
        for t in range(len(Xs_pred)):
            # Window ending at idx-1 (day T-1), excluding today — no lookahead
            idx = ctx_len + t
            w_start = max(0, idx - viterbi_window)
            X_w = Xs_comb[w_start:idx]
            if len(X_w) == 0:
                chunk_states.append(0)
            else:
                raw_st = model.predict(X_w)[-1]
                chunk_states.append(mapping.get(raw_st, 0))

        states_online_list.extend(chunk_states)
        dates_online_list.extend(df_pred.index)
        current_date = next_rebalance

    states_series = pd.Series(states_online_list, index=dates_online_list)

    # Map states onto hourly bars; states_series[T] was derived from T-1 data
    # so it is already the correct lagged signal — no further shift needed.
    h_test = hourly_df.loc[hourly_df.index >= test_start_dt].copy()
    day_idx = h_test.index.normalize()
    h_test["D1_State_lag1d"] = day_idx.map(states_series).fillna(0).astype(int)

    # Ensure required feature aliases exist
    if "MOM_ema200" in h_test.columns and "EMA200" not in h_test.columns:
        h_test["EMA200"] = h_test["MOM_ema200"]
    if "MR_atr14" in h_test.columns and "ATR14" not in h_test.columns:
        h_test["ATR14"] = h_test["MR_atr14"]

    # Compute any still-missing TR3 features from raw OHLCV
    if "ATR14" not in h_test.columns or "EMA200" not in h_test.columns:
        print("Computing missing TR3 features from raw OHLCV …")
        h_test = h_test.sort_index()
        h_test["EMA200"] = h_test["Close"].ewm(span=200, adjust=False).mean()

        hi = h_test["High"]
        lo = h_test["Low"]
        c_prev = h_test["Close"].shift(1)
        tr = pd.concat([hi - lo, (hi - c_prev).abs(), (lo - c_prev).abs()], axis=1).max(axis=1)
        h_test["ATR14"] = tr.ewm(alpha=1 / 14, adjust=False).mean()

        # Donchian shifted so current bar's high is excluded (avoids always-False breakout)
        h_test["MOM_donchian20_up"] = h_test["High"].rolling(window=20).max().shift(1)
        h_test["MOM_ema50"] = h_test["Close"].ewm(span=50, adjust=False).mean()

        up = h_test["High"] - h_test["High"].shift(1)
        dn = h_test["Low"].shift(1) - h_test["Low"]
        p_dm = np.where((up > dn) & (up > 0), up, 0.0)
        m_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
        p_di = 100 * pd.Series(p_dm, index=h_test.index).ewm(alpha=1 / 14, adjust=False).mean() / h_test["ATR14"]
        m_di = 100 * pd.Series(m_dm, index=h_test.index).ewm(alpha=1 / 14, adjust=False).mean() / h_test["ATR14"]
        dx = 100 * (p_di - m_di).abs() / (p_di + m_di).replace(0, np.nan)
        h_test["ADX14"] = dx.ewm(alpha=1 / 14, adjust=False).mean()

        idx_seq = pd.Series(np.arange(len(h_test)), index=h_test.index)
        h_test["R2_ema50"] = h_test["Close"].rolling(50).corr(idx_seq).pow(2)

    trades, hourly_rets = run_strategy(h_test, states_series, TR3_ETH)

    daily_rets = (1 + hourly_rets).resample("D").prod() - 1.0
    daily_rets = daily_rets.fillna(0.0)

    active_mask = pd.Series(False, index=daily_rets.index)
    if not trades.empty:
        entry_times = pd.to_datetime(trades["entry_time"], utc=True)
        exit_times = pd.to_datetime(trades["exit_time"], utc=True)
        for en, ex in zip(entry_times, exit_times):
            active_mask.loc[en.normalize():ex.normalize()] = True

    return trades, daily_rets, active_mask


def main():
    parser = argparse.ArgumentParser(description="ETH HMM-TR3 walk-forward backtest")
    parser.add_argument("--daily", required=True, help="Path to daily ETH OHLCV CSV")
    parser.add_argument("--hourly", required=True, help="Path to hourly ETH OHLCV CSV")
    parser.add_argument("--out-dir", required=True, help="Output directory")
    parser.add_argument("--train-end", default="2020-12-31", help="Last date used for initial training")
    args = parser.parse_args()

    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    df_d, df_h = load_data(Path(args.daily), Path(args.hourly))

    print("Computing hourly features …")
    df_h = compute_hourly_features(df_h)

    print("Running ETH walk-forward …")
    trades, daily_rets, _active = run_eth_walkforward(
        df_d, df_h, train_end=args.train_end
    )

    if trades.empty:
        print("No trades generated.")
        return

    print("Applying ECT risk management …")
    trades = apply_ect(trades, window=30, risk_high=1.0, risk_low=0.5)
    trades.to_csv(out_path / "trades_eth.csv", index=False)

    m = metrics_from_trades(trades, "net_ret_scaled")
    print("\n" + "=" * 40)
    print("ETH STRATEGY RESULTS")
    print("=" * 40)
    for k, v in m.items():
        print(f"{k}: {v}")
    print("=" * 40)

    with open(out_path / "summary.txt", "w") as f:
        for k, v in m.items():
            f.write(f"{k}: {v}\n")
    print(f"Saved results to {out_path}")


if __name__ == "__main__":
    main()
