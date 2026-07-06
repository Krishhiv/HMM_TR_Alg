#!/usr/bin/env python3
"""
Run out-of-sample holdout test.

Trains HMM on Train+Val, tests TR³ on unseen Test period.
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.hmm.model import (
    build_hmm_features,
    fit_hmm,
    pick_best_model,
    decode_states,
    enforce_min_dwell,
    enforce_min_dwell_causal,
    lengths_by_year,
    HMM_FEATURES,
)
from src.strategy.tr3_engine import TR3Config, prepare_data, simulate_tr3
from src.backtest.metrics import compute_metrics, print_summary


def main():
    parser = argparse.ArgumentParser(description="Run holdout backtest")
    parser.add_argument("--daily-csv", default="data/processed/btc_1d_features.csv")
    parser.add_argument("--hourly-csv", default="data/processed/btc_1h_features_tr.csv")
    parser.add_argument("--out-dir", default="outputs/logs")
    parser.add_argument("--train-end", default="2019-12-31")
    parser.add_argument("--val-end", default="2021-12-31")
    parser.add_argument("--min-dwell", type=int, default=3)
    parser.add_argument(
        "--viterbi-window", type=int, default=90,
        help="Lookback bars for causal sliding-window Viterbi on the test set",
    )
    args = parser.parse_args()
    
    out_dir = PROJECT_ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # ===== Load and process daily data for HMM =====
    print("Loading daily data...")
    daily_csv = PROJECT_ROOT / args.daily_csv
    df = pd.read_csv(daily_csv)
    
    if "Date" not in df.columns:
        raise ValueError("Expected 'Date' column in daily CSV")
    
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.set_index("Date").sort_index()
    
    # Build HMM features
    df = build_hmm_features(df)
    
    # Split by date
    train_mask = df.index <= pd.Timestamp(args.train_end, tz="UTC")
    val_mask = (df.index > pd.Timestamp(args.train_end, tz="UTC")) & \
               (df.index <= pd.Timestamp(args.val_end, tz="UTC"))
    test_mask = df.index > pd.Timestamp(args.val_end, tz="UTC")
    
    df_tr, df_va, df_te = df.loc[train_mask], df.loc[val_mask], df.loc[test_mask]
    
    if df_tr.empty or df_va.empty or df_te.empty:
        raise ValueError("One of Train/Val/Test is empty. Check date ranges.")
    
    print(f"Train: {len(df_tr)} days | Val: {len(df_va)} days | Test: {len(df_te)} days")
    
    # Scale features
    X_tr = df_tr[HMM_FEATURES].values
    X_va = df_va[HMM_FEATURES].values
    X_te = df_te[HMM_FEATURES].values
    
    scaler = StandardScaler().fit(X_tr)
    Xs_tr = scaler.transform(X_tr)
    Xs_va = scaler.transform(X_va)
    Xs_te = scaler.transform(X_te)
    
    # ===== Train HMM on Train+Val =====
    print("Training HMM on Train+Val...")
    Xs_trv = np.vstack([Xs_tr, Xs_va])
    len_trv = lengths_by_year(pd.concat([df_tr, df_va]).index)

    model = fit_hmm(Xs_trv, len_trv, k=3, seed=101)

    # Decode train+val with full Viterbi (in-sample — no lookahead concern).
    st_trv, g_trv = decode_states(model, Xs_trv)
    if args.min_dwell > 1:
        st_trv = enforce_min_dwell(st_trv, g_trv, min_run=args.min_dwell)

    # ===== Causal sliding-window Viterbi on the test set =====
    # Running full Viterbi over Xs_te at once is lookahead: state at t would
    # use future observations t+1..T.  Instead, for each test day t we run
    # Viterbi on a window [t-lookback, t-1] (excludes today's observation)
    # and take the last predicted state, which is what we would know at market
    # open on day t.
    print(f"Decoding test states (causal sliding-window, window={args.viterbi_window})...")
    Xs_all = np.vstack([Xs_trv, Xs_te])
    trv_len = len(Xs_trv)
    n_test = len(Xs_te)
    st_te = np.zeros(n_test, dtype=int)

    for t in range(n_test):
        idx = trv_len + t          # position of this test day in the combined array
        start = max(0, idx - args.viterbi_window)
        X_win = Xs_all[start:idx]  # excludes today → no lookahead
        if len(X_win) == 0:
            st_te[t] = int(st_trv[-1])  # seed with last train+val state
        else:
            st_te[t] = model.predict(X_win)[-1]

    # Causal min-dwell on the online test states (no posteriors needed)
    if args.min_dwell > 1:
        st_te = enforce_min_dwell_causal(st_te, min_run=args.min_dwell)

    # Build lagged state series for test period.
    # st_te[t] is the state known at open of test day t (derived from data up
    # to t-1), so it IS already the lagged series — we prepend the last
    # train+val state so the very first test day also has a valid lag value.
    last_trv_state = int(st_trv[-1])
    last_trv_day = pd.concat([df_tr, df_va]).index[-1]
    st_series = pd.Series(st_te, index=df_te.index)
    st_series = pd.concat([pd.Series([last_trv_state], index=[last_trv_day]), st_series])
    lag_states = st_series.shift(1)
    
    # ===== Load hourly data and merge states =====
    print("Loading hourly data...")
    hourly_csv = PROJECT_ROOT / args.hourly_csv
    h = pd.read_csv(hourly_csv)
    
    if "Date" not in h.columns:
        raise ValueError("Hourly CSV must have 'Date' column")
    
    h["Date"] = pd.to_datetime(h["Date"], utc=True, errors="coerce")
    h = h.dropna(subset=["Date"]).sort_values("Date")
    h = h.set_index("Date")
    
    # Filter to test period only
    h_test = h.loc[h.index > pd.Timestamp(args.val_end, tz="UTC")].copy()
    if h_test.empty:
        raise ValueError("No hourly data in test window")
    
    print(f"Test hourly bars: {len(h_test)}")
    
    # Merge lagged daily state
    day_idx = h_test.index.normalize()
    h_test["D1_State_lag1d"] = day_idx.map(lag_states.to_dict())
    h_test = h_test.dropna(subset=["D1_State_lag1d"]).copy()
    
    # Prepare for TR³
    date_col = h_test.index.tz_convert("UTC").tz_localize(None)
    h_test = h_test.reset_index(drop=True)
    h_test.insert(0, "Date", pd.to_datetime(date_col))
    
    # ===== Run TR³ backtest =====
    print("Running TR³ simulation...")
    config = TR3Config()
    tr_df = prepare_data(h_test, config)
    trade_log, _ = simulate_tr3(tr_df, config)
    
    # Save trade log
    trade_log_path = out_dir / "trade_log_holdout.csv"
    trade_log.to_csv(trade_log_path, index=False)
    print(f"Saved: {trade_log_path}")
    
    # Compute and display metrics
    metrics = compute_metrics(tr_df, trade_log)
    print_summary(metrics)
    
    # Save summary
    summary_path = out_dir / "summary.txt"
    with open(summary_path, "w") as f:
        f.write("Holdout Backtest Summary (Train+Val fit, Test only)\n")
        f.write(f"Train end: {args.train_end}\n")
        f.write(f"Val end: {args.val_end}\n")
        f.write(f"Trades: {metrics.get('NumTrades', 0)}\n")
        f.write(f"Final Equity: {metrics.get('FinalEquity', 1.0):.4f}\n")
        f.write(f"CAGR: {metrics.get('CAGR', 0):.2%}\n")
        f.write(f"Sharpe: {metrics.get('Sharpe', 0):.2f}\n")
        f.write(f"Profit Factor: {metrics.get('ProfitFactor', 0):.2f}\n")
        f.write(f"Win Rate: {metrics.get('WinRate', 0):.2%}\n")
        f.write(f"Max Drawdown: {metrics.get('MaxDrawdown', 0):.2%}\n")
    
    print(f"Saved: {summary_path}")


if __name__ == "__main__":
    main()
