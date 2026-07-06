#!/usr/bin/env python3
"""
HMM-TR3 BTC Strategy Runner — Long (TR3) + Bear-Regime Short Overlay

Long side  : TR3 momentum entries when HMM state = bullish (state 1), sized by ECT.
Short side : Fixed-size short BTC when HMM state = bearish (state 2).
             No entry filter — pure regime signal.
"""

import sys
import argparse
from pathlib import Path
from math import sqrt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.run_btc_strategy import run_btc_walkforward
from scripts.run_holdout_ect import apply_ect, metrics_from_trades


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_btc_data(daily_path: Path, hourly_path: Path):
    d = pd.read_csv(daily_path)
    if "time" in d.columns:
        d = d.rename(columns={"time": "Date"})
    d["Date"] = pd.to_datetime(d["Date"], utc=True)
    d = d.set_index("Date").sort_index()

    h = pd.read_csv(hourly_path)
    if "time" in h.columns:
        h = h.rename(columns={"time": "Date"})
    h["Date"] = pd.to_datetime(h["Date"], utc=True)
    h = h.set_index("Date").sort_index()

    return d, h


# ---------------------------------------------------------------------------
# Bear-regime short overlay
# ---------------------------------------------------------------------------

def compute_bear_short_overlay(
    btc_d: pd.DataFrame,
    states_series: pd.Series,
    short_size: float = 0.25,
    bear_state: int = 2,
    ema_period: int = 200,
    min_dwell: int = 7,
) -> pd.Series:
    """
    Daily P&L from a short BTC position when ALL of the following are true:
      1. HMM state == bear_state  (regime signal)
      2. BTC Close < EMA_{ema_period}  (macro trend guard)
      3. State has been bear for at least min_dwell consecutive days
         (filters out brief corrections within bull trends)

    Timing: all conditions checked with T-1 data (no lookahead).
    Position captures Open[T+1]/Open[T]-1, negated.
    """
    # Macro filter: Close < EMA_200 (lag-1 = known at T's open)
    ema200 = btc_d["Close"].ewm(span=ema_period, adjust=False).mean()
    below_ema = (btc_d["Close"] < ema200).shift(1)
    below_ema = below_ema.reindex(states_series.index, fill_value=False)

    # Min-dwell filter: state=2 must have been active for min_dwell consecutive days
    is_bear = (states_series == bear_state).astype(int)
    streak = is_bear.copy().astype(float)
    for i in range(1, len(streak)):
        streak.iloc[i] = streak.iloc[i] * (streak.iloc[i - 1] + 1) if is_bear.iloc[i] else 0.0
    dwell_ok = streak >= min_dwell

    bear_mask = (states_series == bear_state) & below_ema & dwell_ok

    # Forward open-to-open return
    ret_forward = btc_d["Open"].pct_change().shift(-1)
    ret_forward = ret_forward.reindex(states_series.index)

    short_ret = pd.Series(0.0, index=states_series.index)
    short_ret[bear_mask] = -short_size * ret_forward[bear_mask]
    return short_ret.fillna(0.0)


# ---------------------------------------------------------------------------
# Volatility targeting
# ---------------------------------------------------------------------------

def apply_vol_targeting(
    daily_rets: pd.Series,
    btc_d: pd.DataFrame,
    target_vol: float = 0.15,
    lookback: int = 20,
    max_scale: float = 1.5,
) -> pd.Series:
    """
    Scale daily strategy returns so the portfolio targets `target_vol` annual vol.

    Scale[T] = clip( target_vol / RealizedVol[T-1], 0.1, max_scale )
    RealizedVol is computed from BTC daily close-to-close returns (20-day window),
    annualised with sqrt(365), and lagged by 1 day (no lookahead).

    Interpretation:
      - BTC realized vol 60% → scale = 15/60 = 0.25  (quarter-size)
      - BTC realized vol 20% → scale = 15/20 = 0.75
      - BTC realized vol 10% → scale capped at max_scale = 1.5
    """
    btc_ret = btc_d["Close"].pct_change()
    realized_vol = btc_ret.rolling(lookback).std() * sqrt(365)
    realized_vol = realized_vol.shift(1)                     # lag-1: known at open
    realized_vol = realized_vol.reindex(daily_rets.index).ffill()

    scale = (target_vol / realized_vol).clip(lower=0.1, upper=max_scale)
    scale = scale.fillna(1.0)
    return daily_rets * scale, scale


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def calc_equity_metrics(daily_rets: pd.Series) -> dict:
    cum = (1 + daily_rets).cumprod()
    total_ret = cum.iloc[-1] - 1
    years = (daily_rets.index[-1] - daily_rets.index[0]).days / 365.25
    cagr = (1 + total_ret) ** (1 / years) - 1 if years > 0 else 0.0
    sharpe = (daily_rets.mean() / daily_rets.std()) * sqrt(365) if daily_rets.std() > 0 else 0.0
    dd = (cum - cum.cummax()) / cum.cummax()
    max_dd = dd.min()
    calmar = cagr / abs(max_dd) if max_dd < 0 else float("nan")
    sortino_d = daily_rets[daily_rets < 0].std()
    sortino = (daily_rets.mean() / sortino_d) * sqrt(365) if sortino_d > 0 else float("nan")
    return {
        "TotalReturn": total_ret,
        "CAGR": cagr,
        "MaxDrawdown": max_dd,
        "Sharpe": sharpe,
        "Sortino": sortino,
        "Calmar": calmar,
        "AnnualVolatility": daily_rets.std() * sqrt(365),
    }


