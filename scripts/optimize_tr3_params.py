#!/usr/bin/env python3
"""
TR3 Parameter Optimization Script

Uses walk-forward validation to find optimal parameter combinations.
Optimizes on validation period (2020-2021), tests on holdout (2022+).

IMPORTANT: Uses Calmar ratio (CAGR/MaxDD) as optimization target to
balance returns with risk, avoiding overfitting to return-only metrics.
"""

from __future__ import annotations
import argparse
import itertools
from pathlib import Path
import sys
import json
from datetime import datetime

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.run_holdout_ect import (
    fit_hmm, 
    apply_ect, metrics_from_trades,
    TR3 as DEFAULT_TR3
)

def load_data_with_features(df: pd.DataFrame) -> pd.DataFrame:
    """Load data and ensure features exist, WITHOUT dropping based on BTC HMM features."""
    df = df.copy()
    # Standardize columns if needed
    if "BodyPct" not in df.columns:
        df["BodyPct"] = (df["Close"] - df["Open"]) / (df["Open"].replace(0, np.nan))
    
    # Ensure TR3 features exist
    req_cols = ["ATR14", "MOM_ema50", "EMA200", "CLV", "ADX14", "R2_ema50", "MOM_donchian20_up"]
    missing = [c for c in req_cols if c not in df.columns]
    if missing:
        print(f"Warning: Missing columns {missing}, attempting to calculate or alias...")
    
    df = df.dropna(subset=["Close", "Open", "High", "Low"]).copy()
    
    # Ensure valid_bar exists
    df["valid_bar"] = True
    
    # Debug Stats
    if "D1_State_lag1d" in df.columns:
        print(f"DEBUG DATA: Regime 1 count: {(df['D1_State_lag1d'] == 1).sum()}")
        trend = (df["MOM_ema50"] > df["EMA200"]) & (df["Close"] > df["MOM_ema50"])
        print(f"DEBUG DATA: Trend OK count: {trend.sum()}")
        overlap = (df['D1_State_lag1d'] == 1) & trend
        print(f"DEBUG DATA: Overlap count: {overlap.sum()}")

    return df


