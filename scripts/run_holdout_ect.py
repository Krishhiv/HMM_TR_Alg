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
import sys

import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# -----------------------------
# HMM config (same as btc_1d_hmm.py)
# -----------------------------
TRAIN_END = "2019-12-31"
VAL_END = "2021-12-31"
K_CANDIDATES = (3,)
RESTARTS = 10
MAX_ITER = 1500
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
        tol=1e-4,
        random_state=seed,
        min_covar=1e-5,
        startprob_prior=sp,
        transmat_prior=tp,
    )
    model.fit(X, lengths=lengths)
    if model.covariance_type == "diag" and model.covars_.ndim == 3:
        model._covars_ = np.array([np.diag(v) for v in model._covars_])
        model.covariance_type = "full"
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


def enforce_min_dwell_causal(path: np.ndarray, min_run: int = 3) -> np.ndarray:
    """
    Causal min-dwell: prevents switching to a new state unless it persists
    for at least min_run consecutive observations. Uses NO future data.
    """
    p = np.asarray(path, dtype=int)
    if min_run <= 1 or len(p) == 0:
        return p.copy()

    out = p.copy()
    current = out[0]
    pending = None
    pending_count = 0

    for i in range(1, len(out)):
        s = out[i]

        if s == current:
            pending = None
            pending_count = 0
            out[i] = current
            continue

        # s != current
        if pending is None or pending != s:
            pending = s
            pending_count = 1
        else:
            pending_count += 1

        if pending_count >= min_run:
            current = pending
            pending = None
            pending_count = 0

        out[i] = current

    return out


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
            "regime": entry_reg if entry_reg else 1, "strategy": "TR3", "exit_reason": "eod_close",
        })

    trade_log = pd.DataFrame(trades, columns=cols)
    # Shift pos by 1 to align with returns (pos[i]=1 means we hold from i to i+1, so we want ret_oo[i+1])
    # pos array recorded "in_pos" status at step i.
    # If we entered at i, in_pos=True. We want return for i+1.
    strat_rets = pd.Series(pos, index=df.index).shift(1).fillna(0.0) * df["ret_oo"]
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
    parser.add_argument("--min-dwell", type=int, default=1)
    parser.add_argument("--ect-window", type=int, default=20, help="ECT equity SMA window (lower=more responsive)")
    parser.add_argument("--risk-high", type=float, default=1.0)
    parser.add_argument("--risk-low", type=float, default=0.5)
    parser.add_argument("--tr3-params", default="", help="JSON file with TR3 parameter overrides")
    # Option to use saved model
    parser.add_argument(
        "--use-saved-model", 
        action="store_true",
        help="Use saved BTCRegimeDetector from outputs/models/btc_hmm instead of inline training"
    )
    parser.add_argument(
        "--model-dir",
        default="outputs/models/btc_hmm",
        help="Directory containing saved model.pkl, scaler.pkl, config.json"
    )
    # NEW: Walk-Forward Training flag
    parser.add_argument(
        "--walk-forward",
        action="store_true",
        help="Enable walk-forward periodic retraining (Live Simulation)"
    )
    # NEW: Sliding Viterbi window for better state detection
    parser.add_argument(
        "--viterbi-window",
        type=int,
        default=60,
        help="Size of sliding window for Viterbi decoding (uses full window of past data)"
    )
    args = parser.parse_args()

    # Override TR3 config if provided
    if args.tr3_params:
        import json
        params = json.loads(Path(args.tr3_params).read_text())
        if "best_params" in params:
            params = params["best_params"]  # Handle opt_best.json format
        print(f"Overriding TR3 params: {params}")
        TR3.update(params)

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

    # ===== BRANCHING: Use saved model or inline training =====
    if args.use_saved_model:
        # Load saved BTCRegimeDetector and use predict_online
        from src.hmm.model import BTCRegimeDetector
        
        model_dir = Path(args.model_dir)
        if not (model_dir / "model.pkl").exists():
            raise FileNotFoundError(f"No saved model found at {model_dir}. Run BTC HMM training first.")
        
        print(f"\nUsing SAVED MODEL from {model_dir}...")
        detector = BTCRegimeDetector.load_model(model_dir)
        
        # Predict online (no lookahead) for test period
        states_online = detector.predict_online(df_te, lookback=args.viterbi_window)
        
        # Create lagged state series
        # Get last state from train+val period (using full Viterbi just for this one state)
        states_trv = detector.predict(pd.concat([df_tr, df_va]))
        last_trv_state = states_trv.iloc[-1]
        
        # states_online[t] is already the state known at market open on day t (uses data up to t-1)
        # BUT its first day has no prior data when you pass df_te only -> seed it with last train+val state.
        if len(states_online) > 0:
            states_online.iloc[0] = int(last_trv_state)

        states_for_hourly = states_online.copy()
        states_for_hourly.index = states_for_hourly.index.normalize()
        
    elif args.walk_forward:
        # ===== WALK-FORWARD TRAINING (Periodic Retraining) =====
        # 1. Start with initial Train+Val period
        # 2. Predict next N days (rebalance_freq) using current model
        # 3. Retrain on sliding window (e.g. 2 years)
        # 4. Use align_states/warm_start to keep states consistent (0=Bear, 1=Neutral, 2=Bull)
        
        print("\nUsing WALK-FORWARD TRAINING (Live Simulation)...")
        from src.hmm.model import fit_hmm_warm_start, align_states, DEFAULT_CONFIG
        
        rebalance_days = 30  # Retrain every month
        training_window_days = 365 * 2  # 2 years of history
        
        # Initial training set: up to val_end (simulating start of test period)
        # We need the full history to slice windows
        start_idx = df_te.index[0]
        full_history_mask = df.index < start_idx
        
        # Initialize loop variables
        current_date = start_idx
        end_date = df_te.index[-1]
        
        states_online_list = []
        dates_online_list = []
        
        # Initial fit on [Start ... val_end]
        # Use last 2 years of train+val for strict window adherence, or full history?
        # Let's use sliding window of training_window_days ending at current_date
        
        prev_model = None
        
        while current_date <= end_date:
            # Define training window: [current_date - window, current_date)
            window_start = current_date - pd.Timedelta(days=training_window_days)
            train_mask = (df.index >= window_start) & (df.index < current_date)
            
            df_window = df.loc[train_mask]
            if len(df_window) < 100:
                raise ValueError(f"Training window too short at {current_date}")
            
            # Prepare features
            X_win = df_window[FEATURES].values
            scaler = StandardScaler().fit(X_win) # Fit scaler on current window
            Xs_win = scaler.transform(X_win)
            len_win = lengths_by_year(df_window.index)
            
            # Fit HMM
            if prev_model is None:
                # First run: Fit from scratch
                model = fit_hmm(Xs_win, len_win, k=3, seed=101)
                # Align states: Sort by Log_Returns so State 2 is Bullish (Highest Return)
                model = align_states(model, Xs_win, feature_idx_for_sort=0)
            else:
                # Retrain: Warm start from previous model + Align
                # Note: warm start implicitly tries to keep alignment, but we force alignment again
                # to be safe against label switching during EM
                model = fit_hmm_warm_start(Xs_win, len_win, prev_model=prev_model, k=3, seed=101)
                model = align_states(model, Xs_win, feature_idx_for_sort=0)
            
            prev_model = model
            
            # Predict for next `rebalance_days`
            next_rebalance = current_date + pd.Timedelta(days=rebalance_days)
            pred_mask = (df.index >= current_date) & (df.index < next_rebalance)
            df_pred = df.loc[pred_mask]
            
            if df_pred.empty:
                break
                
            # Prepare prediction features (using SAME scaler as training window)
            X_pred = df_pred[FEATURES].values
            Xs_pred = scaler.transform(X_pred)
            
            print(f"Training on window ending {current_date.date()} -> Predicting {len(df_pred)} days")
            
            # Predict day-by-day (Online)
            # For each day in the chunk, we use the trained model 'model'
            # But strictly speaking, for day t inside the chunk, we should only use data up to t
            # Since 'model' is fixed for this chunk (like a weekly/monthly model update), 
            # this is valid "live trading" simulation: model is updated only at the start of the month.
            
            # Use Viterbi/Predict on the chunk using the fixed model
            # Note: This implies we DON'T update the HMM internal params daily, only monthly.
            # But we can still use the sliding Viterbi window for state Inference.
            
            chunk_states = []
            
            # For decoding, we need history. We can append Xs_pred to Xs_win
            # But to be simple and "Saved Model" like:
            # Just predict using sliding window over the recent history we have
            
            # We need context from before current_date for the first few days of prediction
            # Let's take the last (args.viterbi_window) days from training data
            X_context = Xs_win[-args.viterbi_window:]
            
            Xs_combined = np.vstack([X_context, Xs_pred])
            context_len = len(X_context)
            
            for t in range(len(Xs_pred)):
                # Index in combined array corresponding to current day t
                # We want window ending at YESTERDAY (t-1 relative to Xs_pred, so index context_len + t)
                
                # Wait, if we use the *fixed model for the month*, we just need the observation sequence.
                # Just like 'predict_online' in Saved Model:
                
                idx = context_len + t
                start = max(0, idx - args.viterbi_window)
                X_w = Xs_combined[start:idx] # Exclude today
                
                if len(X_w) == 0:
                     chunk_states.append(0) # Fallback
                else:
                    st = model.predict(X_w)[-1]
                    chunk_states.append(st)
                    
            states_online_list.extend(chunk_states)
            dates_online_list.extend(df_pred.index)
            
            current_date = next_rebalance
            
        # Combine all predictions
        st_te_online = np.array(states_online_list)
        # Ensure we cover the full df_te (handle end-of-loop mismatch if any)
        # We iterated until end_date, so lists should match df_te rows roughly
        # Let's align by index
        states_series = pd.Series(st_te_online, index=dates_online_list)
        states_series = states_series.reindex(df_te.index).fillna(0).astype(int)
        
        # Apply min_dwell (Causal)
        if args.min_dwell > 1:
             st_te_online = enforce_min_dwell_causal(states_series.values, min_run=args.min_dwell)
             states_series = pd.Series(st_te_online, index=df_te.index)

        # states_series is ALREADY the state for today (derived from yesterday's data)
        # So it IS "lag1d". No need to shift again.
        states_for_hourly = states_series.copy()
        states_for_hourly.index = states_for_hourly.index.normalize()
    
    else:
        # Fallback / Error if neither mode selected?
        # Or keep Legacy as default if user didn't specify?
        # User said "Forget about inline training completely" -> But let's keep a stub or warning
        # For now, let's treat "no arg" as "Saved Model" or error? 
        # Let's defaults to saved model if nothing passed, or error.
        raise ValueError("Please specify --use-saved-model or --walk-forward")

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
    h_test["D1_State_lag1d"] = day_idx.map(states_for_hourly.to_dict())
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
