#!/usr/bin/env python3
"""
Multi-asset momentum portfolio: BTC + ETH.

Each asset runs the SAME unified HMM-TR3 engine (no per-asset tuning of the
model itself), with two risk overlays applied per sleeve:
  * ECT  — equity-curve throttle (de-risk during own losing streaks)
  * Vol-target — scale down when the asset's realized vol is elevated
  * (ETH also) min-dwell regime smoothing to cut HMM churn

Sleeves are combined at fixed capital weights. The script reports each sleeve's
standalone metrics, the realized strategy-return correlation, and the blended
portfolio metrics — the whole point being that imperfectly-correlated sleeves
lift portfolio Sharpe and smooth the drawdown.
"""

from __future__ import annotations

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
from scripts.run_holdout_ect import apply_ect
from scripts.run_portfolio import calc_equity_metrics, print_metrics, apply_vol_targeting


def ect_scaled_daily(trades_raw, daily_rets_raw, window=40, rh=1.3, rl=0.5):
    """Apply ECT to a trade log and scale the daily return series by risk_factor."""
    trades_ect = apply_ect(trades_raw, window=window, risk_high=rh, risk_low=rl)
    risk_map = pd.Series(1.0, index=daily_rets_raw.index)
    if "risk_factor" in trades_ect.columns:
        for _, row in trades_ect.iterrows():
            t_en = pd.Timestamp(row["entry_time"]); t_ex = pd.Timestamp(row["exit_time"])
            if t_en.tzinfo is None: t_en = t_en.tz_localize("UTC")
            if t_ex.tzinfo is None: t_ex = t_ex.tz_localize("UTC")
            risk_map.loc[t_en.normalize():t_ex.normalize()] = row["risk_factor"]
    return daily_rets_raw * risk_map, trades_ect


def run_sleeve(name, daily_csv, hourly_csv, vol_target, min_dwell):
    """Run one asset end-to-end -> ECT- and vol-target-scaled daily returns."""
    d = pd.read_csv(daily_csv); d["Date"] = pd.to_datetime(d["Date"], utc=True)
    d = d.set_index("Date").sort_index()
    h = pd.read_csv(hourly_csv); h["Date"] = pd.to_datetime(h["Date"], utc=True)
    h = h.set_index("Date").sort_index()

    print(f"  [{name}] walk-forward  (min_dwell={min_dwell}, vol_target={vol_target})…")
    trades_raw, daily_raw, _, states = run_btc_walkforward(d, h, min_dwell=min_dwell)
    daily_ect, trades_ect = ect_scaled_daily(trades_raw, daily_raw)

    if vol_target > 0:
        daily_ect, _scale = apply_vol_targeting(
            daily_ect, d, target_vol=vol_target, lookback=20, max_scale=1.0)

    return daily_ect.fillna(0.0), trades_ect


def per_year_table(sleeves: dict, port: pd.Series):
    print("\n  Per-year returns (each sleeve + combined):")
    hdr = f"  {'Year':<6}" + "".join(f"{n:>12}" for n in sleeves) + f"{'PORTFOLIO':>12}"
    print(hdr); print("  " + "-" * (len(hdr) - 2))
    years = sorted(port.index.year.unique())
    for yr in years:
        row = f"  {yr:<6}"
        for n, s in sleeves.items():
            sy = s[s.index.year == yr]
            row += f"{((1+sy).prod()-1)*100:>11.1f}%"
        py = port[port.index.year == yr]
        row += f"{((1+py).prod()-1)*100:>11.1f}%"
        print(row)


