#!/usr/bin/env python3
"""
walkforward_mean_reversion_test.py

Walk-forward (online-style) evaluation for your BTC mean reversion strategy using ONLY
information available up to each decision point.

What it does
------------
- Trades sequentially bar-by-bar (no peeking).
- Optional walk-forward recalibration: every N days, re-selects parameters using the
  PREVIOUS train window only (grid search).
- Supports:
  - filtered vs unfiltered entries (Hurst + LiquidityCostProxy)
  - cooldown in bars
  - 1 position at a time (by design)
- Outputs:
  - trade log CSV
  - metrics TXT
  - equity curve PNG

Execution model (causal)
------------------------
- Signal is detected at bar i close using ZScore[i] and ZScore[i-1].
- Entry is executed at NEXT bar open (i+1 open).
- Exit conditions are evaluated at each subsequent bar close using ZScore.
- Exit is executed at NEXT bar open after the bar where exit condition triggers.

Costs
-----
- Uses LiquidityCostProxy (decimal) + fee_bps as one-way costs.
- Total round-trip cost = 2 * (fee + liquidity_cost_at_entry).
  (Simple and conservative; you can refine to use both entry & exit liquidity later.)

Notes
-----
- If you short, this assumes you can short (perps/margin). If not, disable shorts.
"""

from __future__ import annotations

import argparse
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Helpers
# -----------------------------
def parse_csv_list(s: str) -> List[float]:
    s = (s or "").strip()
    if not s:
        return []
    return [float(x.strip()) for x in s.split(",") if x.strip()]


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def to_dt_utc_naive(series: pd.Series) -> pd.Series:
    dt = pd.to_datetime(series, errors="coerce", utc=True)
    return dt.dt.tz_convert(None)


def safe_float(x) -> float:
    try:
        v = float(x)
        if math.isfinite(v):
            return v
        return float("nan")
    except Exception:
        return float("nan")


def max_drawdown(equity: np.ndarray) -> float:
    """Max drawdown as a positive fraction (e.g., 0.25 means -25%)."""
    peak = np.maximum.accumulate(equity)
    dd = 1.0 - (equity / peak)
    return float(np.nanmax(dd))


def annualized_sharpe(daily_returns: np.ndarray, periods_per_year: int = 365) -> float:
    daily_returns = daily_returns[np.isfinite(daily_returns)]
    if daily_returns.size < 2:
        return float("nan")
    mu = float(np.mean(daily_returns))
    sd = float(np.std(daily_returns, ddof=1))
    if sd <= 0:
        return float("nan")
    return (mu / sd) * math.sqrt(periods_per_year)


def annualized_sortino(daily_returns: np.ndarray, periods_per_year: int = 365) -> float:
    daily_returns = daily_returns[np.isfinite(daily_returns)]
    if daily_returns.size < 2:
        return float("nan")
    mu = float(np.mean(daily_returns))
    downside = daily_returns[daily_returns < 0]
    if downside.size < 2:
        return float("nan")
    dd = float(np.std(downside, ddof=1))
    if dd <= 0:
        return float("nan")
    return (mu / dd) * math.sqrt(periods_per_year)


# -----------------------------
# Trade model
# -----------------------------
@dataclass
class Params:
    z_entry: float
    z_target: float
    z_stop: float
    max_hold_bars: int


@dataclass
class Position:
    side: int  # +1 long, -1 short
    entry_idx_signal: int  # index where signal was detected (close)
    entry_idx_exec: int    # index where entry executed (open)
    entry_time: pd.Timestamp
    entry_price: float
    entry_z: float
    entry_hurst: float
    entry_liq: float
    equity_before: float
    params: Params


@dataclass
class Trade:
    entry_time: pd.Timestamp
    exit_time: pd.Timestamp
    side: str
    entry_price: float
    exit_price: float
    bars_held: int
    outcome: str  # TARGET/STOP/TIME
    gross_return: float
    net_return: float
    equity_before: float
    equity_after: float
    z_entry: float
    z_exit: float
    hurst_entry: float
    liq_entry: float
    z_entry_thr: float
    z_target_thr: float
    z_stop_thr: float
    max_hold_bars: int