def simulate_tr3_with_params(df: pd.DataFrame, params: dict):
    """Run TR3 simulation with custom parameters."""
    R = params
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
    fee = 0.0
    LEVERAGE = 1.0
    MAX_LOSS_CAP = 0.08

    entry_price = entry_time = entry_bar_high = high_since_entry = entry_reg = be_armed_since = None

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
                continue

            hh = df["High"].iat[j]
            if pd.notna(hh):
                high_since_entry = max(high_since_entry, hh)

            close_j = df["Close"].iat[j]
            ema50_j = df["MOM_ema50"].iat[j]
            atr_j = df["ATR14"].iat[j] if pd.notna(df["ATR14"].iat[j]) else None
            clv_j = df["CLV"].iat[j]

            advance_atr = ((high_since_entry - entry_price) / atr_j) if (atr_j and atr_j > 0) else 0.0
            exit_now, reason = False, "rule"

            use_fth = not (advance_atr >= R.get("fth_disable_after_atr", np.inf))

            can_arm_be = (atr_j is not None) and (advance_atr >= R.get("be_activate_atr", np.inf)) \
                         and (advance_atr < R.get("be_disable_after_atr", np.inf))
            if (be_armed_since is None) and can_arm_be:
                be_armed_since = df["Date"].iat[j]

            if advance_atr >= R.get("be_disable_after_atr", np.inf):
                be_armed_since = None

            if be_armed_since is not None:
                be_can_fire = True
                if R.get("be_one_bar_delay", False) and be_armed_since == df["Date"].iat[j]:
                    be_can_fire = False
                if be_can_fire:
                    be_level = entry_price + R.get("be_cushion_atr", 0) * atr_j
                    if close_j <= be_level:
                        exit_now, reason = True, "breakeven"

            if use_fth and not exit_now:
                if clv_j < R.get("clv_fail_max", 0):
                    exit_now, reason = True, "fth_clv"
                fail_level = entry_bar_high - R.get("fail_level_atr", 0) * atr_j
                if close_j < fail_level:
                    exit_now, reason = True, "fth_level"

            if not exit_now:
                ema_break = close_j < ema50_j
                relax_ab = advance_atr >= R.get("ema_break_relax_after_atr", np.inf)
                if ema_break:
                    if relax_ab:
                        cushion = R.get("ema_break_cushion_atr", 0) * atr_j
                        if close_j < ema50_j - cushion:
                            exit_now, reason = True, "ema50_relaxed"
                    else:
                        exit_now, reason = True, "ema50_break"

            if not exit_now:
                mult = R.get("trail_mult_base", 2.5)
                if advance_atr > 1.0:
                    mult = R.get("trail_mult_1", 3.5)
                if advance_atr > 2.0:
                    mult = R.get("trail_mult_2", 4.5)
                trail = high_since_entry - mult * atr_j
                if close_j < trail:
                    exit_now, reason = True, "trail_atr"

            if exit_now:
                exit_time = df["Date"].iat[i]
                exit_price = df["Open"].iat[i]
                gross_ret = (exit_price / entry_price) - 1.0
                net_ret = gross_ret * LEVERAGE
                net_ret = max(net_ret, -MAX_LOSS_CAP)

                trades.append({
                    "entry_time": entry_time, "entry_price": entry_price,
                    "exit_time": exit_time, "exit_price": exit_price,
                    "gross_ret": gross_ret, "net_ret": net_ret,
                    "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
                    "regime": entry_reg, "strategy": "TR3", "exit_reason": reason,
                })
                in_pos = False
                entry_price = entry_time = entry_bar_high = high_since_entry = entry_reg = be_armed_since = None

    if in_pos:
        i = len(df) - 1
        exit_time = df["Date"].iat[i]
        exit_price = df["Open"].iat[i]
        gross_ret = (exit_price / entry_price) - 1.0
        net_ret = gross_ret * LEVERAGE
        net_ret = max(net_ret, -MAX_LOSS_CAP)
        trades.append({
            "entry_time": entry_time, "entry_price": entry_price,
            "exit_time": exit_time, "exit_price": exit_price,
            "gross_ret": gross_ret, "net_ret": net_ret,
            "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
            "regime": 1, "strategy": "TR3", "exit_reason": "eod_close",
        })

    return pd.DataFrame(trades, columns=cols)


# Define parameter search space
PARAM_GRID = {
    # Entry filters
    "adx_min": [12, 14, 16, 18],
    "r2_min": [0.08, 0.10, 0.12],
    "clv_min": [0.50, 0.55, 0.60],
    
    # FTH exits
    "fth_disable_after_atr": [0.4, 0.5, 0.6, 0.75],
    "clv_fail_max": [0.30, 0.35, 0.40],
    
    # Breakeven
    "be_activate_atr": [0.5, 0.75, 1.0],
    
    # Trailing stop
    "trail_mult_base": [2.0, 2.5, 3.0],
}


