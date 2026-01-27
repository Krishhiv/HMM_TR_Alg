"""
TR³ (Thrust–Retention–Ride) Trading Strategy Engine.

A momentum strategy that trades long during HMM State 1 (trending regime).
Uses Donchian breakouts, ATR thrust moves, and multi-tiered exit logic.
"""

from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import pandas as pd


@dataclass
class TR3Config:
    """Configuration for TR³ strategy."""
    
    # Regime filter
    regime_col: str = "D1_State_lag1d"
    allowed_regime: int = 1
    
    # Entry conditions
    donchian_period: int = 20
    adx_min: float = 14
    r2_min: float = 0.10
    clv_min: float = 0.55
    thrust_atr_mult: float = 0.75
    ema_fast: int = 50
    ema_slow: int = 200
    
    # Exit: Fail-to-hold
    clv_fail_max: float = 0.35
    fail_level_atr: float = 0.25
    fth_disable_after_atr: float = 0.5
    
    # Exit: Breakeven
    be_activate_atr: float = 0.75
    be_cushion_atr: float = -0.02
    be_disable_after_atr: float = 1.0
    be_one_bar_delay: bool = True
    
    # Exit: Trailing stop
    trail_atr_n: int = 14
    trail_mult_base: float = 2.5
    trail_mult_1: float = 3.5  # After +1 ATR
    trail_mult_2: float = 4.5  # After +2 ATR
    
    # Exit: EMA break
    ema_break_relax_after_atr: float = 1.0
    ema_break_cushion_atr: float = 0.25
    
    # Exit: Time-based
    no_progress_hours: int = 12
    no_progress_atr: float = 0.50
    time_stop_hours: int = 24 * 7
    
    # Risk management
    fee_bps: float = 0.0
    max_loss_cap: float = 0.08
    leverage: float = 1.0


def ema(series: pd.Series, span: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=span, adjust=False).mean()


def calc_atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    """Average True Range."""
    hl = df["High"] - df["Low"]
    hc = (df["High"] - df["Close"].shift(1)).abs()
    lc = (df["Low"] - df["Close"].shift(1)).abs()
    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=n).mean()


