#!/usr/bin/env python3
"""
Sanity checks + mean-reversion viability diagnostics for:
- 5m features dataset
- 15m Hurst dataset

Expected columns:
5m:  'Date','Open','High','Low','Close','Volume','FairValue','EWMAVol','ZScore','RangePct','LiquidityCostProxy','Hurst15m'
15m: 'Date','Open','High','Low','Close','Volume','Hurst15m'

Assumption: 5m Hurst15m uses previous 15m candle's Hurst (shifted to avoid lookahead).
"""

import argparse
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

import numpy as np
import pandas as pd


# -----------------------------
# Helpers
# -----------------------------
def read_any(path: str) -> pd.DataFrame:
    ext = os.path.splitext(path.lower())[1]
    if ext in [".parquet"]:
        return pd.read_parquet(path)
    if ext in [".csv"]:
        return pd.read_csv(path)
    if ext in [".feather"]:
        return pd.read_feather(path)
    raise ValueError(f"Unsupported file extension: {ext}. Use .csv or .parquet or .feather")


def to_datetime_utc_naive(s: pd.Series) -> pd.Series:
    # keep naive timestamps (no tz); if tz-aware, convert to UTC then drop tz
    dt = pd.to_datetime(s, errors="coerce", utc=True)
    return dt.dt.tz_convert(None)


def pct_scale_detector(x: pd.Series) -> str:
    """
    Detect whether a "percentage-like" column is in decimal (0.01 = 1%)
    or percent units (1.0 = 1%).
    Returns 'decimal' or 'percent'.
    """
    v = x.replace([np.inf, -np.inf], np.nan).dropna()
    if len(v) == 0:
        return "decimal"
    med = float(np.nanmedian(np.abs(v)))
    # Heuristic:
    # - If median > 0.5, it's probably in percent units (e.g., 0.8 means 0.8%)
    # - If median < 0.2, it's probably decimal (e.g., 0.008 means 0.8%)
    return "percent" if med > 0.5 else "decimal"


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


def warn(msg: str):
    print(f"[WARN] {msg}")


def ok(msg: str):
    print(f"[OK]   {msg}")


def fail(msg: str):
    print(f"[FAIL] {msg}")


# -----------------------------
# Integrity checks
# -----------------------------
def check_schema(df: pd.DataFrame, required: List[str], name: str) -> None:
    missing = [c for c in required if c not in df.columns]
    extra = [c for c in df.columns if c not in required]
    if missing:
        fail(f"{name}: missing required columns: {missing}")
    else:
        ok(f"{name}: has all required columns ({len(required)})")
    if extra:
        warn(f"{name}: extra columns (ignored by checks): {extra}")


def check_time_index(df: pd.DataFrame, name: str, expected_minutes: int) -> pd.DataFrame:
    if "Date" not in df.columns:
        fail(f"{name}: no Date column; cannot run time checks")
        return df

    df = df.copy()
    df["Date"] = to_datetime_utc_naive(df["Date"])

    n_bad = df["Date"].isna().sum()
    if n_bad > 0:
        fail(f"{name}: {n_bad} rows have invalid Date parse")

    df = df.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    # duplicates
    dup = df["Date"].duplicated().sum()
    if dup > 0:
        warn(f"{name}: {dup} duplicate timestamps found")

    # spacing
    deltas = df["Date"].diff().dropna().dt.total_seconds().values
    if len(deltas) > 0:
        exp = expected_minutes * 60
        # count gaps / irregular
        irregular = np.sum(deltas != exp)
        if irregular > 0:
            # report top delta counts
            vals, cnts = np.unique(deltas, return_counts=True)
            top = sorted(zip(cnts, vals), reverse=True)[:8]
            warn(f"{name}: irregular spacing detected. Most common deltas (count, seconds): {top}")
            gaps = np.sum(deltas > exp)
            if gaps > 0:
                warn(f"{name}: {gaps} gaps where delta > expected ({expected_minutes}m)")
        else:
            ok(f"{name}: spacing is perfectly regular at {expected_minutes}m")

    return df


