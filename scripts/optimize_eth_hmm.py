#!/usr/bin/env python3
"""
ETH HMM Feature Optimization

1. Tests multiple feature sets (Momentum, Volatility, Trend Strength).
2. Uses Walk-Forward Validation (Train 2017-2020, Val 2021).
3. Metric: Sharpe Ratio of 'Bullish' State (State 1) in Validation.
   - We want a state that, when active, captures consistent positive returns.
"""

import sys
import argparse
from pathlib import Path
import itertools
import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.hmm.eth_model import compute_daily_features, fit_hmm, pick_best_model, relabel_states_by_return, STATE_LABELS

# Candidate Features
FEATURE_POOL = {
    # Direction / Momentum
    "Log_Returns": ["Log_Returns"],
    "CumRet_10d": ["CumRet_10d"],
    "CumRet_30d": ["CumRet_30d"],
    "MomentumZ": ["MomentumZ"],
    
    # Volatility
    "GKVol_20": ["GKVol_20"],
    "VolZ_20": ["VolZ_20"],
    "Range": ["ClosePosInRange"],
    
    # Trend Strength / Structure
    "TrendScore": ["TrendScore"], # Dist to MAs
    "BodyPct": ["BodyPct"],
}

# Combinations to test
# We want at least 1 directional, 1 volatility, and maybe 1 structure feature
COMBOS = [
    # Baseline (BTC features adapted)
    ["Log_Returns", "GKVol_20", "VolZ_20", "TrendScore", "BodyPct", "ClosePosInRange"],
    
    # Simple Momentum
    ["Log_Returns", "CumRet_10d", "GKVol_20"],
    ["Log_Returns", "CumRet_30d", "GKVol_20"],
    
    # Momentum + TrendScore
    ["Log_Returns", "CumRet_30d", "TrendScore", "GKVol_20"],
    ["Log_Returns", "MomentumZ", "TrendScore", "GKVol_20"],
    
    # Volatility Focus
    ["Log_Returns", "GKVol_20", "VolZ_20", "CumRet_30d"],
    
    # "Clean" Trend
    ["CumRet_10d", "CumRet_30d", "TrendScore"],
]

def evaluate_combo(df: pd.DataFrame, features: list, train_end: str, val_end: str, k: int = 3):
    """
    Train HMM on [Start, Train_End], Evaluate on (Train_End, Val_End].
    Return metrics for State 1 (Bullish).
    """
    # 1. Prepare Data
    df_f = compute_daily_features(df)
    df_f = df_f.dropna(subset=features + ["Close", "Log_Returns"]).copy()
    
    # Split
    mask_tr = df_f.index <= train_end
    mask_va = (df_f.index > train_end) & (df_f.index <= val_end)
    
    df_tr = df_f.loc[mask_tr]
    df_va = df_f.loc[mask_va]
    
    if len(df_tr) < 100 or len(df_va) < 50:
        return None
    
    # 2. Train
    X_tr = df_tr[features].values
    scaler = StandardScaler().fit(X_tr)
    Xs_tr = scaler.transform(X_tr)
    
    # Fit HMM
    # Use lengths grouped by year for better init? Or just flat?
    # pick_best_model expects lengths list
    from src.hmm.eth_model import lengths_by_year
    lens = lengths_by_year(df_tr.index)
    model = pick_best_model(Xs_tr, lens, k=k)
    
    # 3. Predict on Validation (and Train for sanity)
    X_va = df_va[features].values
    Xs_va = scaler.transform(X_va)
    
    states_va = model.predict(Xs_va)
    df_va["state"] = states_va
    
    # 4. Identify Bullish State (Highest Return on TRAIN, apply to VAL)
    # We must determine mapping from TRAIN data
    states_tr = model.predict(Xs_tr)
    df_tr["state"] = states_tr
    mapping = relabel_states_by_return(df_tr, "state") # Returns {old: new} where new=1 is Bull
    
    # Apply mapping to Val
    df_va["state_mapped"] = df_va["state"].map(mapping)
    
    # 5. Metrics for State 1 (Bullish)
    bull_mask = df_va["state_mapped"] == 1
    bull_rets = df_va.loc[bull_mask, "Log_Returns"]
    
    if len(bull_rets) < 5:
        return {
            "features": features,
            "sharpe": -999, 
            "ann_ret": 0, 
            "win_rate": 0, 
            "count": 0, 
            "dwell": 0
        }
    
    # Annualized Metrics
    n = len(bull_rets)
    total_days = (df_va.index[-1] - df_va.index[0]).days / 365.0
    exposure = n / len(df_va)
    
    # Returns statistics
    mean_ret = bull_rets.mean()
    std_ret = bull_rets.std()
    
    sharpe = (mean_ret / std_ret) * np.sqrt(365) if std_ret > 0 else 0
    ann_ret = mean_ret * 365
    win_rate = (bull_rets > 0).mean()
    
    # Dwell time (avg run length)
    runs = (df_va["state_mapped"] != df_va["state_mapped"].shift()).cumsum()
    avg_dwell = df_va.groupby(runs)["state_mapped"].count().mean()
    
    # Buy & Hold benchmark
    bnh_ret = df_va["Log_Returns"].mean() * 365
    bnh_sharpe = (df_va["Log_Returns"].mean() / df_va["Log_Returns"].std()) * np.sqrt(365)
    
    return {
        "features": features,
        "sharpe": sharpe,
        "ann_ret": ann_ret,
        "win_rate": win_rate,
        "exposure": exposure,
        "dwell": avg_dwell,
        "bnh_sharpe": bnh_sharpe,
        "excess_sharpe": sharpe - bnh_sharpe
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily", required=True)
    parser.add_argument("--out", default="outputs/eth_hmm_opt.csv")
    args = parser.parse_args()
    
    print(f"Loading {args.daily}...")
    df = pd.read_csv(args.daily)
    if "time" in df.columns:
        df = df.rename(columns={"time": "Date"})
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    df = df.set_index("Date").sort_index()
    
    results = []
    
    # Fixed Train/Val Split
    # ETH Cycle: 
    # Train: 2017-2020 (Bear -> Accumulation -> Start of Bull)
    # Val: 2021 (Full Bull + Top)
    # This tests if model trained on mixed/bear data can capture the 2021 Bull run correctly.
    TRAIN_END = "2020-12-31"
    VAL_END = "2021-12-31"
    
    print(f" optimizing on Val: {TRAIN_END} -> {VAL_END}")
    
    for i, features in enumerate(COMBOS):
        print(f"\nTesting Combo {i+1}/{len(COMBOS)}: {features}")
        try:
            m = evaluate_combo(df, features, TRAIN_END, VAL_END)
            if m:
                m["id"] = i
                print(f"  > Sharpe: {m['sharpe']:.2f} | AnnRet: {m['ann_ret']:.1%} | Exp: {m['exposure']:.1%}")
                results.append(m)
            else:
                print("  > Failed (Insufficient Data)")
        except Exception as e:
            print(f"  > Error: {e}")
            
    # Save
    res_df = pd.DataFrame(results)
    res_df = res_df.sort_values("sharpe", ascending=False)
    
    print("\n" + "="*50)
    print("TOP 5 FEATURE SETS")
    print("="*50)
    print(res_df[["id", "sharpe", "ann_ret", "exposure", "features"]].head(5).to_string(index=False))
    
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    res_df.to_csv(args.out, index=False)
    print(f"\nSaved results to {args.out}")

if __name__ == "__main__":
    main()
