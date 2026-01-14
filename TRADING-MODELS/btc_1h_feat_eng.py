#!/usr/bin/env python3
# ------------------------------------------------------------
# build_1h_features_and_merge_state.py  (no argparse)
#
# Inputs:
#   1h OHLCV  : ./data_coinbase_btc/btc_1h.csv
#   1d states : ./outputs/btc_1d_with_states_compact.csv
#
# Output:
#   ./outputs/btc_1h_features_merged.csv
#
# What it does:
#   • Builds 1h features for:
#       - Mean Reversion (MR): EMA20, ATR14, z vs EMA, Bollinger (+%B), RSI14
#       - Momentum (MOM): EMA50/EMA200, EMA50 slope, Donchian(20), 24h ROC
#       - Local Vol BB (LVBB): local log-vol(48), EMA48, price-space sigma
#   • Merges daily HMM state into 1h:
#       - D1_State_same_day   : state for that calendar day (UTC)
#       - D1_State_lag1d      : state lagged by 1 day (use this for trading to avoid lookahead)
#
# Notes:
#   • No positions or backtesting here.
#   • All times coerced to UTC; warmup NaNs are expected for indicators.
# ------------------------------------------------------------

from pathlib import Path
import numpy as np
import pandas as pd


# ====== PATHS (edit if needed) ======
IN_CSV_1H   = "./data_coinbase_btc/btc_1h.csv"
IN_CSV_1D   = "./outputs/btc_1d_with_states_compact.csv"
OUT_CSV     = "./outputs/btc_1h_features_merged.csv"
# ====================================


# ---------- helpers ----------
def to_utc_index(df, date_col="Date"):
    if date_col in df.columns:
        idx = pd.to_datetime(df[date_col], utc=True, errors="coerce")
        df = df.set_index(idx).drop(columns=[date_col])
    else:
        df.index = pd.to_datetime(df.index, utc=True, errors="coerce")
    return df.sort_index()


def true_range(h, l, c_prev):
    hl = h - l
    hc = (h - c_prev).abs()
    lc = (l - c_prev).abs()
    return pd.concat([hl, hc, lc], axis=1).max(axis=1)


def atr(high, low, close, n=14):
    c_prev = close.shift(1)
    tr = true_range(high, low, c_prev)
    return tr.ewm(alpha=1.0/n, adjust=False).mean()  # Wilder


def rsi_wilder(close, n=14):
    diff = close.diff()
    up = diff.clip(lower=0.0)
    dn = -diff.clip(upper=0.0)
    avg_gain = up.ewm(alpha=1.0/n, adjust=False).mean()
    avg_loss = dn.ewm(alpha=1.0/n, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + rs))


def rolling_log_vol(close, n=48):
    logp = np.log(close)
    lr = logp.diff()
    return lr.rolling(n, min_periods=n).std()


def donchian(high, low, n=20):
    up = high.rolling(n, min_periods=n).max()
    dn = low.rolling(n, min_periods=n).min()
    rng = up - dn
    return up, dn, rng