def check_ohlcv(df: pd.DataFrame, name: str) -> None:
    need = ["Open", "High", "Low", "Close", "Volume"]
    if any(c not in df.columns for c in need):
        warn(f"{name}: missing OHLCV columns; skipping OHLC checks")
        return

    o = df["Open"].astype(float)
    h = df["High"].astype(float)
    l = df["Low"].astype(float)
    c = df["Close"].astype(float)
    v = df["Volume"].astype(float)

    bad1 = ((h < o) | (h < c) | (l > o) | (l > c) | (h < l)).sum()
    if bad1 > 0:
        fail(f"{name}: {bad1} rows violate OHLC bounds (High/Low inconsistent)")
    else:
        ok(f"{name}: OHLC bounds look consistent")

    badv = (v < 0).sum()
    if badv > 0:
        fail(f"{name}: {badv} rows have negative volume")
    else:
        ok(f"{name}: volume is non-negative")


def check_nans_infs(df: pd.DataFrame, name: str, cols: Optional[List[str]] = None) -> None:
    if cols is None:
        cols = [c for c in df.columns if c != "Date"]
    sub = df[cols].copy()
    # coerce numeric where possible
    for c in cols:
        if c == "Date":
            continue
        sub[c] = pd.to_numeric(sub[c], errors="coerce")

    n_nan = sub.isna().sum().sum()
    n_inf = np.isinf(sub.to_numpy(dtype=float, copy=False)).sum()
    if n_nan > 0:
        warn(f"{name}: total NaNs across numeric columns = {int(n_nan)}")
    else:
        ok(f"{name}: no NaNs in numeric columns (after coercion)")

    if n_inf > 0:
        warn(f"{name}: total inf values across numeric columns = {int(n_inf)}")
    else:
        ok(f"{name}: no inf values in numeric columns")


# -----------------------------
# Feature sanity checks (5m)
# -----------------------------
def check_rangepct(df5: pd.DataFrame) -> Dict[str, float]:
    """
    Check if RangePct matches (High-Low)/Close (decimal or percent scale).
    Returns dict with mismatch stats.
    """
    if not set(["High", "Low", "Close", "RangePct"]).issubset(df5.columns):
        warn("5m: missing RangePct or OHLC; skipping RangePct checks")
        return {}

    rp = pd.to_numeric(df5["RangePct"], errors="coerce")
    h = pd.to_numeric(df5["High"], errors="coerce")
    l = pd.to_numeric(df5["Low"], errors="coerce")
    c = pd.to_numeric(df5["Close"], errors="coerce")

    raw = (h - l) / c
    scale = pct_scale_detector(rp)

    rp_std = rp / 100.0 if scale == "percent" else rp

    err = (rp_std - raw).abs()
    out = {
        "scale_detected": 1.0 if scale == "percent" else 0.0,
        "median_abs_err": float(np.nanmedian(err)),
        "p95_abs_err": float(np.nanpercentile(err.dropna(), 95)) if err.notna().any() else np.nan,
        "mean_abs_err": float(np.nanmean(err)),
    }

    print_header("5m Feature Check: RangePct")
    print(f"Detected RangePct scale: {scale} (internally standardized to decimal)")
    print(f"Median |RangePct - (H-L)/C|  = {fmt(out['median_abs_err'])}")
    print(f"P95    |RangePct - (H-L)/C|  = {fmt(out['p95_abs_err'])}")

    # tolerance: depends on rounding; 1e-5 (~0.1bp) is pretty strict
    if out["p95_abs_err"] < 5e-4:
        ok("RangePct appears consistent with (High-Low)/Close")
    else:
        warn("RangePct mismatch is large; check your feature computation or units")

    return {"range_scale": scale, **out}


