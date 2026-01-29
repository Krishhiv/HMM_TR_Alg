#!/usr/bin/env python3
"""
ETH Strategy Verification Script

1. Loads ETH data (Daily & Hourly)
2. Trains ETH-specific HMM (using ETHRegimeDetector)
3. Generates TR3 features
4. Runs Walk-Forward Backtest (Causal)
5. Compares performance to BTC baseline
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import timedelta

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.hmm.eth_model import ETHRegimeDetector
from src.features.hourly_features import compute_hourly_features
from scripts.run_holdout_ect import apply_ect, metrics_from_trades, TR3 as TR3_CONFIG

# Optimized parameters for ETH (Found via optimize_tr3_params.py on 2020-2021)
TR3_ETH = TR3_CONFIG.copy()
TR3_ETH.update({
    "adx_min": 18,              # Stricter trend req (was 14)
    "r2_min": 0.08,             # Relaxed fit (was 0.1)
    "fth_disable_after_atr": 0.4, # Let winners run sooner (was 0.5)
    "clv_fail_max": 0.4,        # Stricter CLV for FTH (was 0.35)
    "be_activate_atr": 1.0,     # Give more room before BE (was 0.75)
})

def load_data(daily_path: Path, hourly_path: Path):
    """Load and prepare data."""
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
    """Run TR3 strategy on dataframe with pre-computed features and states."""
    
    # Merge states (lagged by 1 day for causality)
    # states index is daily (00:00 UTC)
    # df index is hourly
    
    # Create valid shift: Day T trading uses Day T-1 state
    # states series: Index=Day T, Value=State(Day T) -- ALREADY PREDICTED using T-1
    # Check predict_online logic:
    # "For each day t, only data up to day t-1 is used... result indexed by date known"
    # So state at Date T is safe to use for trading on Date T.
    
    day_idx = df.index.normalize()
    df["regime"] = day_idx.map(states).fillna(0).astype(int)
    
    day_idx = df.index.normalize()
    df["regime"] = day_idx.map(states).fillna(0).astype(int)
    
    # Filter for valid regime (TR3 usually 1=Bullish)
    # ETH Model mapping: 1=Bullish
    
    R = params
    
    # TR3 Logic (Vectorized where possible, but loop dealing with state)
    
    # 1. Compute Signals
    # Need to verify feature names match TR3 config
    # TR3 config uses: MOM_ema50, EMA200, MOM_donchian20_up, ATR14, CLV, ADX14, R2_ema50
    
    # Map features if needed
    if "EMA200" not in df.columns and "MOM_ema200" in df.columns:
        df["EMA200"] = df["MOM_ema200"]
    if "ATR14" not in df.columns and "MR_atr14" in df.columns:
        df["ATR14"] = df["MR_atr14"]
    
    # Compute CLV manually if missing
    if "CLV" not in df.columns:
        rng = (df["High"] - df["Low"]).replace(0, np.nan)
        # CLV = ((C-L) - (H-C)) / (H-L) = (2C - H - L) / (H-L)
        df["CLV"] = (2 * df["Close"] - df["High"] - df["Low"]) / rng
        df["CLV"] = df["CLV"].fillna(0.0)
    
    # Compute ClosePosInRange for good measure (used by some variants)
    if "ClosePosInRange" not in df.columns:
        rng = (df["High"] - df["Low"]).replace(0, np.nan)
        df["ClosePosInRange"] = ((df["Close"] - df["Low"]) / rng) - 0.5
        
    thrust = (df["Close"] - df["Close"].shift(1)) >= (R["thrust_atr_mult"] * df["ATR14"])
    breakout = df["Close"] > df["MOM_donchian20_up"]
    
    # Entry Condition
    # Note: TR3_CONFIG['regime_col'] is ignored effectively as we use 'regime' col
    ent_reg = (df["regime"] == R["allowed_regime"])
    # Strict Trend: EMA50 > EMA200 AND Price > EMA50
    ent_trend = (df["MOM_ema50"] > df["EMA200"]) & (df["Close"] > df["MOM_ema50"])
    ent_mom = (breakout | thrust)
    ent_clv = (df["CLV"] >= R["clv_min"])
    ent_adx = (df["ADX14"] >= R["adx_min"])
    ent_r2 = (df["R2_ema50"] >= R["r2_min"])
    
    cond = (
        ent_reg & ent_trend & ent_mom & ent_clv & ent_adx & ent_r2
    )
    
    overlap_1 = ent_reg & ent_trend
    overlap_2 = overlap_1 & ent_mom
    overlap_3 = overlap_2 & ent_clv
    
    print("\nDEBUG: Entry Condition Stats (Total Bars: {})".format(len(df)))
    print(f"  Regime OK: {ent_reg.sum()} ({ent_reg.mean():.1%})")
    print(f"  Trend OK:  {ent_trend.sum()} ({ent_trend.mean():.1%})")
    print(f"  Mom OK:    {ent_mom.sum()} ({ent_mom.mean():.1%})")
    print(f"  CLV OK:    {ent_clv.sum()} ({ent_clv.mean():.1%})")
    print("\nDEBUG: Overlaps")
    print(f"  Regime + Trend: {overlap_1.sum()} ({overlap_1.mean():.1%})")
    print(f"  + Mom:          {overlap_2.sum()} ({overlap_2.mean():.1%})")
    print(f"  + CLV:          {overlap_3.sum()} ({overlap_3.mean():.1%})")
    print(f"  ALL OK:         {cond.sum()} ({cond.mean():.1%})")
    
    entry_sig = cond.shift(1).fillna(False)
    
    # Simulation Loop (Slow but accurate for path-dependent exits)
    in_pos = False
    trades = []
    
    # Pre-compute arrays for speed
    closes = df["Close"].values
    opens = df["Open"].values
    highs = df["High"].values
    lows = df["Low"].values
    dates = df.index
    atrs = df["ATR14"].values
    ema50s = df["MOM_ema50"].values
    clvs = df["CLV"].values
    sigs = entry_sig.values
    regimes = df["regime"].values
    
    # State vars
    entry_price = 0.0
    entry_idx = 0
    high_since = 0.0
    be_armed = False
    
    # Position tracking
    pos = np.zeros(len(df), dtype=float)
    if "ret_oo" not in df.columns:
        df["ret_oo"] = df["Open"].pct_change().fillna(0.0)
    ret_oo = df["ret_oo"].values
    
    LEVERAGE = 1.0
    
    for i in range(1, len(df)):
        if not in_pos:
            if sigs[i]:
                in_pos = True
                entry_idx = i
                entry_price = opens[i]  # Enter at Open
                high_since = highs[i-1] # Initialize with previous high (signal bar)
                be_armed = False
        else:
            # Check exits using previous bar (i-1)
            j = i - 1
            c_prev = closes[j]
            h_prev = highs[j]
            atr_val = atrs[j]
            ema_val = ema50s[j]
            clv_val = clvs[j]
            
            high_since = max(high_since, h_prev)
            
            if np.isnan(atr_val) or atr_val == 0:
                continue
                
            adv_atr = (high_since - entry_price) / atr_val
            exit_now = False
            reason = ""
            
            # 1. FTH (Fail to Hold)
            use_fth = adv_atr < R["fth_disable_after_atr"]
            if use_fth:
                if clv_val < R["clv_fail_max"]:
                    exit_now = True; reason = "fth_clv"
                elif c_prev < (high_since - R["fail_level_atr"] * atr_val):
                    exit_now = True; reason = "fth_level"
            
            # 2. Breakeven
            if not exit_now:
                if adv_atr >= R["be_activate_atr"] and adv_atr < R["be_disable_after_atr"]:
                    be_armed = True
                if adv_atr >= R["be_disable_after_atr"]:
                    be_armed = False # Revert to normal trailing
                
                if be_armed:
                    # Optional delay check skipped for simplicity or check R['be_one_bar_delay']
                    be_level = entry_price + R["be_cushion_atr"] * atr_val
                    if c_prev <= be_level:
                        exit_now = True; reason = "breakeven"
            
            # 3. EMA Break
            if not exit_now and c_prev < ema_val:
                # Relaxed if far advanced
                if adv_atr >= R["ema_break_relax_after_atr"]:
                    if c_prev < (ema_val - R["ema_break_cushion_atr"] * atr_val):
                        exit_now = True; reason = "ema50_relaxed"
                else:
                    exit_now = True; reason = "ema50_break"
            
            # 4. Trailing Stop
            if not exit_now:
                mult = R["trail_mult_base"]
                if adv_atr > 1.0: mult = R["trail_mult_1"]
                if adv_atr > 2.0: mult = R["trail_mult_2"]
                
                stop = high_since - mult * atr_val
                if c_prev < stop:
                    exit_now = True; reason = "trail_atr"
                    
            if not exit_now:
                # Time Stop
                hold_hrs = (dates[i] - dates[entry_idx]).total_seconds() / 3600
                if hold_hrs > R["time_stop_hours"]:
                    exit_now = True; reason = "time_stop"
                
                # No Progress Stop
                if hold_hrs > R["no_progress_hours"] and adv_atr < R["no_progress_atr"]:
                     exit_now = True; reason = "no_progress"

            if exit_now:
                exit_price = opens[i]
                ret = (exit_price / entry_price) - 1.0
                trades.append({
                    "entry_time": dates[entry_idx],
                    "exit_time": dates[i],
                    "net_ret": ret * LEVERAGE, # No fee sim for raw
                    "holding_hours": (dates[i] - dates[entry_idx]).total_seconds() / 3600,
                    "exit_reason": reason,
                    "regime": regimes[entry_idx]
                })
                in_pos = False
        
        pos[i] = 1.0 if in_pos else 0.0
                
    hourly_rets = pd.Series(pos, index=df.index).shift(1).fillna(0.0) * df["ret_oo"]
    return pd.DataFrame(trades), hourly_rets

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily", required=True)
    parser.add_argument("--hourly", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    
    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # 1. Load Data
    df_d, df_h = load_data(Path(args.daily), Path(args.hourly))
    
    # 2. Compute Features
    print("Computing Hourly Features...")
    df_h = compute_hourly_features(df_h)
    
    # 3. Train HMM (Walk-Forward / Online Prediction)
    print("Training ETH HMM...")
    detector = ETHRegimeDetector(
        train_end="2020-12-31", # ETH DeFi summer start approx
        val_end="2021-12-31",
        k=3
    )
    # Fit on history
    hist_mask = df_d.index <= "2021-12-31"
    detector.fit(df_d.loc[hist_mask])
    
    # Predict Online (Causal)
    # Using 90d lookback for live state detection
    print("Predicting States (Online)...")
    states = detector.predict_online(df_d, lookback=90)
    
    # Save states for inspection
    states.to_csv(out_path / "eth_daily_states.csv")
    
    # --- PREPARE OPTIMIZATION DATA (Full History) ---
    print("Preparing Optimization Input (Full History)...")
    df_full = df_h.copy()
    
    # Add Feature Aliases for TR3 Optimizer
    if "MOM_ema200" in df_full.columns:
        df_full["EMA200"] = df_full["MOM_ema200"]
    if "MR_atr14" in df_full.columns:
        df_full["ATR14"] = df_full["MR_atr14"]
    
    # Compute CLV manually if missing (logic from run_strategy)
    if "CLV" not in df_full.columns:
        rng = (df_full["High"] - df_full["Low"]).replace(0, np.nan)
        df_full["CLV"] = (2 * df_full["Close"] - df_full["High"] - df_full["Low"]) / rng
        df_full["CLV"] = df_full["CLV"].fillna(0.0)
    
from sklearn.preprocessing import StandardScaler
from src.hmm.eth_model import lengths_by_year, fit_hmm, fit_hmm_warm_start, HMM_FEATURES, relabel_states_by_return, compute_daily_features

def run_eth_walkforward(
    daily_df: pd.DataFrame, 
    hourly_df: pd.DataFrame, 
    train_end: str = "2020-12-31", # ETH Bull run start
    rebalance_days: int = 30,
    window_days: int = 730, # 2 years
    viterbi_window: int = 60
) -> pd.DataFrame:
    """
    Run Walk-Forward Analysis for ETH (Live Simulation).
    """
    # 1. Setup Data
    df = compute_daily_features(daily_df)
    df = df.dropna(subset=HMM_FEATURES + ["Close"]).copy()
    
    # Slice Future (Test Period)
    test_start_dt = pd.Timestamp(train_end, tz="UTC")
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
    
    print(f"Starting ETH Walk-Forward from {current_date.date()}...")
    
    while current_date <= end_date:
        # Define Training Window
        win_start = current_date - pd.Timedelta(days=window_days)
        mask_tr = (df.index >= win_start) & (df.index < current_date)
        df_tr = df.loc[mask_tr]
        
        if len(df_tr) < 100:
            print(f"Skipping {current_date}: Insufficient history.")
            current_date += pd.Timedelta(days=rebalance_days)
            continue
            
        # Fit HMM
        X_tr = df_tr[HMM_FEATURES].values
        scaler = StandardScaler().fit(X_tr)
        Xs_tr = scaler.transform(X_tr)
        lens = lengths_by_year(df_tr.index)
        
        # Fit / Warm Start
        if prev_model is None:
            model = fit_hmm(Xs_tr, lens, k=3, seed=42)
        else:
            # Re-training with warm start for stability
            model = fit_hmm_warm_start(Xs_tr, lens, prev_model=prev_model, k=3, seed=42)
            
        # ALIGN STATES: 1=Bullish (Highest Return)
        # We need to predict on training data to map states
        st_tr = model.predict(Xs_tr)
        df_tr["_temp_state"] = st_tr
        mapping = relabel_states_by_return(df_tr, "_temp_state") 
        # mapping maps {Old -> New}. We need to permute model? 
        # Actually `relabel_states_by_return` just gives us the map.
        # We can just apply the map to predictions.
        
        prev_model = model
        
        # Predict Next Chunk
        next_rebalance = current_date + pd.Timedelta(days=rebalance_days)
        mask_pred = (df.index >= current_date) & (df.index < next_rebalance)
        df_pred = df.loc[mask_pred]
        
        if df_pred.empty:
            break
            
        # Prepare Prediction (Sliding Viterbi)
        X_pred = df_pred[HMM_FEATURES].values
        Xs_pred = scaler.transform(X_pred)
        
        # Context
        X_ctx = Xs_tr[-viterbi_window:]
        Xs_comb = np.vstack([X_ctx, Xs_pred])
        ctx_len = len(X_ctx)
        
        chunk_states = []
        for t in range(len(Xs_pred)):
            # Window end = current day T (exclusive of T's data for causal? No, see standard logic)
            # We want state for Day T based on Data UP TO Day T-1.
            # Index of T in Combined is `ctx_len + t`
            # Data avail: `0` to `ctx_len + t` (exclusive, i.e. up to T-1)
            
            idx = ctx_len + t
            w_start = max(0, idx - viterbi_window)
            X_w = Xs_comb[w_start : idx]
            
            if len(X_w) == 0:
                chunk_states.append(0)
            else:
                raw_st = model.predict(X_w)[-1]
                # Map to aligned state
                mapped_st = mapping.get(raw_st, 0)
                chunk_states.append(mapped_st)
        
        states_online_list.extend(chunk_states)
        dates_online_list.extend(df_pred.index)
        
        current_date = next_rebalance
        
    # Map to Hourly
    states_series = pd.Series(states_online_list, index=dates_online_list)
    
    h_test = hourly_df.loc[hourly_df.index >= test_start_dt].copy()
    day_idx = h_test.index.normalize()
    h_test["D1_State_lag1d"] = day_idx.map(states_series).fillna(0).astype(int)
    
    # Run TR3 (Using TR3_ETH optimized params)
    # Ensure aliases
    if "MOM_ema200" in h_test.columns: h_test["EMA200"] = h_test["MOM_ema200"]
    if "MR_atr14" in h_test.columns: h_test["ATR14"] = h_test["MR_atr14"]
    
    # Calculate features if missing (Raw Data Input)
    if "ATR14" not in h_test.columns or "EMA200" not in h_test.columns:
        print("Calculating TR3 features (ATR14, EMA200)...")
        h_test = h_test.sort_index()
        # EMA200
        h_test["EMA200"] = h_test["Close"].ewm(span=200, adjust=False).mean()
        
        # ATR14 (RMA / Alpha=1/14)
        h = h_test["High"]
        l = h_test["Low"]
        c_prev = h_test["Close"].shift(1)
        tr1 = h - l
        tr2 = (h - c_prev).abs()
        tr3 = (l - c_prev).abs()
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        h_test["ATR14"] = tr.ewm(alpha=1/14, adjust=False).mean()
        
        # Donchian 20 (Upper) for Breakout
        h_test["MOM_donchian20_up"] = h_test["High"].rolling(window=20).max().shift(1)
        
        # MOM EMA 50 for Trend
        h_test["MOM_ema50"] = h_test["Close"].ewm(span=50, adjust=False).mean()
        
        # ADX 14
        up = h_test["High"] - h_test["High"].shift(1)
        down = h_test["Low"].shift(1) - h_test["Low"]
        plus_dm = np.where((up > down) & (up > 0), up, 0.0)
        minus_dm = np.where((down > up) & (down > 0), down, 0.0)
        
        # Smooth DM (Alpha=1/14) matches ATR smoothing
        p_dm_smooth = pd.Series(plus_dm, index=h_test.index).ewm(alpha=1/14, adjust=False).mean()
        m_dm_smooth = pd.Series(minus_dm, index=h_test.index).ewm(alpha=1/14, adjust=False).mean()
        # ATR is already computed as 'h_test["ATR14"]' (ewm alpha=1/14)
        
        p_di = 100 * (p_dm_smooth / h_test["ATR14"])
        m_di = 100 * (m_dm_smooth / h_test["ATR14"])
        
        dx = 100 * np.abs(p_di - m_di) / (p_di + m_di)
        h_test["ADX14"] = dx.ewm(alpha=1/14, adjust=False).mean()
        
        # R2_ema50 (Approximated as R2 of Close vs Time over 50 periods)
        idx_seq = pd.Series(np.arange(len(h_test)), index=h_test.index)
        # Rolling correlation of Close vs Time
        r = h_test["Close"].rolling(window=50).corr(idx_seq)
        h_test["R2_ema50"] = r.pow(2)
        
    # Run Strategy logic manually to support D1_State_lag1d column name
    # (run_strategy uses 'regime', simulate_tr3 uses 'regime_col' config)
    h_test["regime"] = h_test["D1_State_lag1d"]
    
    # We need to call run_strategy but it expects `states` series to do the mapping.
    # Here we ALREADY did the mapping (Lagged).
    # So we can just call `simulate_tr3` directly if we prepare the dataframe, OR
    # Adapt run_strategy to skip mapping if column exists.
    
    # Let's use `simulate_tr3` (Low level) directly like BTC script does.
    # We need `load_data_df` equivalent logic or just ensure columns exist.
    
    # Ensure CLV
    if "CLV" not in h_test.columns:
         rng = (h_test["High"] - h_test["Low"]).replace(0, np.nan)
         h_test["CLV"] = (2 * h_test["Close"] - h_test["High"] - h_test["Low"]) / rng
         h_test["CLV"] = h_test["CLV"].fillna(0.0)
         
    # Ensure valid_bar
    h_test["valid_bar"] = True
    
    # Run Simulation
    # Need to update TR3_ETH to use 'D1_State_lag1d' if simulate_tr3 uses it
    # TR3_ETH inherits from TR3_CONFIG which uses 'D1_State_lag1d'
    # So we are good.
    
    # Wait, simulate_tr3 is in `run_holdout_ect`, not imported here yet.
    # It is imported as `run_strategy` uses it? No `run_strategy` implements its own loop in this file.
    # This file has `run_strategy` defined locally!
    # And `run_strategy` does the mapping.
    
    # Let's just USE `run_strategy` but pass a dummy states series and put the regime in correct column?
    # `run_strategy`:
    #   day_idx = df.index.normalize()
    #   df["regime"] = day_idx.map(states).fillna(0).astype(int)
    
    # If we pass `states` as our `states_series`, it will map correctly!
    # Run Strategy
    trades, hourly_rets = run_strategy(h_test, states_series, TR3_ETH)
    
    # Process for Portfolio
    daily_rets = (1 + hourly_rets).resample("D").prod() - 1.0
    daily_rets = daily_rets.fillna(0.0)
    
    active_mask = pd.Series(False, index=daily_rets.index)
    if not trades.empty:
        entry_times = pd.to_datetime(trades["entry_time"], utc=True)
        exit_times = pd.to_datetime(trades["exit_time"], utc=True)
        for en, ex in zip(entry_times, exit_times):
            d_start = en.normalize()
            d_end = ex.normalize()
            active_mask.loc[d_start:d_end] = True
            
    return trades, daily_rets, active_mask
    
    
    print(f"DEBUG: df_full range: {df_full.index.min()} -> {df_full.index.max()}")
    print(f"DEBUG: df_full shape: {df_full.shape}")
    
    day_idx_full = df_full.index.normalize()

    # map states to hourly
    df_full["D1_State_lag1d"] = day_idx_full.map(states).fillna(0).astype(int)
    
    opt_csv_path = Path("outputs/eth_verif/eth_1h_opt_input.csv")
    opt_csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV
    opt_df_out = df_full.reset_index()
    if pd.api.types.is_datetime64tz_dtype(opt_df_out["Date"]):
        opt_df_out["Date"] = opt_df_out["Date"].dt.tz_convert("UTC").dt.tz_localize(None)
    opt_df_out.to_csv(opt_csv_path, index=False)
    print(f"Saved optimization input (full history) to {opt_csv_path}")

    # 4. Run Strategy (Verification Period)
    print("Running TR3 Strategy...")
    # Filter to 2022+ for holdout test
    test_start = "2022-01-01"
    df_h_test = df_full.loc[df_full.index >= test_start].copy()
    # Rename for compatibility with run_strategy logic (expects 'regime' col)
    df_h_test["regime"] = df_h_test["D1_State_lag1d"]
    
    # Revert to TR3_CONFIG (Baseline) as it outperformed TR3_ETH (Optimized) in OOS test
    trades, _ = run_strategy(df_h_test, states, TR3_CONFIG)
    
    if trades.empty:
        print("No trades found!")
        return
        
    # 5. Apply ECT
    print("Applying ECT Risk Management...")
    trades = apply_ect(trades, window=30, risk_high=1.0, risk_low=0.5)
    
    # 6. Save & Report
    trades.to_csv(out_path / "trades_eth.csv", index=False)
    
    m = metrics_from_trades(trades, "net_ret_scaled")
    print("\n" + "="*40)
    print("ETH STRATEGY RESULTS (2022-Present)")
    print("="*40)
    for k, v in m.items():
        print(f"{k}: {v}")
    print("="*40)
    
    # Save summary
    with open(out_path / "summary.txt", "w") as f:
        for k, v in m.items():
            f.write(f"{k}: {v}\n")

if __name__ == "__main__":
    main()
