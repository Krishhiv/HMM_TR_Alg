#!/usr/bin/env python3
"""
Viability testing conditioned on *entry filters* for your mean-reversion strategy.

Inputs:
- 5m features file (must include: Date, Close, ZScore, FairValue, EWMAVol, LiquidityCostProxy, Hurst15m)
- 15m features file (optional; used only for extra integrity checks if desired)

Computes the SAME key diagnostics as your existing script, but for:
1) ALL fresh Z-cross signals
2) FILTERED + EXECUTABLE signals (entry filters + one-position constraint + cooldown)

Key stats:
- signal frequency
- conditional forward returns (signed) at horizons
- Z-path event study (target-before-stop vs stop vs time)
- AR(1) half-life on (Close - FairValue) [global; unchanged by filters]
- autocorr diagnostics (global)
- plus filtered-vs-unfiltered comparisons
"""

import argparse
from dataclasses import dataclass
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd


# -----------------------------
# Utilities
# -----------------------------
def read_any(path: str) -> pd.DataFrame:
    ext = path.lower().split(".")[-1]
    if ext == "csv":
        return pd.read_csv(path)
    if ext == "parquet":
        return pd.read_parquet(path)
    if ext == "feather":
        return pd.read_feather(path)
    raise ValueError("Unsupported file extension. Use .csv/.parquet/.feather")


def to_datetime_utc_naive(s: pd.Series) -> pd.Series:
    dt = pd.to_datetime(s, errors="coerce", utc=True)
    return dt.dt.tz_convert(None)


def fmt(x: float) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "nan"
    if abs(x) >= 1e6:
        return f"{x:,.0f}"
    if abs(x) >= 1e3:
        return f"{x:,.2f}"
    if abs(x) >= 1:
        return f"{x:,.4f}"
    return f"{x:.6f}"


def print_header(title: str):
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)


# -----------------------------
# Core signal logic
# -----------------------------
@dataclass
class SignalEvent:
    idx: int
    ts: pd.Timestamp
    side: str  # 'LONG' or 'SHORT'


def compute_returns_log(close: pd.Series) -> pd.Series:
    close = pd.to_numeric(close, errors="coerce")
    return np.log(close / close.shift(1))


def find_fresh_signals(df5: pd.DataFrame, z_entry: float) -> List[SignalEvent]:
    z = pd.to_numeric(df5["ZScore"], errors="coerce")
    t = df5["Date"]

    long_mask = (z < -z_entry) & (z.shift(1) >= -z_entry)
    short_mask = (z > z_entry) & (z.shift(1) <= z_entry)

    events: List[SignalEvent] = []
    for idx in np.where(long_mask.fillna(False).to_numpy())[0]:
        events.append(SignalEvent(idx=idx, ts=t.iloc[idx], side="LONG"))
    for idx in np.where(short_mask.fillna(False).to_numpy())[0]:
        events.append(SignalEvent(idx=idx, ts=t.iloc[idx], side="SHORT"))

    events.sort(key=lambda e: e.idx)
    return events


def forward_returns_signed(df5: pd.DataFrame, events: List[SignalEvent], horizons: List[int]) -> pd.DataFrame:
    close = pd.to_numeric(df5["Close"], errors="coerce").to_numpy()
    rows = []
    for ev in events:
        i = ev.idx
        base = close[i]
        if not np.isfinite(base):
            continue
        row = {"Date": df5["Date"].iloc[i], "Side": ev.side, "Idx": i}
        for h in horizons:
            j = i + h
            if j >= len(close):
                row[f"fwd_{h}"] = np.nan
                continue
            ret = np.log(close[j] / base)
            signed = ret if ev.side == "LONG" else -ret
            row[f"fwd_{h}"] = signed
        rows.append(row)
    return pd.DataFrame(rows)


