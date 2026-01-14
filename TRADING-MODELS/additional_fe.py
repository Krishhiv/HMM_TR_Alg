#!/usr/bin/env python3
# ------------------------------------------------------------
# add_prime_features.py
#
# Adds the extra features required for the PRIME strategy to an
# already feature-engineered 1h dataset (no positions, no signals).
#
# HOW TO USE:
#   1) Set IN_CSV and OUT_CSV below.
#   2) python add_prime_features.py
#
# REQUIRED existing columns in your CSV (case-sensitive):
#   Date, Open, High, Low, Close, Volume,
#   MR_ema20, MR_atr14, MR_bb_mid, MR_bb_up, MR_bb_dn,
#   MOM_ema50, MOM_ema200, MOM_ema50_slope,
#   MOM_donchian20_up,
#   D1_State_same_day, D1_State_lag1d
# (Other columns can be present; they’re left unchanged.)
#
# NEW columns created:
#   BBW, KC_up, KC_dn, SQZ, RECENT_SQZ, BBW_MED20, EXPANDING,
#   R2_ema50, ADX14,
#   S_VNB, DIST_up_ATR
#
# Notes:
# - Timestamps are parsed from 'Date'. If tz-aware, converted to UTC and tz dropped.
# - Warmup NaNs are expected at the top for rolling metrics.
# ------------------------------------------------------------

import os
import numpy as np
import pandas as pd

# ================== EDIT THESE PATHS ==================
IN_CSV  = "./outputs/btc_1h_features_merged.csv"   # path to your existing 1h features CSV
OUT_CSV = "./TRADING-MODELS/btc_1h_features_PRIME.csv"  # where to save the augmented file
# ======================================================


# ---------- helpers ----------
def parse_date_index(df: pd.DataFrame, date_col: str = "Date") -> pd.DataFrame:
    if date_col not in df.columns:
        raise ValueError("CSV must include a 'Date' column.")
    dt = pd.to_datetime(df[date_col], errors="coerce", utc=True)
    # If your 'Date' was naive, the line above treats it as UTC; good for crypto.
    # If it was tz-aware, it's now converted to UTC.
    df = df.drop(columns=[date_col]).set_index(dt).sort_index()
    return df

def rolling_r2(series: pd.Series, window: int) -> pd.Series:
    """
    Rolling OLS R^2 of 'series' against time index over a fixed window.
    """
    x = np.arange(window)
    def _r2(y_vals: np.ndarray) -> float:
        y = y_vals
        # X = [1, centered_time]
        X = np.vstack([np.ones(window), x - x.mean()]).T
        try:
            beta = np.linalg.lstsq(X, y, rcond=None)[0]
            yhat = X @ beta
            ssr = ((yhat - y.mean())**2).sum()
            sst = ((y - y.mean())**2).sum()
            return 0.0 if sst == 0 else float(ssr / sst)
        except Exception:
            return np.nan
    return series.rolling(window, min_periods=window).apply(_r2, raw=True)

def compute_adx14(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14) -> pd.Series:
    up_move   = (high - high.shift(1)).clip(lower=0)
    down_move = (low.shift(1) - low).clip(lower=0)
    plus_dm   = up_move.where(up_move > down_move, 0.0)
    minus_dm  = down_move.where(down_move > up_move, 0.0)

    tr = pd.concat([
        (high - low),
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs()
    ], axis=1).max(axis=1)

    atr = tr.ewm(alpha=1/n, adjust=False).mean()
    plus_di  = 100 * (plus_dm.ewm(alpha=1/n, adjust=False).mean() / atr.replace(0, np.nan))
    minus_di = 100 * (minus_dm.ewm(alpha=1/n, adjust=False).mean() / atr.replace(0, np.nan))
    dx = ((plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)) * 100
    adx = dx.ewm(alpha=1/n, adjust=False).mean()
    return adx

def check_required(df: pd.DataFrame, cols: list):
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def main():
    # Load
    df = pd.read_csv(IN_CSV)
    df = parse_date_index(df, "Date")

    # --- sanity: required inputs
    required = [
        "Open","High","Low","Close","Volume",
        "MR_ema20","MR_atr14","MR_bb_mid","MR_bb_up","MR_bb_dn",
        "MOM_ema50","MOM_ema200","MOM_ema50_slope",
        "MOM_donchian20_up",
        "D1_State_same_day","D1_State_lag1d",
    ]
    check_required(df, required)

    # ================= PRIME feature block =================

    # 1) Squeeze & expansion
    df["BBW"] = (df["MR_bb_up"] - df["MR_bb_dn"]) / df["MR_bb_mid"].replace(0, np.nan)
    df["KC_up"] = df["MR_ema20"] + 1.5 * df["MR_atr14"]
    df["KC_dn"] = df["MR_ema20"] - 1.5 * df["MR_atr14"]
    df["SQZ"] = (df["MR_bb_up"] < df["KC_up"]) & (df["MR_bb_dn"] > df["KC_dn"])

    L = 24  # lookback for "recent squeeze"
    df["RECENT_SQZ"] = df["SQZ"].rolling(L, min_periods=1).max().astype(bool)

    df["BBW_MED20"] = df["BBW"].rolling(20, min_periods=20).median()
    # expansion: BBW above its median and rising vs 3 bars ago
    df["EXPANDING"] = (df["BBW"] > df["BBW_MED20"]) & (df["BBW"] - df["BBW"].shift(3) > 0)

    # 2) Trend quality: R^2 of EMA50 and ADX14
    df["R2_ema50"] = rolling_r2(df["MOM_ema50"], window=72)  # ~3 days on 1h bars
    df["ADX14"] = compute_adx14(df["High"], df["Low"], df["Close"], n=14)

    # 3) Micro-breakout strength (vol-normalized Donchian)
    df["S_VNB"] = (df["Close"] - df["MOM_donchian20_up"]) / df["MR_atr14"].replace(0, np.nan)
    df["DIST_up_ATR"] = df["S_VNB"]  # convenience alias for later models

    # =======================================================

    # Save with 'Date' column first
    out = df.copy()
    date_col = out.index
    # If tz-aware, convert to UTC and drop tz to keep CSV clean
    if getattr(date_col, "tz", None) is not None:
        date_col = date_col.tz_convert("UTC").tz_localize(None)
    out.insert(0, "Date", pd.to_datetime(date_col))
    # Ensure output directory exists if you changed OUT_CSV to a new folder
    out.to_csv(OUT_CSV, index=False)

    # Summary
    na_ratios = out.isna().mean().sort_values(ascending=False)
    print(f"Saved: {OUT_CSV}")
    print("Top 10 NaN ratios (warmup expected):")
    print(na_ratios.head(10).round(4))


if __name__ == "__main__":
    main()