def build_features_1h(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = df_raw.copy()
    for c in ["Open", "High", "Low", "Close", "Volume"]:
        if c not in df.columns:
            raise ValueError(f"Missing required column: {c}")

    # ----- MR -----
    df["MR_ema20"] = df["Close"].ewm(span=20, adjust=False).mean()
    df["MR_atr14"] = atr(df["High"], df["Low"], df["Close"], n=14)
    scale = df["MR_atr14"].replace(0, np.nan)
    df["MR_z_ema20_atr"] = (df["Close"] - df["MR_ema20"]) / scale

    sma20 = df["Close"].rolling(20, min_periods=20).mean()
    std20 = df["Close"].rolling(20, min_periods=20).std()
    df["MR_bb_mid"] = sma20
    df["MR_bb_std"] = std20
    df["MR_bb_up"]  = sma20 + 2.0 * std20
    df["MR_bb_dn"]  = sma20 - 2.0 * std20
    df["MR_bb_pctB"] = (df["Close"] - df["MR_bb_dn"]) / (df["MR_bb_up"] - df["MR_bb_dn"])

    df["MR_rsi14"] = rsi_wilder(df["Close"], n=14)

    # ----- MOM -----
    df["MOM_ema50"] = df["Close"].ewm(span=50, adjust=False).mean()
    df["MOM_ema200"] = df["Close"].ewm(span=200, adjust=False).mean()
    df["MOM_ema50_slope"] = df["MOM_ema50"].pct_change()

    d_up, d_dn, d_rng = donchian(df["High"], df["Low"], n=20)
    df["MOM_donchian20_up"] = d_up
    df["MOM_donchian20_dn"] = d_dn
    df["MOM_donchian20_rng"] = d_rng
    df["MOM_dist_to_donchian_up"] = (df["Close"] - d_up) / d_up
    df["MOM_dist_to_donchian_dn"] = (df["Close"] - d_dn) / d_dn

    df["MOM_roc_24h"] = df["Close"].pct_change(24)  # 24 bars on 1h

    # ----- LVBB -----
    df["LVBB_sigma_log_48"] = rolling_log_vol(df["Close"], n=48)
    df["LVBB_ema48"] = df["Close"].ewm(span=48, adjust=False).mean()
    df["LVBB_sigma_price_48"] = df["Close"] * df["LVBB_sigma_log_48"]

    # Utilities
    df["RET_1h"] = df["Close"].pct_change().fillna(0.0)
    df["LOGRET_1h"] = np.log(df["Close"]).diff()
    vmean = df["Volume"].rolling(48, min_periods=48).mean()
    vstd  = df["Volume"].rolling(48, min_periods=48).std()
    df["VOL_z48"] = (df["Volume"] - vmean) / vstd

    keep = [
        "Open","High","Low","Close","Volume",
        # MR
        "MR_ema20","MR_atr14","MR_z_ema20_atr",
        "MR_bb_mid","MR_bb_std","MR_bb_up","MR_bb_dn","MR_bb_pctB","MR_rsi14",
        # MOM
        "MOM_ema50","MOM_ema200","MOM_ema50_slope",
        "MOM_donchian20_up","MOM_donchian20_dn","MOM_donchian20_rng",
        "MOM_dist_to_donchian_up","MOM_dist_to_donchian_dn","MOM_roc_24h",
        # LVBB
        "LVBB_sigma_log_48","LVBB_ema48","LVBB_sigma_price_48",
        # Utils
        "RET_1h","LOGRET_1h","VOL_z48",
    ]
    return df[keep]


def read_daily_states(csv_path: str) -> pd.Series:
    # robust reader: handle 'Date' or unnamed index column
    hdr = pd.read_csv(csv_path, nrows=0)
    cols = list(hdr.columns)
    if "Date" in cols:
        df = pd.read_csv(csv_path, parse_dates=["Date"])
        df = df.set_index("Date")
    else:
        df = pd.read_csv(csv_path)
        first = df.columns[0]
        df[first] = pd.to_datetime(df[first], utc=True, errors="coerce")
        df = df.set_index(first)

    df = to_utc_index(df)  # ensure UTC-sorted

    # find state column like "State_K3"
    state_cols = [c for c in df.columns if c.startswith("State_K")]
    if not state_cols:
        raise ValueError("No 'State_K*' column found in daily states CSV.")
    state_col = max(state_cols, key=len)  # pick the most specific
    S = df[state_col].astype("Int64")  # allow NA

    # collapse to one value per calendar day (should already be daily)
    S_by_day = S.groupby(S.index.normalize()).last()
    S_by_day.index.name = "Date"
    return S_by_day


def merge_daily_state_into_1h(feat_1h: pd.DataFrame, S_by_day: pd.Series) -> pd.DataFrame:
    # map same-day state and lagged-by-1-day state to 1h rows via calendar day
    day_idx = feat_1h.index.normalize()

    same_map = S_by_day.to_dict()
    lag_map  = S_by_day.shift(1).to_dict()

    feat_1h["D1_State_same_day"] = day_idx.map(same_map).astype("float")  # may start with NaN
    feat_1h["D1_State_lag1d"]    = day_idx.map(lag_map).astype("float")   # use this for trading

    return feat_1h


def main():
    # 1) Load 1h, build features
    h = pd.read_csv(IN_CSV_1H)
    if "Date" not in h.columns:
        raise ValueError("1h CSV must have a 'Date' column.")
    h = to_utc_index(h, "Date")
    feats = build_features_1h(h)

    # 2) Load daily states and merge
    S_day = read_daily_states(IN_CSV_1D)
    feats = merge_daily_state_into_1h(feats, S_day)

    # 3) Save with a Date column
    out = feats.copy().reset_index()
    out.rename(columns={"index": "Date"}, inplace=True)

    # if Date is tz-aware, drop tz; keep UTC clock time
    if pd.api.types.is_datetime64tz_dtype(out["Date"]):
        out["Date"] = out["Date"].dt.tz_convert("UTC").dt.tz_localize(None)

    out.to_csv(OUT_CSV, index=False)

    # quick sanity
    print("Saved:", OUT_CSV)
    print("NaN % — D1_State_same_day:", out["D1_State_same_day"].isna().mean())
    print("NaN % — D1_State_lag1d   :", out["D1_State_lag1d"].isna().mean())
    print("Top 8 feature NaN ratios (warmup expected):")
    print(out.isna().mean().sort_values(ascending=False).head(8).round(4))


if __name__ == "__main__":
    main()
