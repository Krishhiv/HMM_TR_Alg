"""
Backtest performance metrics.

Computes CAGR, Sharpe, Profit Factor, Win Rate, and other trading metrics.
"""

from math import sqrt
from typing import Optional

import numpy as np
import pandas as pd


def compute_metrics(
    df: pd.DataFrame,
    trade_log: pd.DataFrame,
    ret_col: str = "net_ret",
) -> dict:
    """
    Compute comprehensive backtest metrics.
    
    Args:
        df: DataFrame with 'Date' column
        trade_log: Trade log DataFrame
        ret_col: Column to use for returns ('net_ret' or 'gross_ret')
    
    Returns:
        Dictionary of metrics
    """
    dates = df["Date"]
    r = pd.Series(0.0, index=dates)
    
    # Handle empty trade log
    if trade_log is None or len(trade_log) == 0:
        equity = (1.0 + r).cumprod()
        years = (dates.iloc[-1] - dates.iloc[0]) / pd.Timedelta(days=365.25)
        cagr = equity.iloc[-1] ** (1 / years) - 1 if years > 0 else float("nan")
        mu, sd = r.mean(), r.std(ddof=0)
        sharpe = (mu / sd) * sqrt(24 * 365.25) if sd > 0 else float("nan")
        
        return {
            "CAGR": cagr,
            "Sharpe": sharpe,
            "ProfitFactor": float("nan"),
            "WinRate": float("nan"),
            "FinalEquity": equity.iloc[-1],
            "NumTrades": 0,
            "MaxDrawdown": 0.0,
        }
    
    # Map trades to hourly grid
    idx = pd.Index(dates)
    entry_idx = idx.get_indexer(pd.to_datetime(trade_log["entry_time"]))
    exit_idx = idx.get_indexer(pd.to_datetime(trade_log["exit_time"]))
    
    Hs = trade_log["holding_hours"].to_numpy()
    
    if ret_col not in trade_log.columns:
        ret_col = "gross_ret"
    rets = trade_log[ret_col].astype(float).to_numpy()
    
    # Spread returns evenly across holding period
    for e, x, H, R in zip(entry_idx, exit_idx, Hs, rets):
        H_int = int(round(H))
        if e < 0 or x < 0 or H_int <= 0:
            if x >= 0:
                r.iloc[x] += R
            continue
        rh = (1.0 + R) ** (1.0 / H_int) - 1.0
        end = min(e + H_int, len(r))
        r.iloc[e:end] += rh
    
    # Equity curve
    equity = (1.0 + r).cumprod()
    
    # CAGR
    years = (dates.iloc[-1] - dates.iloc[0]) / pd.Timedelta(days=365.25)
    cagr = equity.iloc[-1] ** (1 / years) - 1 if years > 0 else float("nan")
    
    # Sharpe (hourly, annualized)
    mu, sd = r.mean(), r.std(ddof=0)
    sharpe = (mu / sd) * sqrt(24 * 365.25) if sd > 0 else float("nan")
    
    # Trade-level stats
    ret_series = trade_log[ret_col].astype(float)
    gross_profit = ret_series[ret_series > 0].sum()
    gross_loss = -ret_series[ret_series < 0].sum()
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float("nan")
    win_rate = (ret_series > 0).mean()
    
    # Max drawdown
    running_max = equity.cummax()
    drawdown = (equity - running_max) / running_max
    max_dd = drawdown.min()
    
    # Daily Sharpe
    exit_times = pd.to_datetime(trade_log["exit_time"], errors="coerce")
    daily_rets = pd.Series(ret_series.values, index=exit_times).resample("D").sum().fillna(0.0)
    daily_mu = daily_rets.mean()
    daily_sd = daily_rets.std(ddof=0)
    daily_sharpe = (daily_mu / daily_sd) * sqrt(365) if daily_sd > 0 else float("nan")
    
    # Breakeven-adjusted metrics
    EPS_BE = 0.001
    if "exit_reason" in trade_log.columns:
        is_be = trade_log["exit_reason"].astype(str).eq("breakeven")
    else:
        is_be = pd.Series(False, index=trade_log.index)
    
    win_rate_ge0 = (ret_series >= 0).mean()
    win_rate_be_adj = ((ret_series > 0) | (is_be & (ret_series > -EPS_BE))).mean()
    
    # Average trade stats
    avg_win = ret_series[ret_series > 0].mean() if (ret_series > 0).any() else 0
    avg_loss = ret_series[ret_series < 0].mean() if (ret_series < 0).any() else 0
    avg_hold_hours = trade_log["holding_hours"].mean()
    
    return {
        "CAGR": cagr,
        "Sharpe": sharpe,
        "Sharpe_Daily": daily_sharpe,
        "ProfitFactor": profit_factor,
        "WinRate": win_rate,
        "WinRate_GE0": win_rate_ge0,
        "WinRate_BEAdj": win_rate_be_adj,
        "FinalEquity": equity.iloc[-1],
        "NumTrades": len(trade_log),
        "MaxDrawdown": max_dd,
        "AvgWin": avg_win,
        "AvgLoss": avg_loss,
        "AvgHoldHours": avg_hold_hours,
        "BreakevenCount": int(is_be.sum()),
    }