def evaluate_params(params: dict, h_val: pd.DataFrame) -> dict:
    """Evaluate a parameter set on validation data."""
    try:
        tr_df = load_data_with_features(h_val)
        trades = simulate_tr3_with_params(tr_df, params)
        
        if len(trades) < 10:
            return {"calmar": -np.inf, "cagr": 0, "max_dd": 0, "trades": 0}
        
        trades_ect = apply_ect(trades.reset_index(drop=True), window=30, risk_high=1.0, risk_low=0.5)
        m = metrics_from_trades(trades_ect, "net_ret_scaled")
        
        # Note: metrics_from_trades returns PascalCase keys
        return {
            "calmar": float(m.get("Calmar", 0)),
            "cagr": float(m.get("CAGR", 0)),
            "max_dd": float(m.get("MaxDrawdown", 0)),
            "sharpe": float(m.get("Sharpe", 0)),
            "trades": len(trades),
        }
    except Exception as e:
        return {"calmar": -np.inf, "cagr": 0, "max_dd": 0, "trades": 0, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="TR3 Parameter Optimization")
    parser.add_argument("--hourly-csv", required=True, help="Hourly data with TR features")
    parser.add_argument("--val-start", default="2020-01-01")
    parser.add_argument("--val-end", default="2021-12-31")
    parser.add_argument("--max-combos", type=int, default=500, help="Max combinations to test")
    parser.add_argument("--out-file", default="outputs/opt_results.json")
    args = parser.parse_args()

    print("="*60)
    print("TR3 PARAMETER OPTIMIZATION")
    print("="*60)
    
    # Load hourly data
    h = pd.read_csv(args.hourly_csv)
    h["Date"] = pd.to_datetime(h["Date"], utc=True)
    h = h.set_index("Date").sort_index()
    
    # Validation period
    val_start = pd.Timestamp(args.val_start, tz="UTC")
    val_end = pd.Timestamp(args.val_end, tz="UTC")
    h_val = h.loc[(h.index >= val_start) & (h.index <= val_end)].copy()
    
    print(f"\nValidation period: {val_start.date()} to {val_end.date()}")
    print(f"Validation hours: {len(h_val)}")
    
    # Prepare validation data
    # Only force regime=1 if column missing (legacy behavior). Otherwise respect input.
    if "D1_State_lag1d" not in h_val.columns:
        print("Warning: Regime column missing, defaulting to 1 (Bullish) for all bars.")
        h_val["D1_State_lag1d"] = 1
    date_col = h_val.index.tz_convert("UTC").tz_localize(None)
    h_val = h_val.reset_index(drop=True)
    h_val.insert(0, "Date", pd.to_datetime(date_col))
    
    # Generate combinations
    keys = list(PARAM_GRID.keys())
    values = list(PARAM_GRID.values())
    all_combos = list(itertools.product(*values))
    
    print(f"\nTotal possible combinations: {len(all_combos)}")
    
    # Limit combinations if too many
    if len(all_combos) > args.max_combos:
        np.random.seed(42)
        indices = np.random.choice(len(all_combos), args.max_combos, replace=False)
        all_combos = [all_combos[i] for i in indices]
        print(f"Sampling {args.max_combos} combinations")
    
    # Test each combination
    results = []
    base_params = DEFAULT_TR3.copy()
    
    print(f"\nTesting {len(all_combos)} combinations...")
    
    for i, combo in enumerate(all_combos):
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(all_combos)}")
        
        # Build params
        params = base_params.copy()
        for k, v in zip(keys, combo):
            params[k] = v
        
        metrics = evaluate_params(params, h_val.copy())
        
        results.append({
            "params": {k: v for k, v in zip(keys, combo)},
            "metrics": metrics,
        })
    
    # Sort by Calmar ratio
    results.sort(key=lambda x: x["metrics"]["calmar"], reverse=True)
    
    print("\n" + "="*60)
    print("TOP 10 PARAMETER SETS (by Calmar)")
    print("="*60)
    
    for i, r in enumerate(results[:10]):
        m = r["metrics"]
        print(f"\n{i+1}. Calmar={m['calmar']:.2f}, CAGR={m['cagr']*100:.1f}%, DD={m['max_dd']*100:.1f}%, Trades={m['trades']}")
        for k, v in r["params"].items():
            print(f"   {k}: {v}")
    
    # Save results
    out_path = Path(args.out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    output = {
        "timestamp": datetime.now().isoformat(),
        "val_period": f"{args.val_start} to {args.val_end}",
        "best_params": results[0]["params"],
        "best_metrics": results[0]["metrics"],
        "all_results": results[:50],  # Top 50
    }
    
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\nResults saved to: {out_path}")
    
    # Show best vs default comparison
    print("\n" + "="*60)
    print("BEST vs DEFAULT")
    print("="*60)
    
    default_metrics = evaluate_params(base_params, h_val.copy())
    best_metrics = results[0]["metrics"]
    
    print(f"\nDefault: Calmar={default_metrics['calmar']:.2f}, CAGR={default_metrics['cagr']*100:.1f}%")
    print(f"Best:    Calmar={best_metrics['calmar']:.2f}, CAGR={best_metrics['cagr']*100:.1f}%")
    
    if best_metrics["calmar"] > default_metrics["calmar"]:
        print("\n✅ Found better parameters!")
        print("\nRecommended changes:")
        for k, v in results[0]["params"].items():
            if v != base_params.get(k):
                print(f"  {k}: {base_params.get(k)} → {v}")


if __name__ == "__main__":
    main()