def check_liquidity_proxy(df5: pd.DataFrame, range_scale: str) -> None:
    """
    Check LiquidityCostProxy matches max(floor, k*RangePct) with scale aware.
    We use the exact version we inserted earlier:
        liquidity_cost_proxy = max(0.02%, 0.10 * range_pct)
    with everything in DECIMAL units.
    """
    if not set(["LiquidityCostProxy", "RangePct"]).issubset(df5.columns):
        warn("5m: missing LiquidityCostProxy or RangePct; skipping LiquidityCostProxy checks")
        return

    lp = pd.to_numeric(df5["LiquidityCostProxy"], errors="coerce")
    rp = pd.to_numeric(df5["RangePct"], errors="coerce")
    lp_scale = pct_scale_detector(lp)

    rp_dec = rp / 100.0 if range_scale == "percent" else rp
    lp_dec = lp / 100.0 if lp_scale == "percent" else lp

    floor = 0.0002   # 0.02% in decimal
    k = 0.10
    expected = np.maximum(floor, k * rp_dec)

    err = (lp_dec - expected).abs()

    print_header("5m Feature Check: LiquidityCostProxy")
    print(f"Detected LiquidityCostProxy scale: {lp_scale} (internally standardized to decimal)")
    print(f"Median |LP - max(0.0002, 0.10*RangePct)| = {fmt(float(np.nanmedian(err)))}")
    print(f"P95    |LP - max(0.0002, 0.10*RangePct)| = {fmt(float(np.nanpercentile(err.dropna(), 95)) if err.notna().any() else np.nan)}")

    if err.notna().any() and float(np.nanpercentile(err.dropna(), 95)) < 5e-4:
        ok("LiquidityCostProxy appears consistent with the OHLC-based proxy formula")
    else:
        warn("LiquidityCostProxy does not match the proxy formula closely; check units or formula (floor/k) used")


def check_kalman_ewma_zscore_consistency(df5: pd.DataFrame) -> None:
    """
    We don't know if EWMAVol is return-vol or price-vol.
    We test both hypotheses and report which matches ZScore better.
    """
    req = ["Close", "FairValue", "EWMAVol", "ZScore"]
    if not set(req).issubset(df5.columns):
        warn("5m: missing one of Close/FairValue/EWMAVol/ZScore; skipping ZScore consistency check")
        return

    close = pd.to_numeric(df5["Close"], errors="coerce")
    fv = pd.to_numeric(df5["FairValue"], errors="coerce")
    vol = pd.to_numeric(df5["EWMAVol"], errors="coerce")
    z = pd.to_numeric(df5["ZScore"], errors="coerce")

    # Hypothesis A: EWMAVol already in PRICE units (sigma_price)
    z_a = (close - fv) / vol.replace(0, np.nan)

    # Hypothesis B: EWMAVol is RETURN vol (sigma_return); convert to price vol by * close
    z_b = (close - fv) / (vol * close).replace(0, np.nan)

    # Correlations (robust) and residual scale
    def corr(a, b):
        m = np.isfinite(a) & np.isfinite(b)
        if m.sum() < 50:
            return np.nan
        return float(np.corrcoef(a[m], b[m])[0, 1])

    ca = corr(z, z_a)
    cb = corr(z, z_b)

    # median absolute residuals
    def med_abs(a, b):
        m = np.isfinite(a) & np.isfinite(b)
        if m.sum() < 50:
            return np.nan
        return float(np.nanmedian(np.abs(a[m] - b[m])))

    ra = med_abs(z, z_a)
    rb = med_abs(z, z_b)

    print_header("5m Feature Check: ZScore self-consistency")
    print(f"Corr(ZScore, (Close-FV)/EWMAVol)                = {fmt(ca)} ; median abs residual = {fmt(ra)}")
    print(f"Corr(ZScore, (Close-FV)/(EWMAVol*Close))        = {fmt(cb)} ; median abs residual = {fmt(rb)}")

    if np.nan_to_num(ca) > np.nan_to_num(cb):
        ok("ZScore is more consistent with EWMAVol in PRICE units (sigma_price).")
    else:
        ok("ZScore is more consistent with EWMAVol as RETURN vol (sigma_return), converted via *Close.")

    # basic feature sanity
    if (vol <= 0).sum() > 0:
        warn("EWMAVol has non-positive values; volatility should be strictly positive after warmup")
    else:
        ok("EWMAVol is positive (post coercion, including warmup rows)")

    # FairValue should be “close-ish” but smoother (not a strict test)
    dev = (close - fv) / close
    if dev.replace([np.inf, -np.inf], np.nan).abs().quantile(0.99) > 0.10:
        warn("FairValue deviates >10% from Close at the 99th percentile — check Kalman parameters or computation")
    else:
        ok("FairValue stays reasonably near Close (heuristic check)")


