#!/usr/bin/env python3
"""
Experiment: intraday (4H) HMM regime + 1H TR3 trading.

Identical to the baseline run_portfolio.py EXCEPT the regime HMM runs on
resampled 4-hour bars instead of daily bars. Trading (TR3) stays on 1H.

Hypothesis: a faster-refreshing regime signal detects regime flips ~hours
earlier than the 1D HMM, which may lower drawdown or lift Sharpe in choppy
periods (e.g. 2025).

Everything else — features, k=3, allowed_regime=1, ECT, TR3 params, the
walk-forward cadence (retrain monthly on a 730-day window) — matches baseline.
"""

from __future__ import annotations

import sys
import argparse
from pathlib import Path
from math import sqrt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.features.daily_features import compute_daily_features
from src.hmm.model import fit_hmm, fit_hmm_warm_start, align_states
from scripts.run_holdout_ect import (
    TR3,
    FEATURES,
    build_compact_features,
    load_data_df,
    simulate_tr3,
    apply_ect,
    metrics_from_trades,
    lengths_by_year,
)
from scripts.run_portfolio import calc_equity_metrics, print_metrics


# ---------------------------------------------------------------------------
# Resampling
# ---------------------------------------------------------------------------

def resample_ohlcv(h: pd.DataFrame, rule: str) -> pd.DataFrame:
    """Resample a 1H OHLCV frame to `rule` (e.g. '4h'), left-labelled/closed."""
    agg = (
        h.resample(rule, label="left", closed="left")
        .agg({"Open": "first", "High": "max", "Low": "min",
              "Close": "last", "Volume": "sum"})
        .dropna()
    )
    return agg


# ---------------------------------------------------------------------------
# Intraday walk-forward regime detection
# ---------------------------------------------------------------------------