def main():
    ap = argparse.ArgumentParser(description="BTC+ETH multi-asset momentum portfolio")
    ap.add_argument("--out-dir", default="outputs/portfolio_multi")
    ap.add_argument("--btc-vol-target", type=float, default=0.40)
    ap.add_argument("--eth-vol-target", type=float, default=0.50)
    ap.add_argument("--btc-min-dwell", type=int, default=1)
    ap.add_argument("--eth-min-dwell", type=int, default=2)
    ap.add_argument("--btc-weight", type=float, default=0.50)
    args = ap.parse_args()

    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)

    print("Building multi-asset portfolio (BTC + ETH)…\n")
    btc_r, btc_tr = run_sleeve(
        "BTC", "data/processed/btc_1d_features.csv",
        "data/processed/btc_1h_features_tr.csv",
        args.btc_vol_target, args.btc_min_dwell)
    eth_r, eth_tr = run_sleeve(
        "ETH", "data/processed/eth_1d_features.csv",
        "data/processed/eth_1h_features_tr.csv",
        args.eth_vol_target, args.eth_min_dwell)

    # ---- Align to the common window where BOTH sleeves are live ----
    start = max(btc_r.index.min(), eth_r.index.min())
    end   = min(btc_r.index.max(), eth_r.index.max())
    cal = pd.date_range(start, end, freq="D", tz="UTC")
    btc_a = btc_r.reindex(cal, fill_value=0.0)
    eth_a = eth_r.reindex(cal, fill_value=0.0)
    print(f"\n  Common window: {start.date()} -> {end.date()}  ({len(cal)} days)")

    # ---- Realized strategy-return correlation ----
    both_active = (btc_a != 0) & (eth_a != 0)
    corr_all = btc_a.corr(eth_a)
    corr_active = btc_a[both_active].corr(eth_a[both_active])
    print(f"\n  Realized strategy-return correlation:")
    print(f"    all overlapping days ...... {corr_all:.2f}")
    print(f"    days both in-market ....... {corr_active:.2f}   (n={int(both_active.sum())})")
    print(f"    (BTC/ETH raw ASSET correlation was 0.83 — strategy is far lower)")

    # ---- Combine at fixed weights ----
    w = args.btc_weight
    port = (w * btc_a + (1 - w) * eth_a)

    sleeves = {"BTC": btc_a, "ETH": eth_a}
    m_btc = calc_equity_metrics(btc_a)
    m_eth = calc_equity_metrics(eth_a)
    m_prt = calc_equity_metrics(port)

    print_metrics(m_btc, f"BTC SLEEVE  (vol {args.btc_vol_target}, dwell {args.btc_min_dwell})")
    print_metrics(m_eth, f"ETH SLEEVE  (vol {args.eth_vol_target}, dwell {args.eth_min_dwell})")
    print_metrics(m_prt, f"COMBINED PORTFOLIO  ({w:.0%} BTC / {1-w:.0%} ETH)")

    per_year_table(sleeves, port)

    # ---- Save ----
    eq = pd.DataFrame({
        "btc": (1 + btc_a).cumprod(),
        "eth": (1 + eth_a).cumprod(),
        "portfolio": (1 + port).cumprod(),
        "ret_btc": btc_a, "ret_eth": eth_a, "ret_portfolio": port,
    })
    eq.to_csv(out / "equity_curve.csv")

    # ---- Chart ----
    fig, ax = plt.subplots(2, 1, figsize=(14, 9), sharex=True,
                           gridspec_kw={"height_ratios": [3, 1]})
    ax[0].plot(eq.index, eq["btc"],  color="steelblue", lw=1.1, alpha=0.7,
               label=f"BTC   CAGR {m_btc['CAGR']:.1%}  Sh {m_btc['Sharpe']:.2f}  DD {m_btc['MaxDrawdown']:.1%}")
    ax[0].plot(eq.index, eq["eth"],  color="mediumpurple", lw=1.1, alpha=0.7,
               label=f"ETH   CAGR {m_eth['CAGR']:.1%}  Sh {m_eth['Sharpe']:.2f}  DD {m_eth['MaxDrawdown']:.1%}")
    ax[0].plot(eq.index, eq["portfolio"], color="seagreen", lw=2.2,
               label=f"PORTFOLIO  CAGR {m_prt['CAGR']:.1%}  Sh {m_prt['Sharpe']:.2f}  DD {m_prt['MaxDrawdown']:.1%}")
    ax[0].set_yscale("log"); ax[0].set_ylabel("Equity (log)")
    ax[0].set_title(f"BTC + ETH Momentum Portfolio  |  corr {corr_all:.2f}")
    ax[0].legend(fontsize=9); ax[0].grid(True, alpha=0.3)

    for s, c, lab in [(btc_a, "steelblue", "BTC"), (eth_a, "mediumpurple", "ETH"), (port, "seagreen", "Portfolio")]:
        e = (1 + s).cumprod(); dd = (e - e.cummax()) / e.cummax()
        ax[1].plot(dd.index, dd.values, color=c, lw=1.3 if lab == "Portfolio" else 0.9,
                   alpha=1.0 if lab == "Portfolio" else 0.5, label=lab)
    ax[1].set_ylabel("Drawdown"); ax[1].legend(fontsize=8); ax[1].grid(True, alpha=0.3)

    plt.tight_layout(); plt.savefig(out / "portfolio_chart.png", dpi=150)
    print(f"\nSaved: {out}/portfolio_chart.png  |  equity_curve.csv")


if __name__ == "__main__":
    main()