# -----------------------------
# Hurst no-lookahead checks
# -----------------------------
def check_hurst_piecewise_constant(df5: pd.DataFrame) -> None:
    """
    Within each 15m bucket (3 consecutive 5m bars), the 5m Hurst15m should be constant
    if you forward-filled the (previous) 15m Hurst value.
    """
    if not set(["Date", "Hurst15m"]).issubset(df5.columns):
        warn("5m: missing Date or Hurst15m; skipping piecewise-constant check")
        return

    tmp = df5[["Date", "Hurst15m"]].copy()
    tmp["Date"] = to_datetime_utc_naive(tmp["Date"])
    tmp = tmp.dropna(subset=["Date"]).sort_values("Date")
    tmp["bucket15"] = tmp["Date"].dt.floor("15min")

    # within each bucket, count unique hurst values
    nunq = tmp.groupby("bucket15")["Hurst15m"].nunique(dropna=False)
    bad = (nunq > 1).sum()

    print_header("No-lookahead Check: 5m Hurst15m piecewise constancy")
    print(f"15m buckets checked: {len(nunq)}")
    print(f"Buckets where Hurst15m changes within the 3x 5m bars: {int(bad)}")

    if bad == 0:
        ok("Hurst15m is constant within each 15m bucket (expected for 5m using 15m regime).")
    else:
        warn("Hurst15m changes inside some 15m buckets — verify how you align/merge Hurst into 5m.")


def check_hurst_shift_matches_15m(df5: pd.DataFrame, df15: pd.DataFrame) -> None:
    """
    Verify 5m Hurst15m equals PREVIOUS 15m candle's Hurst:
    For each 5m bar at time t:
      bucket = floor(t to 15m)
      expected = hurst15m_15m[bucket - 15m]
    """
    need5 = ["Date", "Hurst15m"]
    need15 = ["Date", "Hurst15m"]
    if not set(need5).issubset(df5.columns) or not set(need15).issubset(df15.columns):
        warn("Missing Date/Hurst15m in one dataset; skipping 5m vs 15m shift check")
        return

    a = df5[["Date", "Hurst15m"]].copy()
    b = df15[["Date", "Hurst15m"]].copy()
    a["Date"] = to_datetime_utc_naive(a["Date"])
    b["Date"] = to_datetime_utc_naive(b["Date"])
    a = a.dropna(subset=["Date"]).sort_values("Date")
    b = b.dropna(subset=["Date"]).sort_values("Date")

    # Create 15m buckets for 15m DF (should already be on 15m boundaries)
    b["bucket15"] = b["Date"].dt.floor("15min")
    b = b.drop_duplicates("bucket15").set_index("bucket15")["Hurst15m"].sort_index()

    # Map each 5m bar to its 15m bucket and then shift by one bucket backward
    a["bucket15"] = a["Date"].dt.floor("15min")
    a["expected"] = a["bucket15"].map(lambda x: b.get(x - pd.Timedelta(minutes=15), np.nan))

    # Compare where expected exists
    m = a["expected"].notna() & a["Hurst15m"].notna()
    if m.sum() < 50:
        warn("Not enough overlap to check 15m shift alignment (need >= 50 comparable rows).")
        return

    diff = (pd.to_numeric(a.loc[m, "Hurst15m"], errors="coerce") - pd.to_numeric(a.loc[m, "expected"], errors="coerce")).abs()
    # tolerance (hurst estimates can have floating rounding)
    p95 = float(np.nanpercentile(diff, 95))
    exact_match_rate = float((diff < 1e-9).mean())

    print_header("No-lookahead Check: 5m Hurst15m == previous 15m Hurst")
    print(f"Comparable 5m rows: {int(m.sum())}")
    print(f"Exact match rate:   {fmt(exact_match_rate)}")
    print(f"P95 abs difference: {fmt(p95)}")

    if p95 < 1e-6:
        ok("5m Hurst15m matches previous 15m candle's Hurst (shifted correctly).")
    else:
        warn("5m Hurst15m does NOT match the previous 15m Hurst cleanly — verify the shift/fill logic.")


# -----------------------------
# Mean reversion viability checks
# -----------------------------
@dataclass
class SignalEvent:
    idx: int
    ts: pd.Timestamp
    side: str  # 'LONG' or 'SHORT'


def compute_returns(df5: pd.DataFrame) -> pd.Series:
    close = pd.to_numeric(df5["Close"], errors="coerce")
    return np.log(close / close.shift(1))