# -----------------------------
# Core signal + exit logic (causal)
# -----------------------------
def is_entry_signal(z_prev: float, z_now: float, z_entry: float) -> int:
    """
    Returns:
    +1 for LONG signal, -1 for SHORT signal, 0 for none.
    Signal is "fresh crossing" of +/- z_entry.
    """
    if not (math.isfinite(z_prev) and math.isfinite(z_now)):
        return 0

    # LONG: cross below -z_entry
    if (z_now < -z_entry) and (z_prev >= -z_entry):
        return +1

    # SHORT: cross above +z_entry
    if (z_now > z_entry) and (z_prev <= z_entry):
        return -1

    return 0


def check_exit(side: int, z_now: float, p: Params) -> Optional[str]:
    """
    Exit triggers evaluated on bar close.
    Returns one of: "STOP", "TARGET", or None.
    """
    if not math.isfinite(z_now):
        return None

    if side == +1:
        # long target: z >= +z_target ; stop: z <= -z_stop
        if z_now <= -p.z_stop:
            return "STOP"
        if z_now >= p.z_target:
            return "TARGET"
        return None

    # side == -1
    # short target: z <= -z_target ; stop: z >= +z_stop
    if z_now >= p.z_stop:
        return "STOP"
    if z_now <= -p.z_target:
        return "TARGET"
    return None


# -----------------------------
# Walk-forward calibration (optional)
# -----------------------------
def simulate_segment_for_objective(
    open_: np.ndarray,
    close_: np.ndarray,
    z: np.ndarray,
    hurst: np.ndarray,
    liq: np.ndarray,
    t: np.ndarray,
    start_idx: int,
    end_idx: int,
    params: Params,
    use_filters: bool,
    hurst_max: float,
    liq_max: float,
    cooldown_bars: int,
    allow_short: bool,
    fee_bps: float,
) -> float:
    """
    Fast simulation used ONLY for parameter selection on a training window.
    Returns an objective value (default: Sharpe on daily returns inside the window).
    """
    equity = 100.0
    in_pos: Optional[Position] = None
    next_allowed = start_idx

    # equity series for objective
    eq = np.full(end_idx - start_idx, np.nan, dtype=float)
    eq[0] = equity

    fee = fee_bps / 1e4

    for i in range(start_idx, end_idx):
        # mark equity each bar (carry forward)
        if i > start_idx:
            eq[i - start_idx] = eq[i - start_idx - 1] if math.isfinite(eq[i - start_idx - 1]) else equity

        # exit (evaluate at close i, execute at open i+1)
        if in_pos is not None:
            held = i - in_pos.entry_idx_exec
            outcome = check_exit(in_pos.side, z[i], in_pos.params)
            time_exit = (held >= in_pos.params.max_hold_bars)
            if outcome is not None or time_exit:
                exec_idx = i + 1
                if exec_idx >= end_idx:  # can't execute beyond segment
                    break
                exit_price = open_[exec_idx]
                if not math.isfinite(exit_price) or exit_price <= 0:
                    break

                direction = in_pos.side
                gross = direction * (exit_price / in_pos.entry_price - 1.0)
                # cost uses entry liquidity (simple conservative)
                one_way = fee + max(in_pos.entry_liq, 0.0)
                net = gross - 2.0 * one_way

                equity = equity * (1.0 + net)
                in_pos = None
                next_allowed = exec_idx + max(0, cooldown_bars)
                eq[exec_idx - start_idx] = equity
                continue

        # entry (signal at close i, exec at open i+1)
        if in_pos is None and i >= max(start_idx + 1, next_allowed) and (i + 1) < end_idx:
            side_sig = is_entry_signal(z[i - 1], z[i], params.z_entry)
            if side_sig == -1 and not allow_short:
                side_sig = 0

            if side_sig != 0:
                # filters apply on signal bar i
                if use_filters:
                    hv = hurst[i]
                    lv = liq[i]
                    if (not math.isfinite(hv)) or (hv >= hurst_max):
                        side_sig = 0
                    elif (not math.isfinite(lv)) or (lv > liq_max):
                        side_sig = 0

                if side_sig != 0:
                    exec_idx = i + 1
                    entry_price = open_[exec_idx]
                    if math.isfinite(entry_price) and entry_price > 0:
                        in_pos = Position(
                            side=side_sig,
                            entry_idx_signal=i,
                            entry_idx_exec=exec_idx,
                            entry_time=t[exec_idx],
                            entry_price=entry_price,
                            entry_z=z[i],
                            entry_hurst=hurst[i],
                            entry_liq=liq[i],
                            equity_before=equity,
                            params=params,
                        )

    # build daily returns from eq series
    # (approx: use bar-index series -> convert to daily by sampling end-of-day)
    eq_series = pd.Series(eq, index=pd.to_datetime(t[start_idx:end_idx]))
    eq_series = eq_series.ffill().dropna()
    if eq_series.size < 10:
        return float("-inf")

    daily = eq_series.resample("1D").last().dropna()
    if daily.size < 5:
        return float("-inf")

    daily_ret = daily.pct_change().dropna().to_numpy(dtype=float)
    s = annualized_sharpe(daily_ret, periods_per_year=365)
    if not math.isfinite(s):
        return float("-inf")
    return float(s)


