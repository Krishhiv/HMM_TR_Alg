#!/usr/bin/env python3
"""
HMM-TR3 Portfolio Runner (BTC + ETH)
Runs both strategies in Walk-Forward mode and aggregates results.
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add project root
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.run_btc_strategy import run_btc_walkforward
from scripts.run_eth_strategy import run_eth_walkforward
from scripts.run_holdout_ect import apply_ect, metrics_from_trades

def load_data(asset: str, daily_path: Path, hourly_path: Path):
    d = pd.read_csv(daily_path)
    if "time" in d.columns: d = d.rename(columns={"time": "Date"})
    d["Date"] = pd.to_datetime(d["Date"], utc=True)
    d = d.set_index("Date").sort_index()

    h = pd.read_csv(hourly_path)
    if "time" in h.columns: h = h.rename(columns={"time": "Date"})
    h["Date"] = pd.to_datetime(h["Date"], utc=True)
    h = h.set_index("Date").sort_index()
    
    return d, h

def apply_risk_scaling(daily_rets: pd.Series, trades: pd.DataFrame, default_risk: float = 1.0) -> pd.Series:
    """Scale daily returns based on ECT risk factors from trades."""
    scaled_rets = daily_rets.copy()
    
    # Create a Series of risk factors aligned with daily_rets
    risk_map = pd.Series(default_risk, index=daily_rets.index)
    
    if not trades.empty and "risk_factor" in trades.columns:
        entry_times = pd.to_datetime(trades["entry_time"], utc=True)
        exit_times = pd.to_datetime(trades["exit_time"], utc=True)
        risks = trades["risk_factor"].values
        
        for en, ex, r in zip(entry_times, exit_times, risks):
            d_start = en.normalize()
            # If exit is same day, cover that day. If later, cover range.
            # daily_rets index is normalized days.
            d_end = ex.normalize()
            risk_map.loc[d_start:d_end] = r
            
    return scaled_rets * risk_map



def calc_metrics(daily_rets):
    cum_equity = (1 + daily_rets).cumprod()
    total_ret = cum_equity.iloc[-1] - 1
    years = (daily_rets.index[-1] - daily_rets.index[0]).days / 365.25
    cagr = (1 + total_ret) ** (1 / years) - 1 if years > 0 else 0
    
    sharpe = (daily_rets.mean() / daily_rets.std()) * np.sqrt(365) if daily_rets.std() > 0 else 0
    
    rolling_max = cum_equity.cummax()
    dd = (cum_equity - rolling_max) / rolling_max
    max_dd = dd.min()
    
    return {
        "TotalReturn": total_ret,
        "CAGR": cagr,
        "MaxDrawdown": max_dd,
        "Sharpe": sharpe
    }

def print_metrics(metrics: dict, title: str):
    print(f"\n{title}")
    print("-" * 30)
    pct_keys = ["TotalReturn", "CAGR", "MaxDrawdown", "WinRate", "AnnualVolatility", "MaxDD"]
    for k, v in metrics.items():
        if k in pct_keys:
            print(f"{k:<20}: {v:.2%}")
        elif isinstance(v, (int, float)):
            if k == "Trades":
                print(f"{k:<20}: {v}")
            else:
                print(f"{k:<20}: {v:.2f}")
        else:
            print(f"{k:<20}: {v}")
    print("-" * 30)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="outputs/portfolio_walkforward")
    args = parser.parse_args()
    
    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # 1. Load Data
    print("Loading Data...")
    btc_d, btc_h = load_data("BTC", 
                             PROJECT_ROOT / "data/processed/btc_1d_features.csv", 
                             PROJECT_ROOT / "data/processed/btc_1h_features_tr.csv")
    
    eth_d, eth_h = load_data("ETH", 
                             PROJECT_ROOT / "data/raw/eth_usd_1d_coinbase.csv", 
                             PROJECT_ROOT / "data/raw/eth_usd_1h_coinbase.csv")

    # 2. Run BTC Strategy
    print("\n" + "="*40)
    print("RUNNING BTC STRATEGY (Walk-Forward)")
    print("="*40)
    # Returns raw trades (risk=1), raw daily rets (risk=1), and active mask
    btc_trades, btc_daily_raw, btc_active = run_btc_walkforward(btc_d, btc_h, train_end="2021-12-31")
    
    if not btc_trades.empty:
        # Apply ECT (Risk Management)
        # OPTIMIZATION: Boost BTC Bullish Risk to 1.3x
        btc_trades = apply_ect(btc_trades, window=40, risk_high=1.3, risk_low=0.5)
        btc_trades.to_csv(out_path / "trades_btc.csv", index=False)
        
        # Apply Risk Scaling to Daily Returns
        r_btc = apply_risk_scaling(btc_daily_raw, btc_trades)
        
        m_btc = metrics_from_trades(btc_trades, "net_ret_scaled")
        print_metrics(m_btc, "BTC Results (2022+):")
    else:
        print("BTC: No trades found.")
        r_btc = pd.Series(0.0, index=btc_daily_raw.index)
        # Ensure active mask aligns even if empty
        btc_active = pd.Series(False, index=btc_daily_raw.index)

    # 3. Run ETH Strategy
    print("\n" + "="*40)
    print("RUNNING ETH STRATEGY (Walk-Forward)")
    print("="*40)
    # Unpack tuple
    eth_trades, eth_daily_raw, eth_active = run_eth_walkforward(eth_d, eth_h, train_end="2021-12-31")
    
    if not eth_trades.empty:
        # Apply ECT
        eth_trades = apply_ect(eth_trades, window=30, risk_high=1.0, risk_low=0.5)
        eth_trades.to_csv(out_path / "trades_eth.csv", index=False)
        
        # Apply Risk Scaling
        r_eth = apply_risk_scaling(eth_daily_raw, eth_trades)
        
        m_eth = metrics_from_trades(eth_trades, "net_ret_scaled")
        print_metrics(m_eth, "ETH Results (2022+):")
    else:
        print("ETH: No trades found.")
        r_eth = pd.Series(0.0, index=eth_daily_raw.index)
        eth_active = pd.Series(False, index=eth_daily_raw.index)

    # 4. Construct Portfolio (Dynamic Allocation)
    print("\n" + "="*40)
    print("CONSTRUCTING PORTFOLIO (Dynamic Capital Efficiency)")
    print("="*40)
    
    start_date = "2022-01-01"
    end_date = "2025-12-31" 
    
    # Common Index
    idx = pd.date_range(start_date, end_date, freq="D", tz="UTC")
    
    # Realign Series to common index
    r_btc = r_btc.reindex(idx, fill_value=0.0)
    r_eth = r_eth.reindex(idx, fill_value=0.0)
    is_btc = btc_active.reindex(idx, fill_value=False)
    is_eth = eth_active.reindex(idx, fill_value=False)
    
    # Dynamic Weights Vector
    w_btc = pd.Series(0.0, index=idx)
    w_eth = pd.Series(0.0, index=idx)
    
    # Logic:
    # 1. BTC Active, ETH Idle -> BTC 100%
    # 2. ETH Active, BTC Idle -> ETH 100%
    # 3. Both Active -> 70% BTC / 30% ETH (OPTIMIZATION)
    # 4. Neither -> Cash
    
    both = is_btc & is_eth
    only_btc = is_btc & (~is_eth)
    only_eth = is_eth & (~is_btc)
    
    w_btc[both] = 0.70
    w_eth[both] = 0.30
    
    w_btc[only_btc] = 1.0
    w_eth[only_eth] = 1.0
    
    # Portfolio Return
    r_port = (r_btc * w_btc) + (r_eth * w_eth)
    
    m_port = calc_metrics(r_port)
    print_metrics(m_port, "PORTFOLIO RESULTS:")
    
    # Save Curves
    curves = pd.DataFrame({
        "BTC_Equity": (1 + r_btc).cumprod(),
        "ETH_Equity": (1 + r_eth).cumprod(),
        "Portfolio_Equity": (1 + r_port).cumprod(),
        "W_BTC": w_btc,
        "W_ETH": w_eth
    })
    curves.to_csv(out_path / "equity_curves.csv")
    
    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(curves.index, curves["BTC_Equity"], label=f"BTC (CAGR {calc_metrics(r_btc)['CAGR']:.1%})", alpha=0.6)
    plt.plot(curves.index, curves["ETH_Equity"], label=f"ETH (CAGR {calc_metrics(r_eth)['CAGR']:.1%})", alpha=0.6)
    plt.plot(curves.index, curves["Portfolio_Equity"], label=f"Portfolio (CAGR {m_port['CAGR']:.1%})", linewidth=2.5, color="black")
    plt.title("HMM-TR3 Portfolio: Dynamic Capital Allocation")
    plt.yscale("log")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig(out_path / "portfolio_chart.png")
    print(f"Saved chart to {out_path / 'portfolio_chart.png'}")

if __name__ == "__main__":
    main()

