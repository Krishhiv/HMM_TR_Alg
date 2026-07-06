#!/usr/bin/env python3
"""
BTC Strategy Runner (HMM-TR3)
Supports Walk-Forward Re-training for Portfolio Integration.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import HMM logic from model.py (Shared BTC logic)
from src.hmm.model import fit_hmm, fit_hmm_warm_start, align_states, BTCRegimeDetector
from scripts.run_holdout_ect import (
    TR3 as TR3_CONFIG,
    FEATURES as HMM_FEATURES,
    build_compact_features,
    load_data_df,
    simulate_tr3,
    apply_ect,
    metrics_from_trades,
    lengths_by_year
)

def run_btc_walkforward(
    daily_df: pd.DataFrame,
    hourly_df: pd.DataFrame,
    train_end: str = "2019-12-31",
    val_end: str = "2021-12-31",
    rebalance_days: int = 30,
    window_days: int = 730,
    viterbi_window: int = 60,
    min_dwell: int = 1,
) -> tuple[pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    """
    Run Walk-Forward Analysis for BTC.
    
    1. Initial Train on data up to val_end (simulating live start).
    2. Predict next month.
    3. Retrain on sliding window.
    4. Repeat.
    """
    
    # 1. Setup Data
    df = build_compact_features(daily_df)
    
    # Identify Testing Period (Post-Validation)
    # In a real "Walk-Forward", we want to simulate the ENTIRE period from val_end onwards.
    test_start_dt = pd.Timestamp(val_end, tz="UTC")
    
    # We also need coverage for the initial training
    # Initial Training Window: [test_start - window, test_start)
    
    # Slice the "Future" data we want to predict
    df_future = df.loc[df.index > test_start_dt]
    if df_future.empty:
        print("No data after validation end.")
        return pd.DataFrame()
        
    start_date = df_future.index[0]
    end_date = df_future.index[-1]
    
    current_date = start_date
    states_online_list = []
    dates_online_list = []
    
    prev_model = None
    
    print(f"Starting BTC Walk-Forward from {current_date.date()}...")
    
    while current_date <= end_date:
        # Define Training Window: [current_date - window, current_date)
        train_start = current_date - pd.Timedelta(days=window_days)
        train_mask = (df.index >= train_start) & (df.index < current_date)
        df_train = df.loc[train_mask]
        
        if len(df_train) < 100:
            print(f"Skipping {current_date}: Insufficient history.")
            current_date += pd.Timedelta(days=rebalance_days)
            continue
            
        # Fit HMM
        X_train = df_train[HMM_FEATURES].values
        scaler = StandardScaler().fit(X_train)
        Xs_train = scaler.transform(X_train)
        lens = lengths_by_year(df_train.index)
        
        if prev_model is None:
            # First fit
            model = fit_hmm(Xs_train, lens, k=3, seed=42)
            model = align_states(model, Xs_train, feature_idx_for_sort=0) # 0=Log_Returns
        else:
            # Retrain (Warm Start)
            model = fit_hmm_warm_start(Xs_train, lens, prev_model=prev_model, k=3, seed=42)
            model = align_states(model, Xs_train, feature_idx_for_sort=0)
            
        prev_model = model
        
        # Predict Next Chunk
        next_rebalance = current_date + pd.Timedelta(days=rebalance_days)
        pred_mask = (df.index >= current_date) & (df.index < next_rebalance)
        df_pred = df.loc[pred_mask]
        
        if df_pred.empty:
            break
            
        # Prepare Prediction (Sliding Viterbi)
        # We need context from history to validly decode the first few days of the chunk
        # Xs_combined = [History(Last 60d) + Future(Chunk)]
        
        X_pred = df_pred[HMM_FEATURES].values
        Xs_pred = scaler.transform(X_pred)
        
        # Context from training data
        X_context = Xs_train[-viterbi_window:]
        Xs_combined = np.vstack([X_context, Xs_pred])
        context_len = len(X_context)
        
        chunk_states = []
        for t in range(len(Xs_pred)):
            # Causal Viterbi: Window covers [t-window, t-1] (relative to prediction day)
            # Actually, decode_states uses the *observation* at t to guess state at t.
            # But in "predict_online", we usually say state[t] is knowing obs[t]? 
            # TR3 logic: "Day T trading uses Day T-1 state".
            # So here we want to output the state for Day T based on data UP TO Day T.
            # Wait, `predict_online` in `model.py` uses `X_window = Xs[start:t]` (Excludes today).
            # This means state[t] is prediction for today based on yesterday. 
            
            # Let's match correct logic:
            # Standard HMM: `predict([obs_0...obs_t])` -> `state_t`. 
            # This uses obs_t (Today's Close).
            # If we trade on hourly data for Day T, we usually DON'T know Day T close yet.
            # So we must use `state[t-1]`.
            # `run_holdout_ect.py` does: `df_h["D1_State_lag1d"] = day_idx.map(states)`
            # So `states` series should contain State for Day T, derived from data *available* at Day T open.
            
            # If `predict_online` uses `X_window = Xs[start:t]` (0..t-1), then it predicts `next_state`?
            # No, standard `predict` returns state sequence for the input.
            # If we pass `Xs[0..t-1]`, we get states for `0..t-1`. The last one is `state[t-1]`.
            # So we use `state[t-1]` (Yesterday) as the regime for Today.
            
            # Here we want to generate the series of states.
            # For day T in the chunk:
            # We have data up to T (Close). 
            # BUT we want to simulate "What state did we think we were in at 00:00 UTC?"
            # That would be `predict(Data up to T-1)[-1]`.
            
            # So for each day in `df_pred`:
            idx_in_combined = context_len + t
            # Data available at T 00:00 is up to T-1 (index idx_in_combined - 1)
            # Window end = idx_in_combined
            # Window start = idx_in_combined - viterbi_window
            
            # If we include `Xs_combined[idx_in_combined]`, that's Day T data (Lookahead).
            # So we want `Xs_combined[start : idx_in_combined]`.
            
            w_end = idx_in_combined
            w_start = max(0, w_end - viterbi_window)
            
            X_w = Xs_combined[w_start : w_end]
            
            if len(X_w) == 0:
                chunk_states.append(0)
            else:
                s = model.predict(X_w)[-1]
                chunk_states.append(s)
                
        states_online_list.extend(chunk_states)
        dates_online_list.extend(df_pred.index)
        
        current_date = next_rebalance

    # 4. Map to Hourly & Simulate
    states_series = pd.Series(states_online_list, index=dates_online_list)
    
    # Min Dwell
    if min_dwell > 1:
        # Simple causal min dwell
        # (Copy logic if needed, or skip for simplicity as BTC min_dwell=1 usually)
        pass
        
    # Map to Hourly
    # Filter hourly df to test period
    h_test = hourly_df.loc[hourly_df.index >= test_start_dt].copy()
    day_idx = h_test.index.normalize()
    
    # We generated `states_series` where `states_series[T]` = Regime derived from T-1 data.
    # So this IS already the lagged state for Day T.
    h_test["D1_State_lag1d"] = day_idx.map(states_series).fillna(0).astype(int)
    
    # Load for TR3 (reset index to make Date available as column)
    tr_df = load_data_df(h_test.reset_index())
    
    # Run TR3
    # Run TR3
    trades, hourly_rets = simulate_tr3(tr_df)
    
    # Process for Portfolio
    # 1. Daily Returns (Sum of hourly log returns approx, or simple sum of linear)
    # hourly_rets is pos * ret_oo
    hourly_rets.index = tr_df["Date"]
    daily_rets = (1 + hourly_rets).resample("D").prod() - 1.0
    daily_rets = daily_rets.fillna(0.0)
    
    # 2. Active Mask (Days where we had an open position)
    # Reconstruct from trade log to be precise about "Time in Market"
    active_mask = pd.Series(False, index=daily_rets.index)
    
    if not trades.empty:
        # trades["entry_time"] convert to dt
        entry_times = pd.to_datetime(trades["entry_time"], utc=True)
        exit_times = pd.to_datetime(trades["exit_time"], utc=True)
        
        for en, ex in zip(entry_times, exit_times):
            # Mark days covered by this trade
            # Normalize to dates
            d_start = en.normalize()
            d_end = ex.normalize()
            active_mask.loc[d_start:d_end] = True
            
    return trades, daily_rets, active_mask, states_series

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily", required=True)
    parser.add_argument("--hourly", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    
    # Load raw
    d = pd.read_csv(args.daily)
    d["Date"] = pd.to_datetime(d["Date"], utc=True)
    d = d.set_index("Date").sort_index()

    h = pd.read_csv(args.hourly)
    h["Date"] = pd.to_datetime(h["Date"], utc=True)
    h = h.set_index("Date").sort_index()

    # run_btc_walkforward returns (trades, daily_rets, active_mask)
    trades, _daily_rets, _active_mask, _states = run_btc_walkforward(d, h)

    # Save
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    trades.to_csv(out_path, index=False)

    # Stats
    m = metrics_from_trades(apply_ect(trades), "net_ret_scaled")
    print("BTC Walk-Forward Results:")
    print(m)

if __name__ == "__main__":
    main()