def find_fresh_signals(df5: pd.DataFrame, z_entry: float = 2.0) -> List[SignalEvent]:
    z = pd.to_numeric(df5["ZScore"], errors="coerce")
    t = df5["Date"]

    long_mask = (z < -z_entry) & (z.shift(1) >= -z_entry)
    short_mask = (z > z_entry) & (z.shift(1) <= z_entry)

    events = []
    for idx in np.where(long_mask.fillna(False).to_numpy())[0]:
        events.append(SignalEvent(idx=idx, ts=t.iloc[idx], side="LONG"))
    for idx in np.where(short_mask.fillna(False).to_numpy())[0]:
        events.append(SignalEvent(idx=idx, ts=t.iloc[idx], side="SHORT"))

    events.sort(key=lambda e: e.idx)
    return events


def event_forward_returns(df5: pd.DataFrame, events: List[SignalEvent], horizons: List[int]) -> pd.DataFrame:
    """
    Compute forward log returns from event idx to idx+h.
    For LONG signals: we report raw forward return (expect positive).
    For SHORT signals: we report signed forward return (negative return is good, so we multiply by -1).
    """
    r = compute_returns(df5)
    close = pd.to_numeric(df5["Close"], errors="coerce")

    rows = []
    for ev in events:
        base = close.iloc[ev.idx]
        if not np.isfinite(base):
            continue
        row = {"Date": ev.ts, "Side": ev.side, "Idx": ev.idx}
        for h in horizons:
            j = ev.idx + h
            if j >= len(close):
                row[f"fwd_{h}"] = np.nan
                continue
            ret = np.log(close.iloc[j] / base)
            # "goodness" sign
            signed = ret if ev.side == "LONG" else -ret
            row[f"fwd_{h}"] = signed
        rows.append(row)

    return pd.DataFrame(rows)


def simulate_strategy_style_outcome(df5: pd.DataFrame,
                                    events: List[SignalEvent],
                                    z_target: float = 0.5,
                                    z_stop: float = 2.8,
                                    max_hold_bars: int = 72) -> pd.DataFrame:
    """
    For each fresh signal, look forward up to max_hold_bars and check:
    - did we hit target before stop?
    This is a pure ZScore-path event study (no execution / fills), but matches your logic.
    """
    z = pd.to_numeric(df5["ZScore"], errors="coerce").to_numpy()
    dates = df5["Date"].to_numpy()

    out = []
    for ev in events:
        i = ev.idx
        end = min(i + max_hold_bars, len(z) - 1)
        path = z[i+1:end+1]  # after entry bar

        hit_target = False
        hit_stop = False
        hit_time = None
        reason = "TIME"

        if ev.side == "LONG":
            # target: z >= +0.5 ; stop: z <= -2.8
            for k, zz in enumerate(path, start=1):
                if not np.isfinite(zz):
                    continue
                if zz <= -z_stop:
                    hit_stop = True
                    hit_time = k
                    reason = "STOP"
                    break
                if zz >= z_target:
                    hit_target = True
                    hit_time = k
                    reason = "TARGET"
                    break
        else:
            # SHORT: target z <= -0.5 ; stop z >= +2.8
            for k, zz in enumerate(path, start=1):
                if not np.isfinite(zz):
                    continue
                if zz >= z_stop:
                    hit_stop = True
                    hit_time = k
                    reason = "STOP"
                    break
                if zz <= -z_target:
                    hit_target = True
                    hit_time = k
                    reason = "TARGET"
                    break

        out.append({
            "Date": pd.Timestamp(dates[i]),
            "Side": ev.side,
            "Idx": i,
            "Outcome": reason,
            "BarsToOutcome": hit_time if hit_time is not None else max_hold_bars
        })

    return pd.DataFrame(out)


def ar1_half_life(x: pd.Series) -> Tuple[float, float]:
    """
    Fit AR(1): x_t = a + b x_{t-1} + e
    Return (b, half_life_in_bars). Half-life defined when 0 < b < 1:
        half_life = -ln(2)/ln(b)
    """
    x = pd.to_numeric(x, errors="coerce").replace([np.inf, -np.inf], np.nan).dropna()
    if len(x) < 200:
        return np.nan, np.nan

    x0 = x.shift(1).dropna()
    x1 = x.loc[x0.index]

    # OLS for b with intercept
    X = np.column_stack([np.ones(len(x0)), x0.to_numpy()])
    y = x1.to_numpy()
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    b = float(beta[1])

    if b <= 0 or b >= 1:
        hl = np.nan
    else:
        hl = float(-np.log(2.0) / np.log(b))
    return b, hl