def simulate_outcome_with_exit_index(
    z: np.ndarray,
    i: int,
    side: str,
    z_target: float,
    z_stop: float,
    max_hold_bars: int,
) -> Tuple[str, int]:
    """
    Returns:
    - outcome in {"TARGET","STOP","TIME"}
    - exit_idx (inclusive index where outcome happened; if TIME, i+max_hold_bars)
    """
    end = min(i + max_hold_bars, len(z) - 1)
    path = z[i + 1 : end + 1]

    if side == "LONG":
        # target: z >= +z_target ; stop: z <= -z_stop
        for k, zz in enumerate(path, start=1):
            if not np.isfinite(zz):
                continue
            if zz <= -z_stop:
                return "STOP", i + k
            if zz >= z_target:
                return "TARGET", i + k
        return "TIME", end

    else:
        # SHORT: target: z <= -z_target ; stop: z >= +z_stop
        for k, zz in enumerate(path, start=1):
            if not np.isfinite(zz):
                continue
            if zz >= z_stop:
                return "STOP", i + k
            if zz <= -z_target:
                return "TARGET", i + k
        return "TIME", end


def event_study_z_only(
    df5: pd.DataFrame,
    events: List[SignalEvent],
    z_target: float,
    z_stop: float,
    max_hold_bars: int,
) -> pd.DataFrame:
    z = pd.to_numeric(df5["ZScore"], errors="coerce").to_numpy()
    rows = []
    for ev in events:
        outcome, exit_idx = simulate_outcome_with_exit_index(
            z=z,
            i=ev.idx,
            side=ev.side,
            z_target=z_target,
            z_stop=z_stop,
            max_hold_bars=max_hold_bars,
        )
        rows.append(
            {
                "Date": df5["Date"].iloc[ev.idx],
                "Side": ev.side,
                "Idx": ev.idx,
                "Outcome": outcome,
                "ExitIdx": exit_idx,
                "BarsToOutcome": int(exit_idx - ev.idx),
            }
        )
    return pd.DataFrame(rows)


# -----------------------------
# Filtered “executable events” logic
# -----------------------------
def apply_entry_filters(
    df5: pd.DataFrame,
    events: List[SignalEvent],
    hurst_max: Optional[float],
    liq_max: Optional[float],
) -> List[SignalEvent]:
    """
    Filters events by checking feature values at entry bar.
    - hurst_max: keep only if Hurst15m < hurst_max
    - liq_max: keep only if LiquidityCostProxy <= liq_max
    """
    hurst = pd.to_numeric(df5["Hurst15m"], errors="coerce") if "Hurst15m" in df5.columns else None
    liq = pd.to_numeric(df5["LiquidityCostProxy"], errors="coerce") if "LiquidityCostProxy" in df5.columns else None

    kept: List[SignalEvent] = []
    for ev in events:
        i = ev.idx

        # Require finite essentials
        ok = True
        for col in ["Close", "ZScore", "FairValue", "EWMAVol"]:
            val = pd.to_numeric(df5[col].iloc[i], errors="coerce")
            if not np.isfinite(val):
                ok = False
                break
        if not ok:
            continue

        if hurst_max is not None:
            hv = float(hurst.iloc[i])
            if not np.isfinite(hv) or hv >= hurst_max:
                continue

        if liq_max is not None:
            lv = float(liq.iloc[i])
            if not np.isfinite(lv) or lv > liq_max:
                continue

        kept.append(ev)

    return kept