def compute_equity_curve(
    df: pd.DataFrame,
    trade_log: pd.DataFrame,
    ret_col: str = "net_ret",
) -> pd.Series:
    """
    Reconstruct hourly equity curve from trades.
    """
    dates = df["Date"]
    r = pd.Series(0.0, index=dates)
    
    if trade_log is None or len(trade_log) == 0:
        return (1.0 + r).cumprod()
    
    idx = pd.Index(dates)
    entry_idx = idx.get_indexer(pd.to_datetime(trade_log["entry_time"]))
    exit_idx = idx.get_indexer(pd.to_datetime(trade_log["exit_time"]))
    
    Hs = trade_log["holding_hours"].to_numpy()
    
    if ret_col not in trade_log.columns:
        ret_col = "gross_ret"
    rets = trade_log[ret_col].astype(float).to_numpy()
    
    for e, x, H, R in zip(entry_idx, exit_idx, Hs, rets):
        H_int = int(round(H))
        if e < 0 or x < 0 or H_int <= 0:
            if x >= 0:
                r.iloc[x] += R
            continue
        rh = (1.0 + R) ** (1.0 / H_int) - 1.0
        end = min(e + H_int, len(r))
        r.iloc[e:end] += rh
    
    return (1.0 + r).cumprod()


def print_summary(metrics: dict) -> None:
    """Print a formatted metrics summary."""
    print("\n" + "=" * 50)
    print("BACKTEST SUMMARY")
    print("=" * 50)
    
    print(f"Trades:        {metrics.get('NumTrades', 0)}")
    print(f"Final Equity:  {metrics.get('FinalEquity', 1.0):.4f}")
    print(f"CAGR:          {metrics.get('CAGR', 0):.2%}")
    print(f"Sharpe:        {metrics.get('Sharpe', 0):.2f}")
    print(f"Profit Factor: {metrics.get('ProfitFactor', 0):.2f}")
    print(f"Win Rate:      {metrics.get('WinRate', 0):.2%}")
    print(f"Max Drawdown:  {metrics.get('MaxDrawdown', 0):.2%}")
    print(f"Avg Win:       {metrics.get('AvgWin', 0):.2%}")
    print(f"Avg Loss:      {metrics.get('AvgLoss', 0):.2%}")
    print(f"Avg Hold:      {metrics.get('AvgHoldHours', 0):.1f}h")
    print("=" * 50)


def exit_analysis(trade_log: pd.DataFrame) -> pd.DataFrame:
    """Analyze exit reasons distribution."""
    if "exit_reason" not in trade_log.columns:
        return pd.DataFrame()
    
    grouped = trade_log.groupby("exit_reason").agg({
        "net_ret": ["count", "mean", "sum"],
        "holding_hours": "mean",
    })
    grouped.columns = ["Count", "AvgRet", "TotalRet", "AvgHoldHours"]
    grouped["Pct"] = grouped["Count"] / len(trade_log)
    
    return grouped.sort_values("Count", ascending=False)
