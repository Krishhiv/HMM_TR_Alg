#!/usr/bin/env python3
"""
Holdout test with Equity Curve Trading (ECT) risk manager.
Uses the same HMM + TR^3 logic as run_holdout.py and TR_MODEL_2.py,
but scales trade returns based on a 30-trade equity SMA filter.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from math import sqrt

import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler


# -----------------------------
# HMM config (same as btc_1d_hmm.py)
# -----------------------------
TRAIN_END = "2019-12-31"
VAL_END = "2021-12-31"
K_CANDIDATES = (3,)
RESTARTS = 5
MAX_ITER = 500
RANDOM_SEED = 42


# -----------------------------
# TR^3 config (same as TR_MODEL_2.py)
# -----------------------------
TR3 = {
    "regime_col": "D1_State_lag1d",
    "allowed_regime": 1,
    "donchian_period": 20,
    "adx_min": 14,
    "r2_min": 0.10,
    "clv_min": 0.55,
    "thrust_atr_mult": 0.75,
    "ema_fast": 50,
    "ema_slow": 200,
    "clv_fail_max": 0.35,
    "fail_level_atr": 0.25,
    "trail_atr_n": 14,
    "trail_atr_mult": 2.5,
    "no_progress_hours": 12,
    "no_progress_atr": 0.50,
    "time_stop_hours": 24 * 7,
    "fth_disable_after_atr": 0.5,
    "be_activate_atr": 0.75,
    "be_cushion_atr": -0.02,
    "be_disable_after_atr": 1.0,
    "be_one_bar_delay": True,
    "trail_mult_base": 2.5,
    "trail_mult_1": 3.5,
    "trail_mult_2": 4.5,
    "ema_break_relax_after_atr": 1.0,
    "ema_break_cushion_atr": 0.25,
}


# -----------------------------
# HMM features (same as btc_1d_hmm.py)
# -----------------------------
FEATURES = [
    "Log_Returns",
    "GKVol_20",
    "VolZ_20",
    "EMA_20_slope",
    "BodyPct",
    "ClosePosInRange",
    "CloseOverEMA20",
]


def build_compact_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["BodyPct"] = (df["Close"] - df["Open"]) / (df["Open"].replace(0, np.nan))
    rng = (df["High"] - df["Low"]).replace(0, np.nan)
    df["ClosePosInRange"] = ((df["Close"] - df["Low"]) / rng) - 0.5
    df["CloseOverEMA20"] = (df["Close"] / df["EMA_20"]) - 1.0
    df = df.dropna(subset=FEATURES + ["Close"]).copy()
    return df


def lengths_by_year(idx_utc: pd.Index) -> list[int]:
    idx_naive = idx_utc.tz_convert(None) if idx_utc.tz is not None else idx_utc
    g = pd.Series(1, index=idx_naive).groupby(idx_naive.to_period("Y")).sum()
    return g.astype(int).tolist()


def priors(k: int, self_bias: float = 5.0, concentration: float = 50.0):
    trans = np.full((k, k), 1.0, dtype=float)
    np.fill_diagonal(trans, self_bias)
    trans *= (concentration / k)
    start = np.full(k, concentration / k, dtype=float)
    return start, trans


def fit_hmm(X: np.ndarray, lengths: list[int], k: int, seed: int) -> GaussianHMM:
    sp, tp = priors(k, self_bias=1.8)
    model = GaussianHMM(
        n_components=k,
        covariance_type="diag",
        n_iter=MAX_ITER,
        tol=1e-3,
        random_state=seed,
        min_covar=1e-5,
        startprob_prior=sp,
        transmat_prior=tp,
    )
    model.fit(X, lengths=lengths)
    return model


def pick_best_model(X: np.ndarray, lengths: list[int], k: int) -> GaussianHMM:
    best, best_ll = None, -np.inf
    seeds = [RANDOM_SEED + i * 7 for i in range(RESTARTS)]
    for s in seeds:
        m = fit_hmm(X, lengths, k, seed=s)
        ll = m.score(X, lengths=lengths)
        if ll > best_ll:
            best, best_ll = m, ll
    return best


def decode(model: GaussianHMM, X: np.ndarray):
    states = model.predict(X)
    _, gamma = model.score_samples(X)
    return states, gamma


def enforce_min_dwell_gamma(path: np.ndarray, gamma: np.ndarray, min_run: int = 3) -> np.ndarray:
    p = np.asarray(path, dtype=int).copy()
    n = len(p)
    changed = True
    while changed:
        changed = False
        i = 0
        while i < n:
            j = i + 1
            while j < n and p[j] == p[i]:
                j += 1
            run_len = j - i
            if run_len < min_run:
                left = p[i - 1] if i > 0 else None
                right = p[j] if j < n else None
                cand = []
                if left is not None:
                    cand.append((left, float(gamma[i:j, left].sum())))
                if right is not None:
                    cand.append((right, float(gamma[i:j, right].sum())))
                if cand:
                    fill = max(cand, key=lambda t: t[1])[0]
                    p[i:j] = fill
                    changed = True
            i = j
    return p


# -----------------------------
# TR^3 helpers (same as TR_MODEL_2.py)
# -----------------------------
def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def calc_atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    hl = df["High"] - df["Low"]
    hc = (df["High"] - df["Close"].shift(1)).abs()
    lc = (df["Low"] - df["Close"].shift(1)).abs()
    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=n).mean()


def load_data_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.sort_values("Date").reset_index(drop=True)

    required = [
        "Open", "High", "Low", "Close",
        "MOM_donchian20_up", "MOM_ema50",
        "ADX14", "R2_ema50", "MR_rsi14",
        TR3["regime_col"],
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in hourly data: {missing}")

    if "EMA200" not in df.columns:
        df["EMA200"] = ema(df["Close"], TR3["ema_slow"])
    if "ATR14" not in df.columns:
        df["ATR14"] = calc_atr(df, TR3["trail_atr_n"])

    rng = (df["High"] - df["Low"]).replace(0, np.nan)
    df["CLV"] = ((df["Close"] - df["Low"]) / rng).fillna(0.5)

    df["ret_oo_raw"] = df["Open"].pct_change()
    bad_price = (
        (df["Open"] <= 0) | (df["High"] <= 0) | (df["Low"] <= 0) | (df["Close"] <= 0) |
        (df["High"] < df["Low"])
    )
    spike = df["ret_oo_raw"].abs() > 0.40
    df["valid_bar"] = (~bad_price) & (~spike)
    df["ret_oo"] = 0.0
    ok = df["valid_bar"] & (~df["ret_oo_raw"].isna())
    df.loc[ok, "ret_oo"] = df.loc[ok, "ret_oo_raw"]
    df["ret_oo"] = df["ret_oo"].fillna(0.0)

    df[TR3["regime_col"]] = df[TR3["regime_col"]].ffill().fillna(1).astype(int)
    return df


def simulate_tr3(df: pd.DataFrame):
    R = TR3
    regcol = R["regime_col"]

    thrust = (df["Close"] - df["Close"].shift(1)) >= (R["thrust_atr_mult"] * df["ATR14"])
    breakout = df["Close"] > df["MOM_donchian20_up"]

    cond_now = (
        df["valid_bar"] &
        (df[regcol] == R["allowed_regime"]) &
        (df["MOM_ema50"] > df["EMA200"]) &
        (df["Close"] > df["MOM_ema50"]) &
        ((breakout) | (thrust)) &
        (df["CLV"] >= R["clv_min"]) &
        (df["ADX14"] >= R["adx_min"]) &
        (df["R2_ema50"] >= R["r2_min"])
    )
    entry_sig = cond_now.shift(1, fill_value=False).astype(bool)

    in_pos = False
    trades = []
    pos = np.zeros(len(df), dtype=float)
    fee = 0.0

    LEVERAGE = 1.0
    MAX_LOSS_CAP = 0.08

    entry_price = None
    entry_time = None
    entry_bar_high = None
    high_since_entry = None
    entry_reg = None
    be_armed_since = None

    cols = [
        "entry_time", "entry_price", "exit_time", "exit_price",
        "gross_ret", "net_ret", "holding_hours", "regime", "strategy", "exit_reason",
    ]

    for i in range(1, len(df)):
        if not in_pos:
            if entry_sig.iat[i]:
                in_pos = True
                j = i - 1
                entry_time = df["Date"].iat[i]
                entry_price = df["Open"].iat[i]
                entry_bar_high = df["High"].iat[j]
                high_since_entry = df["High"].iat[j]
                entry_reg = int(df[regcol].iat[j])
                be_armed_since = None
        else:
            j = i - 1

            if not bool(df["valid_bar"].iat[j]):
                pos[i] = 1.0
                continue

            hh = df["High"].iat[j]
            if pd.notna(hh):
                high_since_entry = max(high_since_entry, hh)

            close_j = df["Close"].iat[j]
            ema50_j = df["MOM_ema50"].iat[j]
            atr_j = df["ATR14"].iat[j] if pd.notna(df["ATR14"].iat[j]) else None
            clv_j = df["CLV"].iat[j]

            advance_atr = ((high_since_entry - entry_price) / atr_j) if (atr_j is not None and atr_j > 0) else 0.0
            exit_now, reason = False, "rule"

            use_fth = not (advance_atr >= R.get("fth_disable_after_atr", np.inf))

            can_arm_be = (atr_j is not None) and (advance_atr >= R.get("be_activate_atr", np.inf)) \
                         and (advance_atr < R.get("be_disable_after_atr", np.inf))
            if (be_armed_since is None) and can_arm_be:
                be_armed_since = df["Date"].iat[j]

            if advance_atr >= R.get("be_disable_after_atr", np.inf):
                be_armed_since = None

            if be_armed_since is not None:
                if R.get("be_one_bar_delay", True):
                    be_active = (df["Date"].iat[j] - be_armed_since) >= pd.Timedelta(hours=1)
                else:
                    be_active = True
            else:
                be_active = False

            be_level = None
            if be_active and (atr_j is not None):
                be_level = entry_price - R.get("be_cushion_atr", 0.0) * atr_j

            if atr_j is not None:
                if advance_atr >= 2.0:
                    trail_mult = R.get("trail_mult_2", R.get("trail_atr_mult", 2.5))
                elif advance_atr >= 1.0:
                    trail_mult = R.get("trail_mult_1", R.get("trail_atr_mult", 2.5))
                else:
                    trail_mult = R.get("trail_mult_base", R.get("trail_atr_mult", 2.5))
                trail = high_since_entry - trail_mult * atr_j
            else:
                trail = None

            if use_fth:
                if clv_j <= R["clv_fail_max"]:
                    exit_now, reason = True, "fth_clv"
                elif (atr_j is not None) and (close_j < (entry_bar_high - R["fail_level_atr"] * atr_j)):
                    exit_now, reason = True, "fth_level"

            if (not exit_now) and (be_level is not None) and (close_j < be_level):
                exit_now, reason = True, "breakeven"

            if (not exit_now) and (trail is not None) and (close_j < trail):
                exit_now, reason = True, "trail_atr"

            if not exit_now:
                if (advance_atr >= R.get("ema_break_relax_after_atr", np.inf)) and (atr_j is not None):
                    if close_j < (ema50_j - R.get("ema_break_cushion_atr", 0.0) * atr_j):
                        exit_now, reason = True, "ema50_relaxed"
                else:
                    if close_j < ema50_j:
                        exit_now, reason = True, "ema50_break"

            if not exit_now and (df["Date"].iat[j] - entry_time) >= pd.Timedelta(hours=R["no_progress_hours"]):
                if (atr_j is None) or ((high_since_entry - entry_price) < (R["no_progress_atr"] * atr_j)):
                    exit_now, reason = True, "no_progress"

            if not exit_now and (df["Date"].iat[j] - entry_time) >= pd.Timedelta(hours=R["time_stop_hours"]):
                exit_now, reason = True, "time_stop"

            if exit_now:
                exit_time = df["Date"].iat[i]
                exit_price = df["Open"].iat[i]
                gross_ret = (exit_price / entry_price) - 1.0
                net_ret = ((exit_price * (1 - fee)) / (entry_price * (1 + fee)) - 1.0) if fee > 0 else gross_ret
                net_ret *= LEVERAGE
                net_ret = max(net_ret, -MAX_LOSS_CAP)

                trades.append({
                    "entry_time": entry_time, "entry_price": entry_price,
                    "exit_time": exit_time, "exit_price": exit_price,
                    "gross_ret": gross_ret, "net_ret": net_ret,
                    "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
                    "regime": entry_reg, "strategy": "TR3", "exit_reason": reason,
                })
                in_pos = False
                entry_price = entry_time = entry_bar_high = high_since_entry = None
                entry_reg = None
                be_armed_since = None

        pos[i] = 1.0 if in_pos else 0.0

    if in_pos:
        i = len(df) - 1
        exit_time = df["Date"].iat[i]
        exit_price = df["Open"].iat[i]
        gross_ret = (exit_price / entry_price) - 1.0
        net_ret = ((exit_price * (1 - fee)) / (entry_price * (1 + fee)) - 1.0) if fee > 0 else gross_ret
        net_ret *= LEVERAGE
        net_ret = max(net_ret, -MAX_LOSS_CAP)
        trades.append({
            "entry_time": entry_time, "entry_price": entry_price,
            "exit_time": exit_time, "exit_price": exit_price,
            "gross_ret": gross_ret, "net_ret": net_ret,
            "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
            "regime": 1, "strategy": "TR3", "exit_reason": "eod_close",
        })

    trade_log = pd.DataFrame(trades, columns=cols)
    strat_rets = pd.Series(pos, index=df.index) * df["ret_oo"]
    return trade_log, strat_rets


def apply_ect(trade_log: pd.DataFrame, window: int = 40, risk_high: float = 1.0, risk_low: float = 0.5) -> pd.DataFrame:
    """
    Equity Curve Trading (ECT) with a warm-up period and sensitivity buffer.
    - Warm-up: First 'window' trades are at full size to build a baseline.
    - Buffer: Only scales down if equity is 0.5% below the SMA to avoid noise.
    """
    tl = trade_log.copy()
    tl["net_ret_scaled"] = np.nan
    tl["risk_factor"] = np.nan
    tl["equity"] = np.nan
    tl["equity_sma"] = np.nan

    equity = 1.0
    equity_hist = []

    for i in range(len(tl)):
        # Calculate SMA based on historical equity
        if len(equity_hist) < 1:
            sma = 1.0
        else:
            # Use the window of previous equity points
            hist = equity_hist[-window:]
            sma = float(np.mean(hist))

        # --- THE LOGIC TWEAK ---
        if len(equity_hist) < window:
            # 1. Warm-up phase: Build the SMA with full-sized trades
            risk = risk_high
        else:
            # 2. Buffer phase: Only cut risk if equity is 0.5% below the SMA
            # This prevents the bot from scaling down on tiny 'noise' pullbacks
            buffer = 0.995 
            risk = risk_high if equity >= (sma * buffer) else risk_low
        
        # Calculate scaled return for this trade
        ret = tl.loc[i, "net_ret"] * risk

        # Update cumulative equity
        equity = equity * (1.0 + ret)
        equity_hist.append(equity)

        # Log metrics
        tl.at[i, "net_ret_scaled"] = ret
        tl.at[i, "risk_factor"] = risk
        tl.at[i, "equity"] = equity
        tl.at[i, "equity_sma"] = sma

    return tl


def metrics_from_trades(trade_log: pd.DataFrame, ret_col: str) -> dict:
    df = trade_log.copy()
    df["exit_time"] = pd.to_datetime(df["exit_time"], errors="coerce")
    df = df.dropna(subset=["exit_time"])
    df = df.sort_values("exit_time")

    daily_rets = df.set_index("exit_time")[ret_col].resample("D").sum().fillna(0.0)
    cum_equity = (1 + daily_rets).cumprod()
    total_ret = cum_equity.iloc[-1] - 1
    years = (daily_rets.index[-1] - daily_rets.index[0]).days / 365.25
    cagr = (1 + total_ret) ** (1 / years) - 1 if years > 0 else float("nan")

    ann_vol = daily_rets.std() * np.sqrt(365)
    sharpe = (daily_rets.mean() / daily_rets.std()) * np.sqrt(365) if daily_rets.std() > 0 else float("nan")

    downside = daily_rets[daily_rets < 0]
    sortino = (daily_rets.mean() / downside.std()) * np.sqrt(365) if downside.std() > 0 else float("nan")

    rolling_max = cum_equity.cummax()
    drawdown = (cum_equity - rolling_max) / rolling_max
    max_dd = drawdown.min()
    calmar = cagr / abs(max_dd) if max_dd < 0 else float("nan")

    win_rate = (df[ret_col] > 0).mean()
    profits = df.loc[df[ret_col] > 0, ret_col].sum()
    losses = df.loc[df[ret_col] < 0, ret_col].sum()
    profit_factor = (profits / abs(losses)) if losses < 0 else float("nan")

    return {
        "TotalReturn": total_ret,
        "CAGR": cagr,
        "MaxDrawdown": max_dd,
        "Sharpe": sharpe,
        "Sortino": sortino,
        "Calmar": calmar,
        "ProfitFactor": profit_factor,
        "WinRate": win_rate,
        "AnnualVolatility": ann_vol,
        "Trades": len(df),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily-csv", default="MAIN-DATASETS/btc_1d_main.csv")
    parser.add_argument("--hourly-csv", default="TRADING-MODELS/btc_1h_features_TR.csv")
    parser.add_argument("--out-dir", default="walkforward/outputs")
    parser.add_argument("--train-end", default=TRAIN_END)
    parser.add_argument("--val-end", default=VAL_END)
    parser.add_argument("--min-dwell", type=int, default=3)
    parser.add_argument("--ect-window", type=int, default=40)
    parser.add_argument("--risk-high", type=float, default=1.0)
    parser.add_argument("--risk-low", type=float, default=0.5)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.daily_csv)
    if "Date" not in df.columns:
        raise ValueError("Expected a 'Date' column in daily CSV.")
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.set_index("Date").sort_index()

    need = ["Open", "High", "Low", "Close", "Volume", "Log_Returns", "GKVol_20", "VolZ_20", "EMA_20", "EMA_20_slope"]
    missing = [c for c in need if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = build_compact_features(df)

    train_mask = df.index <= pd.Timestamp(args.train_end, tz="UTC")
    val_mask = (df.index > pd.Timestamp(args.train_end, tz="UTC")) & (df.index <= pd.Timestamp(args.val_end, tz="UTC"))
    test_mask = df.index > pd.Timestamp(args.val_end, tz="UTC")

    df_tr, df_va, df_te = df.loc[train_mask], df.loc[val_mask], df.loc[test_mask]
    if df_tr.empty or df_va.empty or df_te.empty:
        raise ValueError("One of Train/Val/Test is empty; adjust train-end or val-end.")

    X_tr, X_va, X_te = df_tr[FEATURES].values, df_va[FEATURES].values, df_te[FEATURES].values
    scaler = StandardScaler().fit(X_tr)
    Xs_tr, Xs_va, Xs_te = scaler.transform(X_tr), scaler.transform(X_va), scaler.transform(X_te)

    len_tr = lengths_by_year(df_tr.index)
    len_trv = lengths_by_year(pd.concat([df_tr, df_va]).index)

    pick_best_model(Xs_tr, len_tr, k=3)
    Xs_trv = np.vstack([Xs_tr, Xs_va])
    final = fit_hmm(Xs_trv, len_trv, k=3, seed=101)

    st_trv, g_trv = decode(final, Xs_trv)
    st_te, g_te = decode(final, Xs_te)

    if args.min_dwell and args.min_dwell > 1:
        st_trv = enforce_min_dwell_gamma(st_trv, g_trv, min_run=args.min_dwell)
        st_te = enforce_min_dwell_gamma(st_te, g_te, min_run=args.min_dwell)

    last_trv_state = st_trv[-1]
    last_trv_day = pd.concat([df_tr, df_va]).index[-1]
    st_series = pd.Series(st_te, index=df_te.index)
    st_series = pd.concat([pd.Series([last_trv_state], index=[last_trv_day]), st_series])
    lag_states = st_series.shift(1)

    h = pd.read_csv(args.hourly_csv)
    if "Date" not in h.columns:
        raise ValueError("Hourly CSV must have a 'Date' column.")
    h["Date"] = pd.to_datetime(h["Date"], utc=True, errors="coerce")
    h = h.dropna(subset=["Date"]).sort_values("Date")
    h = h.set_index("Date")
    h_test = h.loc[(h.index > pd.Timestamp(args.val_end, tz="UTC"))].copy()
    if h_test.empty:
        raise ValueError("No hourly data in test window.")

    day_idx = h_test.index.normalize()
    h_test["D1_State_lag1d"] = day_idx.map(lag_states.to_dict())
    h_test = h_test.dropna(subset=["D1_State_lag1d"]).copy()
    date_col = h_test.index.tz_convert("UTC").tz_localize(None)
    h_test = h_test.reset_index(drop=True)
    h_test.insert(0, "Date", pd.to_datetime(date_col))

    tr_df = load_data_df(h_test)
    trade_log, _ = simulate_tr3(tr_df)
    trade_log.to_csv(out_dir / "trade_log_holdout_raw.csv", index=False)

    trade_log_ect = apply_ect(trade_log, window=args.ect_window, risk_high=args.risk_high, risk_low=args.risk_low)
    trade_log_ect.to_csv(out_dir / "trade_log_holdout_ect.csv", index=False)

    m = metrics_from_trades(trade_log_ect, ret_col="net_ret_scaled")
    summary_path = out_dir / "summary_ect.txt"
    summary_path.write_text(
        "Holdout summary with ECT (Train+Val fit, Test only)\n"
        f"Train end: {args.train_end}\n"
        f"Val end:   {args.val_end}\n"
        f"Trades: {m.get('Trades', 0)}\n"
        f"Final Equity: {1 + m.get('TotalReturn', float('nan')):.4f}\n"
        f"CAGR: {m.get('CAGR', float('nan')):.2%}\n"
        f"Max Drawdown: {m.get('MaxDrawdown', float('nan')):.2%}\n"
        f"Sharpe: {m.get('Sharpe', float('nan')):.2f}\n"
        f"Sortino: {m.get('Sortino', float('nan')):.2f}\n"
        f"Calmar: {m.get('Calmar', float('nan')):.2f}\n"
        f"Profit Factor: {m.get('ProfitFactor', float('nan')):.2f}\n"
        f"Win Rate: {m.get('WinRate', float('nan')):.2%}\n"
        f"Annual Volatility: {m.get('AnnualVolatility', float('nan')):.2%}\n"
    )

    print(f"Saved {out_dir / 'trade_log_holdout_raw.csv'}")
    print(f"Saved {out_dir / 'trade_log_holdout_ect.csv'}")
    print(f"Saved {summary_path}")


if __name__ == "__main__":
    main()