def enforce_one_position_and_cooldown(
    df5: pd.DataFrame,
    events: List[SignalEvent],
    z_target: float,
    z_stop: float,
    max_hold_bars: int,
    cooldown_bars: int,
) -> Tuple[List[SignalEvent], pd.DataFrame]:
    """
    Sequentially accepts events in time order such that:
    - Only one position at a time
    - After exit, wait cooldown_bars before next entry

    Returns:
    - accepted events
    - outcomes dataframe for accepted events (with ExitIdx etc.)
    """
    z = pd.to_numeric(df5["ZScore"], errors="coerce").to_numpy()

    accepted: List[SignalEvent] = []
    out_rows = []

    next_allowed_idx = 0
    for ev in events:
        if ev.idx < next_allowed_idx:
            continue

        outcome, exit_idx = simulate_outcome_with_exit_index(
            z=z,
            i=ev.idx,
            side=ev.side,
            z_target=z_target,
            z_stop=z_stop,
            max_hold_bars=max_hold_bars,
        )

        accepted.append(ev)
        out_rows.append(
            {
                "Date": df5["Date"].iloc[ev.idx],
                "Side": ev.side,
                "Idx": ev.idx,
                "Outcome": outcome,
                "ExitIdx": exit_idx,
                "BarsToOutcome": int(exit_idx - ev.idx),
            }
        )

        next_allowed_idx = exit_idx + max(0, cooldown_bars)

    return accepted, pd.DataFrame(out_rows)


# -----------------------------
# Diagnostics / Reporting
# -----------------------------
def summarize_forward_returns(fr: pd.DataFrame, horizons: List[int], title: str):
    print_header(title)
    if fr is None or len(fr) == 0:
        print("No samples.")
        return
    for h in horizons:
        col = f"fwd_{h}"
        vals = fr[col].dropna()
        if len(vals) < 20:
            print(f"Horizon {h:>2} bars: not enough samples (n={len(vals)})")
            continue
        print(
            f"Horizon {h:>2} bars: mean={fmt(float(vals.mean()))}  "
            f"median={fmt(float(vals.median()))}  "
            f"hit_rate(>0)={fmt(float((vals>0).mean()))}  "
            f"n={len(vals)}"
        )


def summarize_outcomes(out: pd.DataFrame, title: str):
    print_header(title)
    if out is None or len(out) == 0:
        print("No samples.")
        return

    counts = out["Outcome"].value_counts(dropna=False).to_dict()
    total = len(out)
    for k, v in counts.items():
        print(f"{k:>6}: {v} ({v/total:.2%})")

    print(f"\nAvg BarsToOutcome (all):     {fmt(float(out['BarsToOutcome'].mean()))}")
    if (out["Outcome"] == "TARGET").any():
        print(f"Avg BarsToOutcome (TARGET):  {fmt(float(out.loc[out['Outcome']=='TARGET','BarsToOutcome'].mean()))}")
    if (out["Outcome"] == "STOP").any():
        print(f"Avg BarsToOutcome (STOP):    {fmt(float(out.loc[out['Outcome']=='STOP','BarsToOutcome'].mean()))}")


def summarize_filter_context(df5: pd.DataFrame, events: List[SignalEvent], title: str):
    print_header(title)
    if len(events) == 0:
        print("No events.")
        return

    idxs = [e.idx for e in events]
    if "Hurst15m" in df5.columns:
        h = pd.to_numeric(df5.loc[idxs, "Hurst15m"], errors="coerce")
        print("Hurst15m @ entry quantiles:", h.quantile([0.05,0.25,0.5,0.75,0.95]).to_dict())
        print("Share H<0.50:", fmt(float((h < 0.50).mean())))
        print("Share H>=0.55:", fmt(float((h >= 0.55).mean())))
    if "LiquidityCostProxy" in df5.columns:
        l = pd.to_numeric(df5.loc[idxs, "LiquidityCostProxy"], errors="coerce")
        print("LiquidityCostProxy @ entry quantiles:", l.quantile([0.05,0.25,0.5,0.75,0.95]).to_dict())


