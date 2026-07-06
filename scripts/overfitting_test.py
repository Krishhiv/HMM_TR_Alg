#!/usr/bin/env python3
"""
Overfitting / robustness test for the BTC+ETH momentum portfolio.

The HMM+TR3 engine is already walk-forward OOS. The overlays (vol-target,
min_dwell, weight) were chosen on full-period hindsight, so this script stress-
tests THOSE choices:

  Test 1  Parameter sensitivity grid — is Sharpe a robust plateau or a spike?
  Test 2  Monte-Carlo block bootstrap — confidence interval on the Sharpe.
  Test 3  Sub-period stability — does it hold in both halves of the sample?

Walk-forwards are run once per sleeve; the overlays are swept offline (cheap).
"""

from __future__ import annotations
import sys
from pathlib import Path
from math import sqrt

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.run_btc_strategy import run_btc_walkforward
from scripts.run_portfolio_multi import ect_scaled_daily


def load_close(csv):
    d = pd.read_csv(csv); d["Date"] = pd.to_datetime(d["Date"], utc=True)
    return d.set_index("Date").sort_index()["Close"]


def sleeve_ect(daily_csv, hourly_csv, min_dwell):
    d = pd.read_csv(daily_csv); d["Date"] = pd.to_datetime(d["Date"], utc=True); d = d.set_index("Date").sort_index()
    h = pd.read_csv(hourly_csv); h["Date"] = pd.to_datetime(h["Date"], utc=True); h = h.set_index("Date").sort_index()
    trades, draw, _, _ = run_btc_walkforward(d, h, min_dwell=min_dwell)
    ect, _ = ect_scaled_daily(trades, draw)
    return ect.fillna(0.0)


def voltarget(r, close, tgt, lb=20, ms=1.0):
    if tgt <= 0:
        return r
    rv = (close.pct_change().rolling(lb).std() * sqrt(365)).shift(1).reindex(r.index).ffill()
    return r * (tgt / rv).clip(0.1, ms).fillna(1.0)


def metrics(x):
    cum = (1 + x).cumprod(); tot = cum.iloc[-1] - 1
    yrs = (x.index[-1] - x.index[0]).days / 365.25
    cagr = (1 + tot) ** (1 / yrs) - 1
    sh = (x.mean() / x.std()) * sqrt(365) if x.std() > 0 else 0.0
    dd = ((cum - cum.cummax()) / cum.cummax()).min()
    return cagr, sh, dd


def combine(btc_r, eth_r, w):
    start = max(btc_r.index.min(), eth_r.index.min())
    end = min(btc_r.index.max(), eth_r.index.max())
    cal = pd.date_range(start, end, freq="D", tz="UTC")
    b = btc_r.reindex(cal, fill_value=0.0); e = eth_r.reindex(cal, fill_value=0.0)
    return w * b + (1 - w) * e