def calibrate_params_walkforward(
    open_: np.ndarray,
    close_: np.ndarray,
    z: np.ndarray,
    hurst: np.ndarray,
    liq: np.ndarray,
    t: np.ndarray,
    train_start_idx: int,
    train_end_idx: int,
    base_params: Params,
    z_entry_grid: List[float],
    z_stop_grid: List[float],
    z_target_grid: List[float],
    use_filters: bool,
    hurst_max: float,
    liq_max: float,
    cooldown_bars: int,
    allow_short: bool,
    fee_bps: float,
) -> Params:
    """
    Grid-search params on TRAIN window only.
    Returns best params by objective (Sharpe on daily returns inside train).
    """
    # Fallback if grids empty
    z_entry_grid = z_entry_grid or [base_params.z_entry]
    z_stop_grid = z_stop_grid or [base_params.z_stop]
    z_target_grid = z_target_grid or [base_params.z_target]

    best_score = float("-inf")
    best_params = base_params

    # Small guard: ensure train window has enough bars
    if (train_end_idx - train_start_idx) < 10_000:  # ~35 days of 5m bars
        # Still allow, but may be noisy
        pass

    for ze in z_entry_grid:
        for zs in z_stop_grid:
            for zt in z_target_grid:
                p = Params(z_entry=ze, z_target=zt, z_stop=zs, max_hold_bars=base_params.max_hold_bars)
                score = simulate_segment_for_objective(
                    open_=open_,
                    close_=close_,
                    z=z,
                    hurst=hurst,
                    liq=liq,
                    t=t,
                    start_idx=train_start_idx,
                    end_idx=train_end_idx,
                    params=p,
                    use_filters=use_filters,
                    hurst_max=hurst_max,
                    liq_max=liq_max,
                    cooldown_bars=cooldown_bars,
                    allow_short=allow_short,
                    fee_bps=fee_bps,
                )
                if score > best_score:
                    best_score = score
                    best_params = p

    return best_params