def autocorr(series: pd.Series, max_lag: int = 12) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce").replace([np.inf, -np.inf], np.nan).dropna()
    if len(s) < 200:
        return pd.Series(dtype=float)
    out = {}
    arr = s.to_numpy()
    arr = arr - np.mean(arr)
    denom = np.dot(arr, arr)
    for lag in range(1, max_lag + 1):
        num = np.dot(arr[lag:], arr[:-lag])
        out[lag] = float(num / denom) if denom != 0 else np.nan
    return pd.Series(out)


def hurst_summary(df5: pd.DataFrame) -> None:
    if "Hurst15m" not in df5.columns:
        return
    h = pd.to_numeric(df5["Hurst15m"], errors="coerce").dropna()
    if len(h) < 100:
        warn("Not enough Hurst15m values for distribution summary.")
        return

    print_header("Mean Reversion Viability: Hurst distribution (from 5m dataset)")
    qs = h.quantile([0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99]).to_dict()
    for k, v in qs.items():
        print(f"Quantile {k:>4}: {fmt(float(v))}")

    share_lt_05 = float((h < 0.50).mean())
    share_lt_045 = float((h < 0.45).mean())
    share_ge_055 = float((h >= 0.55).mean())
    print(f"\nShare H < 0.50  (good for MR): {fmt(share_lt_05)}")
    print(f"Share H < 0.45  (strong MR):  {fmt(share_lt_045)}")
    print(f"Share H >= 0.55 (trendy):     {fmt(share_ge_055)}")


def mean_reversion_viability(df5: pd.DataFrame,
                             z_entry: float = 2.0,
                             z_target: float = 0.5,
                             z_stop: float = 2.8,
                             max_hold_bars: int = 72) -> None:
    if not set(["Date", "Close", "ZScore", "FairValue"]).issubset(df5.columns):
        warn("5m: missing required columns for MR viability checks")
        return

    # Z sanity
    z = pd.to_numeric(df5["ZScore"], errors="coerce")
    print_header("Mean Reversion Viability: ZScore distribution & signal frequency")
    print(f"Z mean  = {fmt(float(z.mean()))}")
    print(f"Z std   = {fmt(float(z.std()))}")
    print(f"Z p01   = {fmt(float(z.quantile(0.01)))}")
    print(f"Z p05   = {fmt(float(z.quantile(0.05)))}")
    print(f"Z p50   = {fmt(float(z.quantile(0.50)))}")
    print(f"Z p95   = {fmt(float(z.quantile(0.95)))}")
    print(f"Z p99   = {fmt(float(z.quantile(0.99)))}")

    events = find_fresh_signals(df5, z_entry=z_entry)
    n_long = sum(e.side == "LONG" for e in events)
    n_short = sum(e.side == "SHORT" for e in events)
    print(f"\nFresh signals (crossing |Z|>{z_entry}): total={len(events)} long={n_long} short={n_short}")

    # forward return study
    horizons = [12, 24, 48, 72]  # 1h,2h,4h,6h
    fr = event_forward_returns(df5, events, horizons=horizons)
    if len(fr) == 0:
        warn("No events found for forward-return analysis.")
    else:
        print_header("Mean Reversion Viability: Conditional forward returns (signed)")
        # signed means "good direction is positive" for both long and short
        for h in horizons:
            col = f"fwd_{h}"
            vals = fr[col].dropna()
            if len(vals) < 20:
                warn(f"Not enough samples for horizon {h} bars.")
                continue
            print(f"Horizon {h:>2} bars: mean={fmt(float(vals.mean()))}  median={fmt(float(vals.median()))}  hit_rate(>0)={fmt(float((vals>0).mean()))}")

    # strategy-style outcome (target before stop within max_hold)
    outcomes = simulate_strategy_style_outcome(df5, events, z_target=z_target, z_stop=z_stop, max_hold_bars=max_hold_bars)
    if len(outcomes) > 0:
        print_header("Mean Reversion Viability: Target-before-stop event study (Z-only)")
        counts = outcomes["Outcome"].value_counts(dropna=False).to_dict()
        total = len(outcomes)
        for k, v in counts.items():
            print(f"{k:>6}: {v} ({v/total:.2%})")
        # average time-to-outcome
        print(f"\nAvg BarsToOutcome (all):   {fmt(float(outcomes['BarsToOutcome'].mean()))}")
        print(f"Avg BarsToOutcome (TARGET): {fmt(float(outcomes.loc[outcomes['Outcome']=='TARGET','BarsToOutcome'].mean()))}")

    # OU/AR1 half-life on deviation series
    dev = pd.to_numeric(df5["Close"], errors="coerce") - pd.to_numeric(df5["FairValue"], errors="coerce")
    b, hl = ar1_half_life(dev)
    print_header("Mean Reversion Viability: OU/AR(1) half-life on (Close - FairValue)")
    print(f"AR(1) b coefficient: {fmt(b)}")
    if np.isfinite(hl):
        print(f"Half-life (bars):    {fmt(hl)}  (~{fmt(hl*5/60)} hours at 5m bars)")
        ok("Half-life is defined (0<b<1). Smaller is faster mean reversion.")
    else:
        warn("Half-life undefined (b not in (0,1)). MR may be weak/unstable or dev series not OU-like.")

    # autocorr
    r = compute_returns(df5)
    ac_r = autocorr(r, max_lag=12)
    ac_z = autocorr(z, max_lag=12)
    print_header("Diagnostics: autocorrelation (lags 1..12)")
    if len(ac_r) > 0:
        print("Return autocorr:")
        for lag, val in ac_r.items():
            print(f"  lag {lag:>2}: {fmt(val)}")
    else:
        warn("Not enough data for return autocorr.")

    if len(ac_z) > 0:
        print("\nZScore autocorr:")
        for lag, val in ac_z.items():
            print(f"  lag {lag:>2}: {fmt(val)}")
    else:
        warn("Not enough data for Z autocorr.")

    # Hurst distribution
    hurst_summary(df5)