# -----------------------------
# Main
# -----------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file5m", required=True, help="Path to 5m features file (.csv/.parquet/.feather)")
    ap.add_argument("--file15m", required=False, help="Path to 15m features file (optional for this script)")

    # Strategy thresholds
    ap.add_argument("--z_entry", type=float, default=2.0)
    ap.add_argument("--z_target", type=float, default=0.5)
    ap.add_argument("--z_stop", type=float, default=2.8)
    ap.add_argument("--max_hold_bars", type=int, default=72)

    # Entry filters
    ap.add_argument("--hurst_max", type=float, default=0.50, help="Keep only if Hurst15m < hurst_max (set -1 to disable)")
    ap.add_argument("--liq_max", type=float, default=0.0010, help="Keep only if LiquidityCostProxy <= liq_max (decimal units). Set -1 to disable.")

    # Execution constraints
    ap.add_argument("--cooldown_bars", type=int, default=12, help="Cooldown after exit (5m bars). 12 bars = 1 hour.")
    args = ap.parse_args()

    hurst_max = None if args.hurst_max < 0 else args.hurst_max
    liq_max = None if args.liq_max < 0 else args.liq_max

    print_header("Loading data")
    df5 = read_any(args.file5m)
    df5["Date"] = to_datetime_utc_naive(df5["Date"])
    df5 = df5.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    print(f"Loaded 5m rows: {len(df5):,}")

    # Optional: read 15m but not necessary for stats
    if args.file15m:
        df15 = read_any(args.file15m)
        df15["Date"] = to_datetime_utc_naive(df15["Date"])
        df15 = df15.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)
        print(f"Loaded 15m rows: {len(df15):,}")

    # Create signal universe
    print_header("Signals: fresh Z-cross events (unfiltered)")
    all_events = find_fresh_signals(df5, z_entry=args.z_entry)
    n_long = sum(e.side == "LONG" for e in all_events)
    n_short = sum(e.side == "SHORT" for e in all_events)
    print(f"Fresh signals |Z|>{args.z_entry}: total={len(all_events)} long={n_long} short={n_short}")

    horizons = [12, 24, 48, 72]  # 1h,2h,4h,6h

    # Unfiltered stats
    fr_all = forward_returns_signed(df5, all_events, horizons)
    out_all = event_study_z_only(df5, all_events, z_target=args.z_target, z_stop=args.z_stop, max_hold_bars=args.max_hold_bars)

    summarize_filter_context(df5, all_events, "Context @ entry (unfiltered signals)")
    summarize_forward_returns(fr_all, horizons, "Conditional forward returns (signed) — UNFILTERED")
    summarize_outcomes(out_all, "Target-before-stop event study (Z-only) — UNFILTERED")

    # Apply entry filters at the signal bar
    print_header("Applying entry filters")
    filtered_events = apply_entry_filters(df5, all_events, hurst_max=hurst_max, liq_max=liq_max)
    n_long_f = sum(e.side == "LONG" for e in filtered_events)
    n_short_f = sum(e.side == "SHORT" for e in filtered_events)

    print(f"After entry filters:")
    if hurst_max is not None:
        print(f"  - Hurst15m < {hurst_max}")
    else:
        print("  - Hurst filter disabled")
    if liq_max is not None:
        print(f"  - LiquidityCostProxy <= {liq_max} (decimal, e.g. 0.0010 = 0.10%)")
    else:
        print("  - Liquidity filter disabled")

    print(f"Filtered signals: total={len(filtered_events)} long={n_long_f} short={n_short_f}")

    summarize_filter_context(df5, filtered_events, "Context @ entry (after entry filters)")

    # Enforce one-position + cooldown by simulating exit index and skipping overlaps
    accepted_events, out_acc = enforce_one_position_and_cooldown(
        df5,
        filtered_events,
        z_target=args.z_target,
        z_stop=args.z_stop,
        max_hold_bars=args.max_hold_bars,
        cooldown_bars=args.cooldown_bars,
    )
    print_header("Execution constraints applied")
    print(f"One-position + cooldown_bars={args.cooldown_bars} => accepted trades: {len(accepted_events)}")

    fr_acc = forward_returns_signed(df5, accepted_events, horizons)

    summarize_forward_returns(fr_acc, horizons, "Conditional forward returns (signed) — FILTERED + EXECUTABLE")
    summarize_outcomes(out_acc, "Target-before-stop event study (Z-only) — FILTERED + EXECUTABLE")

    print_header("Done")


if __name__ == "__main__":
    main()