def print_metrics(m: dict, title: str):
    pct_keys = {"TotalReturn", "CAGR", "MaxDrawdown", "AnnualVolatility"}
    print(f"\n{title}")
    print("-" * 40)
    for k, v in m.items():
        if k in pct_keys and isinstance(v, float):
            print(f"  {k:<24}: {v:.2%}")
        elif isinstance(v, float):
            print(f"  {k:<24}: {v:.3f}")
        else:
            print(f"  {k:<24}: {v}")
    print("-" * 40)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="BTC HMM-TR3 + Bear-Short Overlay")
    parser.add_argument("--out-dir",    default="outputs/portfolio_walkforward")
    parser.add_argument("--train-end",  default="2021-12-31")
    parser.add_argument("--ect-window", type=int,   default=40)
    parser.add_argument("--risk-high",  type=float, default=1.3)
    parser.add_argument("--risk-low",   type=float, default=0.5)
    parser.add_argument("--short-size",  type=float, default=0.0,
                        help="Fractional BTC short in bearish regime (0 = long-only)")
    parser.add_argument("--vol-target",  type=float, default=0.0,
                        help="Annual vol target for position scaling (0 = disabled)")
    parser.add_argument(
        "--daily",
        default=str(PROJECT_ROOT / "data/processed/btc_1d_features.csv"),
    )
    parser.add_argument(
        "--hourly",
        default=str(PROJECT_ROOT / "data/processed/btc_1h_features_tr.csv"),
    )
    args = parser.parse_args()

    out_path = Path(args.out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Load data
    # ------------------------------------------------------------------
    print("Loading BTC data…")
    btc_d, btc_h = load_btc_data(Path(args.daily), Path(args.hourly))

    # ------------------------------------------------------------------
    # 2. Run BTC walk-forward (long / TR3 side)
    # ------------------------------------------------------------------
    print(f"\nRunning BTC Walk-Forward (train_end={args.train_end})…")
    trades_raw, daily_rets_raw, _, states_series = run_btc_walkforward(
        btc_d, btc_h, train_end=args.train_end
    )

    if trades_raw.empty:
        print("No trades generated.")
        return

    # ------------------------------------------------------------------
    # 3. Apply ECT to long side
    # ------------------------------------------------------------------
    print(f"\nApplying ECT (window={args.ect_window}, "
          f"risk_high={args.risk_high}, risk_low={args.risk_low})…")
    trades_ect = apply_ect(
        trades_raw,
        window=args.ect_window,
        risk_high=args.risk_high,
        risk_low=args.risk_low,
    )
    trades_ect.to_csv(out_path / "trades_btc_long.csv", index=False)

    # Scale daily long returns by ECT risk factor
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

    daily_rets_long = daily_rets_raw * risk_map

    # ------------------------------------------------------------------
    # 4. Volatility targeting (optional)
    # ------------------------------------------------------------------
    vol_scale = None
    if args.vol_target > 0:
        print(f"\nApplying vol targeting (target={args.vol_target:.0%}, lookback=20d)…")
        daily_rets_long, vol_scale = apply_vol_targeting(
            daily_rets_long, btc_d,
            target_vol=args.vol_target, lookback=20, max_scale=1.5,
        )
        print(f"  Scale range: {vol_scale.min():.2f}× – {vol_scale.max():.2f}×  "
              f"mean {vol_scale.mean():.2f}×")

    # ------------------------------------------------------------------
    # 5. Bear-regime short overlay
    # ------------------------------------------------------------------
    short_size = args.short_size
    if short_size > 0:
        print(f"\nComputing bear-regime short overlay "
              f"(size={short_size:.0%}, HMM state 2)…")
        daily_rets_short = compute_bear_short_overlay(
            btc_d, states_series, short_size=short_size, bear_state=2,
            ema_period=200, min_dwell=3,
        )

        # Align to common calendar
        idx = daily_rets_long.index.union(daily_rets_short.index)
        daily_rets_long  = daily_rets_long.reindex(idx, fill_value=0.0)
        daily_rets_short = daily_rets_short.reindex(idx, fill_value=0.0)
        daily_rets_combined = daily_rets_long + daily_rets_short

        bear_days = (states_series == 2).reindex(idx, fill_value=False)
        n_bear = int(bear_days.sum())
        bear_total = daily_rets_short[bear_days].sum()
        print(f"  Bear-regime days shorted: {n_bear} "
              f" |  Short overlay cumulative return: {bear_total:.2%}")
    else:
        daily_rets_combined = daily_rets_long
        daily_rets_short    = pd.Series(0.0, index=daily_rets_long.index)

    # ------------------------------------------------------------------
    # 6. Metrics
    # ------------------------------------------------------------------
    m_long  = calc_equity_metrics(daily_rets_long)
    m_combo = calc_equity_metrics(daily_rets_combined)
    m_tr3   = metrics_from_trades(trades_ect, "net_ret_scaled")

    print_metrics(m_tr3,   "TR3 LONG TRADES (ECT-scaled)")
    print_metrics(m_long,  "LONG-ONLY EQUITY CURVE")
    print_metrics(m_combo, "COMBINED (LONG + SHORT OVERLAY)")

    # Per-year breakdown
    print("\n  Per-year combined breakdown:")
    print(f"  {'Year':<6} {'Return':>8}  {'Sharpe':>8}  {'Long ret':>9}  {'Short ret':>9}")
    print(f"  {'-'*48}")
    for yr in sorted(daily_rets_combined.index.year.unique()):
        mask = daily_rets_combined.index.year == yr
        r_c = daily_rets_combined[mask]
        r_l = daily_rets_long[mask]
        r_s = daily_rets_short[mask]
        ann_ret = (1 + r_c).prod() - 1
        sh = (r_c.mean() / r_c.std()) * sqrt(365) if r_c.std() > 0 else float("nan")
        l_ret = (1 + r_l).prod() - 1
        s_ret = (1 + r_s).prod() - 1
        print(f"  {yr:<6} {ann_ret:>8.2%}  {sh:>8.2f}  {l_ret:>9.2%}  {s_ret:>9.2%}")

    # ------------------------------------------------------------------
    # 6. Save outputs
    # ------------------------------------------------------------------
    pd.DataFrame({
        "equity_long_only": (1 + daily_rets_long).cumprod(),
        "equity_combined":  (1 + daily_rets_combined).cumprod(),
        "daily_ret_long":   daily_rets_long,
        "daily_ret_short":  daily_rets_short,
        "daily_ret_combined": daily_rets_combined,
    }).to_csv(out_path / "equity_curve.csv")

    # ------------------------------------------------------------------
    # 7. Chart
    # ------------------------------------------------------------------
    equity_long  = (1 + daily_rets_long).cumprod()
    equity_combo = (1 + daily_rets_combined).cumprod()

    fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True,
                             gridspec_kw={"height_ratios": [3, 1, 1]})

    axes[0].plot(equity_long.index,  equity_long.values,
                 color="steelblue", linewidth=1.2, alpha=0.65,
                 label=f"Long-only   CAGR {m_long['CAGR']:.1%}  Sharpe {m_long['Sharpe']:.2f}")
    axes[0].plot(equity_combo.index, equity_combo.values,
                 color="seagreen", linewidth=2.0,
                 label=f"Long+Short  CAGR {m_combo['CAGR']:.1%}  Sharpe {m_combo['Sharpe']:.2f}")
    axes[0].set_yscale("log")
    axes[0].set_ylabel("Equity (log scale)")
    axes[0].set_title(
        f"BTC HMM-TR3  |  Bear short {short_size:.0%} in state-2 regime"
    )
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)

    dd_long  = (equity_long  - equity_long.cummax())  / equity_long.cummax()
    dd_combo = (equity_combo - equity_combo.cummax()) / equity_combo.cummax()
    axes[1].fill_between(dd_long.index,  dd_long.values,  0,
                         color="steelblue", alpha=0.45,
                         label=f"Long-only  max {m_long['MaxDrawdown']:.1%}")
    axes[1].fill_between(dd_combo.index, dd_combo.values, 0,
                         color="seagreen",  alpha=0.55,
                         label=f"Combined   max {m_combo['MaxDrawdown']:.1%}")
    axes[1].set_ylabel("Drawdown")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    axes[2].fill_between(daily_rets_short.index, daily_rets_short.values, 0,
                         where=(daily_rets_short > 0),
                         color="seagreen", alpha=0.65, label="Short overlay — gain")
    axes[2].fill_between(daily_rets_short.index, daily_rets_short.values, 0,
                         where=(daily_rets_short < 0),
                         color="salmon",   alpha=0.65, label="Short overlay — loss")
    axes[2].set_ylabel("Short daily P&L")
    axes[2].legend(fontsize=8)
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path / "equity_chart.png", dpi=150)
    print(f"\nSaved: {out_path}/equity_chart.png  |  equity_curve.csv  |  trades_btc_long.csv")


if __name__ == "__main__":
    main()