def run_intraday_regime_walkforward(
    bars_df: pd.DataFrame,
    hourly_df: pd.DataFrame,
    rule: str = "4h",
    val_end: str = "2021-12-31",
    rebalance_days: int = 30,
    window_days: int = 730,
    viterbi_window: int = 120,
    k: int = 3,
) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    """
    Walk-forward HMM regime detection on intraday (`rule`) bars, then map the
    causal state onto 1H bars and run TR3.

    Mirrors run_btc_strategy.run_btc_walkforward exactly, but the HMM operates
    on `rule` bars. state[B] is decoded from data strictly BEFORE bar B, so the
    1H bars that fall inside bar B may use state[B] without lookahead.

    Returns (trades, daily_rets, states_series[bar-indexed]).
    """
    df = build_compact_features(compute_daily_features(bars_df, n=20))

    test_start_dt = pd.Timestamp(val_end, tz="UTC")
    df_future = df.loc[df.index > test_start_dt]
    if df_future.empty:
        print("No data after validation end.")
        return pd.DataFrame(), pd.Series(dtype=float), pd.Series(dtype=float)

    start_date = df_future.index[0]
    end_date = df_future.index[-1]

    current_date = start_date
    states_online_list: list[int] = []
    dates_online_list: list[pd.Timestamp] = []
    prev_model = None

    print(f"Starting {rule} regime walk-forward from {current_date}...")

    while current_date <= end_date:
        train_start = current_date - pd.Timedelta(days=window_days)
        train_mask = (df.index >= train_start) & (df.index < current_date)
        df_train = df.loc[train_mask]

        if len(df_train) < 200:
            current_date += pd.Timedelta(days=rebalance_days)
            continue

        X_train = df_train[FEATURES].values
        scaler = StandardScaler().fit(X_train)
        Xs_train = scaler.transform(X_train)
        lens = lengths_by_year(df_train.index)

        if prev_model is None:
            model = fit_hmm(Xs_train, lens, k=k, seed=42)
        else:
            model = fit_hmm_warm_start(Xs_train, lens, prev_model=prev_model, k=k, seed=42)
        model = align_states(model, Xs_train, feature_idx_for_sort=0)
        prev_model = model

        next_rebalance = current_date + pd.Timedelta(days=rebalance_days)
        pred_mask = (df.index >= current_date) & (df.index < next_rebalance)
        df_pred = df.loc[pred_mask]
        if df_pred.empty:
            current_date = next_rebalance
            continue

        X_pred = scaler.transform(df_pred[FEATURES].values)
        X_context = Xs_train[-viterbi_window:]
        Xs_combined = np.vstack([X_context, X_pred])
        context_len = len(X_context)

        chunk_states = []
        for t in range(len(X_pred)):
            idx_in_combined = context_len + t
            w_end = idx_in_combined                       # exclude bar t (no lookahead)
            w_start = max(0, w_end - viterbi_window)
            X_w = Xs_combined[w_start:w_end]
            if len(X_w) == 0:
                chunk_states.append(0)
            else:
                chunk_states.append(int(model.predict(X_w)[-1]))

        states_online_list.extend(chunk_states)
        dates_online_list.extend(df_pred.index)
        current_date = next_rebalance

    states_series = pd.Series(states_online_list, index=dates_online_list)

    # ------------------------------------------------------------------
    # Map intraday states -> 1H bars (causal: 1H bar uses its containing
    # `rule` bar's state, which was decoded from prior bars only).
    # ------------------------------------------------------------------
    h_test = hourly_df.loc[hourly_df.index >= test_start_dt].copy()
    bar_floor = h_test.index.floor(rule)
    h_test[TR3["regime_col"]] = (
        pd.Series(bar_floor.map(states_series), index=h_test.index)
        .ffill()
        .fillna(1)
        .astype(int)
    )

    tr_df = load_data_df(h_test.reset_index())
    trades, hourly_rets = simulate_tr3(tr_df)

    hourly_rets.index = tr_df["Date"]
    daily_rets = (1 + hourly_rets).resample("D").prod() - 1.0
    daily_rets = daily_rets.fillna(0.0)

    return trades, daily_rets, states_series


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="4H-HMM regime + 1H TR3")
    parser.add_argument("--rule", default="4h",
                        help="Intraday bar for the HMM (e.g. 2h, 4h, 6h, 12h)")
    parser.add_argument("--out-dir", default="outputs/portfolio_4h")
    parser.add_argument("--val-end", default="2021-12-31")
    parser.add_argument("--ect-window", type=int, default=40)
    parser.add_argument("--risk-high", type=float, default=1.3)
    parser.add_argument("--risk-low", type=float, default=0.5)
    parser.add_argument("--viterbi-window", type=int, default=120)
    parser.add_argument("--raw-hourly",
                        default=str(PROJECT_ROOT / "data/raw/btc_1h.csv"))
    parser.add_argument("--hourly-features",
                        default=str(PROJECT_ROOT / "data/processed/btc_1h_features_tr.csv"))
    args = parser.parse_args()

    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # --- Load 1H raw (for resampling) + 1H features (for TR3) --------------
    print("Loading 1H data…")
    raw = pd.read_csv(args.raw_hourly)
    raw["Date"] = pd.to_datetime(raw["Date"], utc=True)
    raw = raw.set_index("Date").sort_index()

    hf = pd.read_csv(args.hourly_features)
    hf["Date"] = pd.to_datetime(hf["Date"], utc=True)
    hf = hf.set_index("Date").sort_index()

    # --- Resample to intraday bars for the HMM ----------------------------
    print(f"Resampling 1H -> {args.rule} for the regime HMM…")
    bars = resample_ohlcv(raw, args.rule)

    # --- Walk-forward regime + TR3 ----------------------------------------
    print(f"\nRunning {args.rule}-HMM regime walk-forward…")
    trades_raw, daily_rets_raw, states = run_intraday_regime_walkforward(
        bars, hf, rule=args.rule, val_end=args.val_end,
        viterbi_window=args.viterbi_window,
    )

    if trades_raw.empty:
        print("No trades generated.")
        return

    # --- ECT --------------------------------------------------------------
    print(f"\nApplying ECT (window={args.ect_window}, "
          f"risk_high={args.risk_high}, risk_low={args.risk_low})…")
    trades_ect = apply_ect(trades_raw, window=args.ect_window,
                           risk_high=args.risk_high, risk_low=args.risk_low)
    trades_ect.to_csv(out_path / "trades_btc_long.csv", index=False)

    risk_map = pd.Series(1.0, index=daily_rets_raw.index)
    if "risk_factor" in trades_ect.columns:
        for _, row in trades_ect.iterrows():
            t_en = pd.Timestamp(row["entry_time"])
            t_ex = pd.Timestamp(row["exit_time"])
            if t_en.tzinfo is None:
                t_en = t_en.tz_localize("UTC")
            if t_ex.tzinfo is None:
                t_ex = t_ex.tz_localize("UTC")
            risk_map.loc[t_en.normalize():t_ex.normalize()] = row["risk_factor"]

    daily_rets = daily_rets_raw * risk_map

    # --- Metrics ----------------------------------------------------------
    m_eq = calc_equity_metrics(daily_rets)
    m_tr3 = metrics_from_trades(trades_ect, "net_ret_scaled")

    print_metrics(m_tr3, f"TR3 TRADES (ECT-scaled)  [{args.rule} HMM]")
    print_metrics(m_eq, f"EQUITY CURVE  [{args.rule} HMM]")

    print("\n  Per-year breakdown:")
    print(f"  {'Year':<6} {'Return':>8}  {'Sharpe':>8}  {'Trades':>7}")
    print(f"  {'-'*34}")
    tr_years = pd.to_datetime(trades_ect["entry_time"], utc=True).dt.year
    for yr in sorted(daily_rets.index.year.unique()):
        r = daily_rets[daily_rets.index.year == yr]
        ann = (1 + r).prod() - 1
        sh = (r.mean() / r.std()) * sqrt(365) if r.std() > 0 else float("nan")
        n_tr = int((tr_years == yr).sum())
        print(f"  {yr:<6} {ann:>8.2%}  {sh:>8.2f}  {n_tr:>7}")

    # --- Save + chart -----------------------------------------------------
    equity = (1 + daily_rets).cumprod()
    pd.DataFrame({"equity": equity, "daily_ret": daily_rets}).to_csv(
        out_path / "equity_curve.csv")

    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True,
                             gridspec_kw={"height_ratios": [3, 1]})
    axes[0].plot(equity.index, equity.values, color="darkorange", linewidth=1.6,
                 label=f"{args.rule} HMM   CAGR {m_eq['CAGR']:.1%}  "
                       f"Sharpe {m_eq['Sharpe']:.2f}  MaxDD {m_eq['MaxDrawdown']:.1%}")
    axes[0].set_yscale("log")
    axes[0].set_ylabel("Equity (log)")
    axes[0].set_title(f"BTC TR3  |  {args.rule} HMM regime  vs  1D baseline")
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)

    dd = (equity - equity.cummax()) / equity.cummax()
    axes[1].fill_between(dd.index, dd.values, 0, color="darkorange", alpha=0.4)
    axes[1].set_ylabel("Drawdown")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path / "equity_chart.png", dpi=150)
    print(f"\nSaved: {out_path}/equity_chart.png  |  equity_curve.csv  |  trades_btc_long.csv")


if __name__ == "__main__":
    main()