# -----------------------------
# Main
# -----------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file5m", required=True, help="Path to 5m features file (.csv/.parquet/.feather)")
    ap.add_argument("--file15m", required=True, help="Path to 15m features file (.csv/.parquet/.feather)")
    ap.add_argument("--z_entry", type=float, default=2.0)
    ap.add_argument("--z_target", type=float, default=0.5)
    ap.add_argument("--z_stop", type=float, default=2.8)
    ap.add_argument("--max_hold_bars", type=int, default=72)
    args = ap.parse_args()

    print_header("Loading data")
    df5 = read_any(args.file5m)
    df15 = read_any(args.file15m)
    print(f"Loaded 5m rows:  {len(df5):,}")
    print(f"Loaded 15m rows: {len(df15):,}")

    # Required schemas
    req5 = ['Date','Open','High','Low','Close','Volume','FairValue','EWMAVol','ZScore','RangePct','LiquidityCostProxy','Hurst15m']
    req15 = ['Date','Open','High','Low','Close','Volume','Hurst15m']

    print_header("Schema checks")
    check_schema(df5, req5, "5m")
    check_schema(df15, req15, "15m")

    # Time + OHLC
    print_header("Time index integrity")
    df5 = check_time_index(df5, "5m", expected_minutes=5)
    df15 = check_time_index(df15, "15m", expected_minutes=15)

    print_header("OHLCV integrity")
    check_ohlcv(df5, "5m")
    check_ohlcv(df15, "15m")

    print_header("NaN/Inf scan")
    check_nans_infs(df5, "5m", cols=[c for c in req5 if c in df5.columns])
    check_nans_infs(df15, "15m", cols=[c for c in req15 if c in df15.columns])

    # Feature checks 5m
    range_info = check_rangepct(df5)
    range_scale = range_info.get("range_scale", "decimal")
    check_liquidity_proxy(df5, range_scale=range_scale)
    check_kalman_ewma_zscore_consistency(df5)

    # Hurst alignment checks
    check_hurst_piecewise_constant(df5)
    check_hurst_shift_matches_15m(df5, df15)

    # Mean reversion viability checks
    mean_reversion_viability(df5,
                             z_entry=args.z_entry,
                             z_target=args.z_target,
                             z_stop=args.z_stop,
                             max_hold_bars=args.max_hold_bars)

    print_header("Done")


if __name__ == "__main__":
    main()