def prepare_data(df: pd.DataFrame, config: TR3Config) -> pd.DataFrame:
    """
    Prepare data for TR³ simulation.
    
    Adds required columns if missing and validates data quality.
    """
    df = df.copy()
    df = df.sort_values("Date").reset_index(drop=True)
    
    # Validate required columns
    required = [
        "Date", "Open", "High", "Low", "Close",
        "MOM_donchian20_up", "MOM_ema50",
        "ADX14", "R2_ema50", "MR_rsi14",
        config.regime_col,
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Add helper columns if not present
    if "EMA200" not in df.columns:
        df["EMA200"] = ema(df["Close"], config.ema_slow)
    if "ATR14" not in df.columns:
        df["ATR14"] = calc_atr(df, config.trail_atr_n)
    
    # Close Location Value
    rng = (df["High"] - df["Low"]).replace(0, np.nan)
    df["CLV"] = ((df["Close"] - df["Low"]) / rng).fillna(0.5)
    
    # Open-to-open returns with spike filtering
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
    
    # Clean regime column
    df[config.regime_col] = df[config.regime_col].ffill().fillna(1).astype(int)
    
    return df


def simulate_tr3(
    df: pd.DataFrame,
    config: Optional[TR3Config] = None,
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Run TR³ backtest simulation.
    
    Entry: t-1 signals, execute at t open
    Exit: Multiple tiered exits based on trade progress
    
    Args:
        df: Prepared DataFrame with features
        config: Strategy configuration
    
    Returns:
        (trade_log, strategy_returns)
    """
    config = config or TR3Config()
    R = config
    regcol = R.regime_col
    
    # Entry conditions
    thrust = (df["Close"] - df["Close"].shift(1)) >= (R.thrust_atr_mult * df["ATR14"])
    breakout = df["Close"] > df["MOM_donchian20_up"]
    
    cond_now = (
        df["valid_bar"] &
        (df[regcol] == R.allowed_regime) &
        (df["MOM_ema50"] > df["EMA200"]) &
        (df["Close"] > df["MOM_ema50"]) &
        (breakout | thrust) &
        (df["CLV"] >= R.clv_min) &
        (df["ADX14"] >= R.adx_min) &
        (df["R2_ema50"] >= R.r2_min)
    )
    entry_sig = cond_now.shift(1).fillna(False).astype(bool)
    
    # State variables
    in_pos = False
    trades = []
    pos = np.zeros(len(df), dtype=float)
    fee = R.fee_bps / 10000.0
    
    entry_price = entry_time = entry_bar_high = None
    high_since_entry = entry_reg = be_armed_since = None
    
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
            
            # Skip invalid bars
            if not bool(df["valid_bar"].iat[j]):
                pos[i] = 1.0
                continue
            
            # Update running stats
            hh = df["High"].iat[j]
            if pd.notna(hh):
                high_since_entry = max(high_since_entry, hh)
            
            close_j = df["Close"].iat[j]
            ema50_j = df["MOM_ema50"].iat[j]
            atr_j = df["ATR14"].iat[j] if pd.notna(df["ATR14"].iat[j]) else None
            clv_j = df["CLV"].iat[j]
            
            # Progress in ATR terms
            advance_atr = (
                (high_since_entry - entry_price) / atr_j
                if (atr_j is not None and atr_j > 0)
                else 0.0
            )
            
            exit_now, reason = False, "rule"
            
            # === EXIT LOGIC ===
            
            # 1. Fail-to-hold (early exit protection)
            use_fth = advance_atr < R.fth_disable_after_atr
            if use_fth:
                if clv_j <= R.clv_fail_max:
                    exit_now, reason = True, "fth_clv"
                elif (atr_j is not None) and (close_j < (entry_bar_high - R.fail_level_atr * atr_j)):
                    exit_now, reason = True, "fth_level"
            
            # 2. Breakeven (protect capital after initial advance)
            can_arm_be = (
                (atr_j is not None) and
                (advance_atr >= R.be_activate_atr) and
                (advance_atr < R.be_disable_after_atr)
            )
            if (be_armed_since is None) and can_arm_be:
                be_armed_since = df["Date"].iat[j]
            
            if advance_atr >= R.be_disable_after_atr:
                be_armed_since = None
            
            be_active = False
            if be_armed_since is not None:
                if R.be_one_bar_delay:
                    be_active = (df["Date"].iat[j] - be_armed_since) >= pd.Timedelta(hours=1)
                else:
                    be_active = True
            
            if (not exit_now) and be_active and (atr_j is not None):
                be_level = entry_price - R.be_cushion_atr * atr_j
                if close_j < be_level:
                    exit_now, reason = True, "breakeven"
            
            # 3. Ratcheting trailing stop
            if (not exit_now) and (atr_j is not None):
                if advance_atr >= 2.0:
                    trail_mult = R.trail_mult_2
                elif advance_atr >= 1.0:
                    trail_mult = R.trail_mult_1
                else:
                    trail_mult = R.trail_mult_base
                
                trail = high_since_entry - trail_mult * atr_j
                if close_j < trail:
                    exit_now, reason = True, "trail_atr"
            
            # 4. EMA50 break (relaxed when in profit)
            if not exit_now:
                if (advance_atr >= R.ema_break_relax_after_atr) and (atr_j is not None):
                    if close_j < (ema50_j - R.ema_break_cushion_atr * atr_j):
                        exit_now, reason = True, "ema50_relaxed"
                else:
                    if close_j < ema50_j:
                        exit_now, reason = True, "ema50_break"
            
            # 5. No-progress stop
            if (not exit_now):
                hold_time = df["Date"].iat[j] - entry_time
                if hold_time >= pd.Timedelta(hours=R.no_progress_hours):
                    if (atr_j is None) or ((high_since_entry - entry_price) < (R.no_progress_atr * atr_j)):
                        exit_now, reason = True, "no_progress"
            
            # 6. Time stop
            if (not exit_now):
                hold_time = df["Date"].iat[j] - entry_time
                if hold_time >= pd.Timedelta(hours=R.time_stop_hours):
                    exit_now, reason = True, "time_stop"
            
            # Execute exit
            if exit_now:
                exit_time = df["Date"].iat[i]
                exit_price = df["Open"].iat[i]
                gross_ret = (exit_price / entry_price) - 1.0
                
                if fee > 0:
                    net_ret = ((exit_price * (1 - fee)) / (entry_price * (1 + fee))) - 1.0
                else:
                    net_ret = gross_ret
                
                net_ret *= R.leverage
                net_ret = max(net_ret, -R.max_loss_cap)
                
                trades.append({
                    "entry_time": entry_time,
                    "entry_price": entry_price,
                    "exit_time": exit_time,
                    "exit_price": exit_price,
                    "gross_ret": gross_ret,
                    "net_ret": net_ret,
                    "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
                    "regime": entry_reg,
                    "strategy": "TR3",
                    "exit_reason": reason,
                })
                
                in_pos = False
                entry_price = entry_time = entry_bar_high = None
                high_since_entry = entry_reg = be_armed_since = None
        
        pos[i] = 1.0 if in_pos else 0.0
    
    # Close any open position at end
    if in_pos:
        i = len(df) - 1
        exit_time = df["Date"].iat[i]
        exit_price = df["Open"].iat[i]
        gross_ret = (exit_price / entry_price) - 1.0
        net_ret = gross_ret * R.leverage
        net_ret = max(net_ret, -R.max_loss_cap)
        
        trades.append({
            "entry_time": entry_time,
            "entry_price": entry_price,
            "exit_time": exit_time,
            "exit_price": exit_price,
            "gross_ret": gross_ret,
            "net_ret": net_ret,
            "holding_hours": (exit_time - entry_time) / pd.Timedelta(hours=1),
            "regime": entry_reg,
            "strategy": "TR3",
            "exit_reason": "eod_close",
        })
    
    trade_log = pd.DataFrame(trades, columns=cols)
    strat_rets = pd.Series(pos, index=df.index) * df["ret_oo"]
    
    return trade_log, strat_rets


def run_backtest(
    hourly_csv: str,
    config: Optional[TR3Config] = None,
    out_csv: Optional[str] = None,
) -> tuple[pd.DataFrame, dict]:
    """
    Run full TR³ backtest on hourly data.
    
    Args:
        hourly_csv: Path to hourly features CSV
        config: Strategy configuration
        out_csv: Optional path to save trade log
    
    Returns:
        (trade_log, metrics)
    """
    from .metrics import compute_metrics  # Avoid circular import
    
    config = config or TR3Config()
    
    df = pd.read_csv(hourly_csv, parse_dates=["Date"])
    df = prepare_data(df, config)
    
    trade_log, _ = simulate_tr3(df, config)
    
    if out_csv:
        trade_log.to_csv(out_csv, index=False)
        print(f"Saved trade log: {out_csv}")
    
    metrics = compute_metrics(df, trade_log)
    
    return trade_log, metrics