# -----------------------------
# Main walk-forward trading simulation (with logging + equity)
# -----------------------------
def run_walkforward(
    df: pd.DataFrame,
    out_dir: str,
    tag: str,
    base_params: Params,
    start_equity: float,
    use_filters: bool,
    hurst_max: float,
    liq_max: float,
    cooldown_bars: int,
    allow_short: bool,
    fee_bps: float,
    walkforward: bool,
    train_days: int,
    recalib_days: int,
    optimize: bool,
    z_entry_grid: List[float],
    z_stop_grid: List[float],
    z_target_grid: List[float],
) -> Tuple[pd.DataFrame, Dict[str, float], pd.Series]:
    """
    Returns:
      - trades dataframe
      - metrics dict
      - equity curve series (bar-level, forward-filled)
    """
    ensure_dir(out_dir)

    # Required columns
    required = ["Date", "Open", "Close", "ZScore", "FairValue", "EWMAVol"]
    for c in required:
        if c not in df.columns:
            raise ValueError(f"Missing required column: {c}")

    if use_filters:
        for c in ["Hurst15m", "LiquidityCostProxy"]:
            if c not in df.columns:
                raise ValueError(f"use_filters=True but missing column: {c}")

    # Sort & coerce
    d = df.copy()
    d["Date"] = to_dt_utc_naive(d["Date"])
    d = d.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    # Numeric arrays
    t = d["Date"].to_numpy()
    open_ = pd.to_numeric(d["Open"], errors="coerce").to_numpy(dtype=float)
    close_ = pd.to_numeric(d["Close"], errors="coerce").to_numpy(dtype=float)
    z = pd.to_numeric(d["ZScore"], errors="coerce").to_numpy(dtype=float)
    hurst = pd.to_numeric(d["Hurst15m"], errors="coerce").to_numpy(dtype=float) if "Hurst15m" in d.columns else np.full(len(d), np.nan)
    liq = pd.to_numeric(d["LiquidityCostProxy"], errors="coerce").to_numpy(dtype=float) if "LiquidityCostProxy" in d.columns else np.full(len(d), 0.0)

    n = len(d)

    # Walk-forward schedule
    # Start trading after we have a train window if walkforward enabled,
    # else start at bar 1 (since we need z[i-1]).
    if walkforward:
        start_time = pd.Timestamp(t[0]) + pd.Timedelta(days=train_days)
        start_idx = int(np.searchsorted(t, np.array(start_time, dtype="datetime64[ns]"), side="left"))
        next_recalib_time = pd.Timestamp(t[0]) + pd.Timedelta(days=train_days)
        next_recalib_idx = start_idx
    else:
        start_idx = 1
        next_recalib_time = None
        next_recalib_idx = None

    equity = float(start_equity)
    eq = np.full(n, np.nan, dtype=float)
    eq[:start_idx] = np.nan
    eq[start_idx] = equity

    in_pos: Optional[Position] = None
    next_allowed = start_idx

    current_params = base_params

    trades: List[Trade] = []
    fee = fee_bps / 1e4

    for i in range(start_idx, n):
        # carry equity forward on each bar (bar-level equity curve)
        if i > start_idx:
            eq[i] = eq[i - 1] if math.isfinite(eq[i - 1]) else equity

        # Walk-forward recalibration at the moment we "reach" the recalib point
        if walkforward and optimize and (i >= next_recalib_idx):
            # training window: [i - train_days, i)
            train_start_time = pd.Timestamp(t[i]) - pd.Timedelta(days=train_days)
            train_start_idx = int(np.searchsorted(t, np.array(train_start_time, dtype="datetime64[ns]"), side="left"))
            train_end_idx = i  # exclusive

            # Calibrate using past data only
            current_params = calibrate_params_walkforward(
                open_=open_,
                close_=close_,
                z=z,
                hurst=hurst,
                liq=liq,
                t=t,
                train_start_idx=train_start_idx,
                train_end_idx=train_end_idx,
                base_params=base_params,
                z_entry_grid=z_entry_grid,
                z_stop_grid=z_stop_grid,
                z_target_grid=z_target_grid,
                use_filters=use_filters,
                hurst_max=hurst_max,
                liq_max=liq_max,
                cooldown_bars=cooldown_bars,
                allow_short=allow_short,
                fee_bps=fee_bps,
            )

            # schedule next recalibration
            next_recalib_time = pd.Timestamp(t[i]) + pd.Timedelta(days=recalib_days)
            next_recalib_idx = int(np.searchsorted(t, np.array(next_recalib_time, dtype="datetime64[ns]"), side="left"))

        # EXIT: evaluate at close i, execute at open i+1
        if in_pos is not None:
            held = i - in_pos.entry_idx_exec
            outcome = check_exit(in_pos.side, z[i], in_pos.params)
            time_exit = (held >= in_pos.params.max_hold_bars)

            if (outcome is not None) or time_exit:
                exec_idx = i + 1
                if exec_idx >= n:
                    break
                exit_price = open_[exec_idx]
                if (not math.isfinite(exit_price)) or exit_price <= 0:
                    break

                direction = in_pos.side
                gross = direction * (exit_price / in_pos.entry_price - 1.0)

                # round-trip cost (fee + entry liquidity proxy)
                one_way = fee + max(in_pos.entry_liq, 0.0)
                net = gross - 2.0 * one_way

                eq_before = in_pos.equity_before
                equity = eq_before * (1.0 + net)

                exit_z = z[i]
                exit_time = pd.Timestamp(t[exec_idx])

                trades.append(
                    Trade(
                        entry_time=in_pos.entry_time,
                        exit_time=exit_time,
                        side="LONG" if in_pos.side == +1 else "SHORT",
                        entry_price=float(in_pos.entry_price),
                        exit_price=float(exit_price),
                        bars_held=int(exec_idx - in_pos.entry_idx_exec),
                        outcome=outcome if outcome is not None else "TIME",
                        gross_return=float(gross),
                        net_return=float(net),
                        equity_before=float(eq_before),
                        equity_after=float(equity),
                        z_entry=float(in_pos.entry_z),
                        z_exit=float(exit_z),
                        hurst_entry=float(in_pos.entry_hurst),
                        liq_entry=float(in_pos.entry_liq),
                        z_entry_thr=float(in_pos.params.z_entry),
                        z_target_thr=float(in_pos.params.z_target),
                        z_stop_thr=float(in_pos.params.z_stop),
                        max_hold_bars=int(in_pos.params.max_hold_bars),
                    )
                )

                in_pos = None
                eq[exec_idx] = equity
                next_allowed = exec_idx + max(0, cooldown_bars)
                continue

        # ENTRY: evaluate at close i, execute at open i+1
        if in_pos is None and i >= max(1, next_allowed) and (i + 1) < n:
            side_sig = is_entry_signal(z[i - 1], z[i], current_params.z_entry)
            if side_sig == -1 and not allow_short:
                side_sig = 0

            if side_sig != 0:
                # filters on signal bar i (using ONLY bar i features)
                if use_filters:
                    hv = hurst[i]
                    lv = liq[i]
                    if (not math.isfinite(hv)) or (hv >= hurst_max):
                        side_sig = 0
                    elif (not math.isfinite(lv)) or (lv > liq_max):
                        side_sig = 0

                if side_sig != 0:
                    exec_idx = i + 1
                    entry_price = open_[exec_idx]
                    if math.isfinite(entry_price) and entry_price > 0:
                        in_pos = Position(
                            side=side_sig,
                            entry_idx_signal=i,
                            entry_idx_exec=exec_idx,
                            entry_time=pd.Timestamp(t[exec_idx]),
                            entry_price=float(entry_price),
                            entry_z=float(z[i]),
                            entry_hurst=float(hurst[i]) if math.isfinite(hurst[i]) else float("nan"),
                            entry_liq=float(liq[i]) if math.isfinite(liq[i]) else 0.0,
                            equity_before=float(equity),
                            params=current_params,
                        )

    # Build equity curve series
    eq_series = pd.Series(eq, index=pd.to_datetime(t))
    eq_series = eq_series.ffill().dropna()

    # Trades DF
    trades_df = pd.DataFrame([trade.__dict__ for trade in trades])

    # Metrics
    start_time = eq_series.index.min()
    end_time = eq_series.index.max()
    duration_days = (end_time - start_time).total_seconds() / 86400.0
    years = duration_days / 365.25 if duration_days > 0 else float("nan")

    final_equity = float(eq_series.iloc[-1])
    net_return = final_equity / start_equity - 1.0
    cagr = (final_equity / start_equity) ** (1.0 / years) - 1.0 if math.isfinite(years) and years > 0 else float("nan")

    daily = eq_series.resample("1D").last().dropna()
    daily_ret = daily.pct_change().dropna().to_numpy(dtype=float)

    mdd = max_drawdown(eq_series.to_numpy(dtype=float))
    sharpe = annualized_sharpe(daily_ret, periods_per_year=365)
    sortino = annualized_sortino(daily_ret, periods_per_year=365)
    calmar = (cagr / mdd) if (math.isfinite(cagr) and mdd > 0) else float("nan")

    # Win rate: by net_return > 0 (trade-level), plus outcome-based
    win_rate_pnl = float((trades_df["net_return"] > 0).mean()) if len(trades_df) else float("nan")
    win_rate_target = float((trades_df["outcome"] == "TARGET").mean()) if len(trades_df) else float("nan")

    metrics = {
        "start_equity": float(start_equity),
        "final_equity": float(final_equity),
        "net_return": float(net_return),
        "CAGR": float(cagr) if math.isfinite(cagr) else float("nan"),
        "sharpe": float(sharpe) if math.isfinite(sharpe) else float("nan"),
        "sortino": float(sortino) if math.isfinite(sortino) else float("nan"),
        "calmar": float(calmar) if math.isfinite(calmar) else float("nan"),
        "max_drawdown": float(mdd),
        "trade_count": int(len(trades_df)),
        "win_rate_pnl": float(win_rate_pnl) if math.isfinite(win_rate_pnl) else float("nan"),
        "win_rate_target": float(win_rate_target) if math.isfinite(win_rate_target) else float("nan"),
        "cooldown_bars": int(cooldown_bars),
        "use_filters": bool(use_filters),
        "hurst_max": float(hurst_max) if use_filters else float("nan"),
        "liq_max": float(liq_max) if use_filters else float("nan"),
        "fee_bps": float(fee_bps),
        "allow_short": bool(allow_short),
        "walkforward": bool(walkforward),
        "train_days": int(train_days) if walkforward else 0,
        "recalib_days": int(recalib_days) if walkforward else 0,
        "optimize": bool(optimize),
        "base_z_entry": float(base_params.z_entry),
        "base_z_target": float(base_params.z_target),
        "base_z_stop": float(base_params.z_stop),
        "max_hold_bars": int(base_params.max_hold_bars),
        "start_time": str(start_time),
        "end_time": str(end_time),
        "duration_days": float(duration_days),
    }

    # Save files
    trade_csv = os.path.join(out_dir, f"trade_log_{tag}.csv")
    metrics_txt = os.path.join(out_dir, f"metrics_{tag}.txt")
    equity_png = os.path.join(out_dir, f"equity_curve_{tag}.png")

    trades_df.to_csv(trade_csv, index=False)

    with open(metrics_txt, "w", encoding="utf-8") as f:
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")

    # Equity curve plot (no manual colors)
    plt.figure(figsize=(12, 6))
    plt.plot(eq_series.index, eq_series.values)
    plt.title(f"Equity Curve ({tag})")
    plt.xlabel("Time")
    plt.ylabel("Equity")
    plt.tight_layout()
    plt.savefig(equity_png, dpi=160)
    plt.close()

    return trades_df, metrics, eq_series