def main():
    print("Running walk-forwards (once each)…")
    btc_ect = sleeve_ect("data/processed/btc_1d_features.csv",
                         "data/processed/btc_1h_features_tr.csv", min_dwell=1)
    eth_ect = sleeve_ect("data/processed/eth_1d_features.csv",
                         "data/processed/eth_1h_features_tr.csv", min_dwell=2)
    btc_close = load_close("data/processed/btc_1d_features.csv")
    eth_close = load_close("data/processed/eth_1d_features.csv")

    chosen = dict(bt=0.40, et=0.50, w=0.50)
    c, s, dd = metrics(combine(voltarget(btc_ect, btc_close, chosen["bt"]),
                               voltarget(eth_ect, eth_close, chosen["et"]),
                               chosen["w"]))
    print(f"\nChosen config: BTC vol {chosen['bt']}, ETH vol {chosen['et']}, "
          f"weight {chosen['w']:.0%}/{1-chosen['w']:.0%}")
    print(f"  -> CAGR {c:.2%}  Sharpe {s:.3f}  MaxDD {dd:.2%}")

    # ---------------- Test 1: parameter sensitivity grid ----------------
    print("\n" + "=" * 62)
    print("TEST 1  PARAMETER SENSITIVITY  (80 configs around the choice)")
    print("=" * 62)
    sharpes, cagrs, dds = [], [], []
    for bt in [0.30, 0.40, 0.50, 0.60]:
        for et in [0.40, 0.50, 0.60, 0.70]:
            for w in [0.30, 0.40, 0.50, 0.60, 0.70]:
                pr = combine(voltarget(btc_ect, btc_close, bt),
                             voltarget(eth_ect, eth_close, et), w)
                cc, ss, d2 = metrics(pr)
                sharpes.append(ss); cagrs.append(cc); dds.append(d2)
    sharpes = np.array(sharpes); cagrs = np.array(cagrs); dds = np.array(dds)
    print(f"  configs tested ......... {len(sharpes)}")
    print(f"  Sharpe  min/median/max . {sharpes.min():.2f} / {np.median(sharpes):.2f} / {sharpes.max():.2f}")
    print(f"  CAGR    min/median/max . {cagrs.min():.1%} / {np.median(cagrs):.1%} / {cagrs.max():.1%}")
    print(f"  MaxDD   min/median/max . {dds.min():.1%} / {np.median(dds):.1%} / {dds.max():.1%}")
    print(f"  % configs Sharpe > 1.40  {(sharpes > 1.40).mean():.0%}")
    print(f"  % configs Sharpe > 1.50  {(sharpes > 1.50).mean():.0%}")
    print(f"  % configs CAGR   > 20%   {(cagrs > 0.20).mean():.0%}")
    print("  -> Robust if the chosen 1.68 sits INSIDE a broad high-Sharpe plateau,")
    print("     not alone at the top.")

    # ---------------- Test 2: Monte-Carlo block bootstrap ----------------
    print("\n" + "=" * 62)
    print("TEST 2  MONTE-CARLO BLOCK BOOTSTRAP  (Sharpe confidence interval)")
    print("=" * 62)
    port = combine(voltarget(btc_ect, btc_close, chosen["bt"]),
                   voltarget(eth_ect, eth_close, chosen["et"]), chosen["w"])
    vals = port.values; L = len(vals); block = 20; nboot = 5000
    rng = np.random.default_rng(42)
    nb = int(np.ceil(L / block))
    boot = np.empty(nboot)
    for i in range(nboot):
        starts = rng.integers(0, L - block, nb)
        samp = np.concatenate([vals[st:st + block] for st in starts])[:L]
        sd = samp.std()
        boot[i] = (samp.mean() / sd) * sqrt(365) if sd > 0 else 0.0
    print(f"  resamples .............. {nboot}  (20-day blocks, preserves autocorr)")
    print(f"  Sharpe  5th percentile . {np.percentile(boot, 5):.2f}")
    print(f"  Sharpe  50th (median) .. {np.percentile(boot, 50):.2f}")
    print(f"  Sharpe  95th percentile  {np.percentile(boot, 95):.2f}")
    print(f"  P(Sharpe > 1.0) ........ {(boot > 1.0).mean():.0%}")
    print(f"  P(Sharpe > 0)  ......... {(boot > 0.0).mean():.0%}")
    print("  -> Healthy if the 5th percentile stays clearly positive (edge is not")
    print("     a fluke of a few lucky windows).")

    # ---------------- Test 3: sub-period stability ----------------
    print("\n" + "=" * 62)
    print("TEST 3  SUB-PERIOD STABILITY  (independent halves)")
    print("=" * 62)
    mid = port.index[len(port) // 2]
    h1 = port.loc[:mid]; h2 = port.loc[mid:]
    for lab, seg in [("first half ", h1), ("second half", h2)]:
        cc, ss, d2 = metrics(seg)
        print(f"  {lab} {seg.index[0].date()}..{seg.index[-1].date()}:  "
              f"CAGR {cc:>7.1%}  Sharpe {ss:>5.2f}  MaxDD {d2:>7.1%}")
    print("  -> Robust if BOTH halves are profitable with sane Sharpe (not one")
    print("     half carrying the entire result).")


if __name__ == "__main__":
    main()