# -----------------------------
# CLI
# -----------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file5m", required=True, help="5m feature file path (.csv)")
    ap.add_argument("--out_dir", default="EngineB/Reports", help="Output directory")

    # Strategy base params (used if optimize=False; or as default grid anchors)
    ap.add_argument("--z_entry", type=float, default=2.0)
    ap.add_argument("--z_target", type=float, default=0.5)
    ap.add_argument("--z_stop", type=float, default=2.8)
    ap.add_argument("--max_hold_bars", type=int, default=72)

    # Filters
    ap.add_argument("--use_filters", action="store_true", help="Enable Hurst+Liquidity entry filters")
    ap.add_argument("--hurst_max", type=float, default=0.50)
    ap.add_argument("--liq_max", type=float, default=0.0010)  # 0.10%

    # Execution constraints
    ap.add_argument("--cooldown_bars", type=int, default=12)
    ap.add_argument("--allow_short", action="store_true", help="Allow short trades (assumes perp/margin)")

    # Costs
    ap.add_argument("--fee_bps", type=float, default=4.0, help="One-way fee in basis points (e.g., 4 = 0.04%)")

    # Walk-forward controls
    ap.add_argument("--walkforward", action="store_true", help="Enable walk-forward mode (recalib schedule).")
    ap.add_argument("--train_days", type=int, default=365, help="Train lookback window (days) for walk-forward.")
    ap.add_argument("--recalib_days", type=int, default=30, help="Recalibrate every N days (days).")

    # Parameter optimization (optional)
    ap.add_argument("--optimize", action="store_true", help="If set, grid-search params each recalibration (train window only).")
    ap.add_argument("--z_entry_grid", type=str, default="", help='Comma list, e.g. "1.8,2.0,2.2"')
    ap.add_argument("--z_stop_grid", type=str, default="", help='Comma list, e.g. "2.6,2.8,3.0"')
    ap.add_argument("--z_target_grid", type=str, default="", help='Comma list, e.g. "0.3,0.5,0.7"')

    # Equity
    ap.add_argument("--start_equity", type=float, default=100.0)

    # Output tag
    ap.add_argument("--tag", type=str, default="", help="Optional label appended to outputs.")

    args = ap.parse_args()

    df = pd.read_csv(args.file5m)

    base_params = Params(
        z_entry=args.z_entry,
        z_target=args.z_target,
        z_stop=args.z_stop,
        max_hold_bars=args.max_hold_bars,
    )

    z_entry_grid = parse_csv_list(args.z_entry_grid)
    z_stop_grid = parse_csv_list(args.z_stop_grid)
    z_target_grid = parse_csv_list(args.z_target_grid)

    # Build a safe filename tag
    auto_tag_parts = [
        "filtered" if args.use_filters else "unfiltered",
        f"cd{args.cooldown_bars}",
        f"fee{args.fee_bps}bps",
        "shorts" if args.allow_short else "longonly",
        "wf" if args.walkforward else "nowf",
        "opt" if args.optimize else "noopt",
    ]
    if args.tag:
        auto_tag_parts.append(args.tag)
    tag = "_".join(auto_tag_parts)

    trades_df, metrics, eq_series = run_walkforward(
        df=df,
        out_dir=args.out_dir,
        tag=tag,
        base_params=base_params,
        start_equity=args.start_equity,
        use_filters=args.use_filters,
        hurst_max=args.hurst_max,
        liq_max=args.liq_max,
        cooldown_bars=args.cooldown_bars,
        allow_short=args.allow_short,
        fee_bps=args.fee_bps,
        walkforward=args.walkforward,
        train_days=args.train_days,
        recalib_days=args.recalib_days,
        optimize=args.optimize,
        z_entry_grid=z_entry_grid,
        z_stop_grid=z_stop_grid,
        z_target_grid=z_target_grid,
    )

    # Print summary to stdout
    print("\n" + "=" * 90)
    print(f"RUN TAG: {tag}")
    print("=" * 90)
    for k in [
        "final_equity",
        "net_return",
        "CAGR",
        "sharpe",
        "sortino",
        "calmar",
        "max_drawdown",
        "trade_count",
        "win_rate_pnl",
        "win_rate_target",
    ]:
        print(f"{k:>16}: {metrics.get(k)}")
    print("=" * 90)
    print(f"Saved trade log  : {os.path.join(args.out_dir, f'trade_log_{tag}.csv')}")
    print(f"Saved metrics txt: {os.path.join(args.out_dir, f'metrics_{tag}.txt')}")
    print(f"Saved equity png : {os.path.join(args.out_dir, f'equity_curve_{tag}.png')}")
    print("=" * 90)


if __name__ == "__main__":
    main()
