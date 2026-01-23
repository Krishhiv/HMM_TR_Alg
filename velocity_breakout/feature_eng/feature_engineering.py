import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def _standardize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names and ensure timestamp is datetime."""
    cols = {c: c.strip().lower() for c in df.columns}
    df = df.rename(columns=cols).copy()
    if "date" in df.columns:
        df = df.rename(columns={"date": "timestamp"})
    required = ["timestamp", "open", "high", "low", "close", "volume"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df


def _add_common_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add core technical indicators used by the strategy."""
    out = df.copy()

    # EMAs
    out["ema_50"] = out["close"].ewm(span=50, adjust=False).mean()
    out["ema_100"] = out["close"].ewm(span=100, adjust=False).mean()

    # True range and ATR
    high_low = out["high"] - out["low"]
    high_prev_close = (out["high"] - out["close"].shift(1)).abs()
    low_prev_close = (out["low"] - out["close"].shift(1)).abs()
    out["tr"] = np.maximum(high_low, np.maximum(high_prev_close, low_prev_close))
    out["atr_14"] = out["tr"].rolling(14).mean()
    out["atr_50_ma"] = out["atr_14"].rolling(50).mean()

    # Donchian channels (CRITICAL: shifted by 1 to avoid look-ahead bias)
    out["high_20"] = out["high"].rolling(20).max()
    out["low_20"] = out["low"].rolling(20).min()
    out["high_20_prev"] = out["high_20"].shift(1)  # For breakout detection
    out["low_20_prev"] = out["low_20"].shift(1)    # For breakout detection

    # Volume
    out["volume_ma_20"] = out["volume"].rolling(20).mean()
    out["volume_ratio"] = out["volume"] / out["volume_ma_20"]

    # ROC (Rate of Change)
    out["roc_3"] = (out["close"] / out["close"].shift(3) - 1.0) * 100.0

    # CLV (Close Location Value)
    range_ = out["high"] - out["low"]
    clv = ((out["close"] - out["low"]) - (out["high"] - out["close"])) / range_
    out["clv"] = np.where(range_ == 0, 0.0, clv)

    # Time features
    out["hour_utc"] = out["timestamp"].dt.hour

    # Next bar's open (for realistic backtesting fills)
    out["open_next"] = out["open"].shift(-1)

    return out


def _trim_feature_nans(df: pd.DataFrame) -> pd.DataFrame:
    feature_cols = [
        "ema_50",
        "ema_100",
        "atr_14",
        "atr_50_ma",
        "high_20",
        "low_20",
        "volume_ma_20",
        "volume_ratio",
        "roc_3",
        "clv",
        "open_next",
    ]
    return df.dropna(subset=feature_cols).reset_index(drop=True)


def build_15m_features(df_15m: pd.DataFrame, trim_nans: bool = True) -> pd.DataFrame:
    """Build features for 15-minute timeframe."""
    df = _standardize_ohlcv(df_15m)
    df = _add_common_features(df)
    
    # Add 15m-specific label for clarity
    df["timeframe"] = "15m"

    return _trim_feature_nans(df) if trim_nans else df


def build_1h_features(df_1h: pd.DataFrame, trim_nans: bool = True) -> pd.DataFrame:
    """Build features for 1-hour timeframe."""
    df = _standardize_ohlcv(df_1h)
    df = _add_common_features(df)
    
    # Add 1h-specific label for clarity
    df["timeframe"] = "1h"

    return _trim_feature_nans(df) if trim_nans else df


def merge_1h_ema_to_15m(
    df_15m: pd.DataFrame, 
    df_1h: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge 1-hour EMA50 into 15-minute data for higher timeframe trend filter.
    
    This is an OPTIONAL enhancement that adds a stronger trend filter.
    Uses merge_asof to broadcast hourly values to all 15m bars within that hour.
    """
    # Ensure both are sorted by timestamp
    df_15m_sorted = df_15m.sort_values("timestamp").copy()
    df_1h_sorted = df_1h.sort_values("timestamp").copy()
    
    # Select only timestamp and ema_50 from 1h data
    df_1h_ema = df_1h_sorted[["timestamp", "ema_50"]].copy()
    df_1h_ema = df_1h_ema.rename(columns={"ema_50": "ema_50_1h"})
    
    # Merge using backward direction (each 15m bar gets the most recent 1h EMA)
    df_merged = pd.merge_asof(
        df_15m_sorted,
        df_1h_ema,
        on="timestamp",
        direction="backward"
    )
    
    return df_merged


def merge_daily_regime(
    df_15m: pd.DataFrame,
    df_daily: pd.DataFrame,
    regime_col: str = "state_lag1d"
) -> pd.DataFrame:
    """
    Merge daily HMM regime state into 15-minute data.
    
    This is OPTIONAL and requires your existing daily HMM output.
    Allows the strategy to avoid trading when TR³ is active (State 1).
    
    Parameters:
    -----------
    df_15m : DataFrame with 15m features
    df_daily : DataFrame with columns ['timestamp', regime_col]
    regime_col : Name of the lagged regime state column (default: 'state_lag1d')
    """
    # Ensure sorted
    df_15m_sorted = df_15m.sort_values("timestamp").copy()
    df_daily_sorted = df_daily.sort_values("timestamp").copy()
    
    # Select only timestamp and regime
    df_regime = df_daily_sorted[["timestamp", regime_col]].copy()
    
    # Merge using backward direction (each 15m bar gets current day's regime)
    df_merged = pd.merge_asof(
        df_15m_sorted,
        df_regime,
        on="timestamp",
        direction="backward"
    )
    
    return df_merged


def validate_features(df: pd.DataFrame, timeframe: str) -> None:
    """
    Validate feature engineering output and print diagnostics.
    
    Checks for common issues:
    - NaN values (expected only in initial lookback period)
    - Infinite values (should be none)
    - CLV range (should be [-1, 1])
    - Volume ratio distribution (should center around 1.0)
    """
    print(f"\n{'='*60}")
    print(f"Feature Validation - {timeframe} Timeframe")
    print(f"{'='*60}")
    
    # 1. Check data shape
    print(f"\nTotal rows: {len(df):,}")
    print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
    
    # 2. NaN counts
    nan_counts = df.isnull().sum()
    nan_counts = nan_counts[nan_counts > 0]
    if len(nan_counts) > 0:
        print(f"\nNaN counts by column:")
        print(nan_counts)
        print(f"\nRows with ANY NaN: {df.isnull().any(axis=1).sum():,}")
    else:
        print("\n✓ No NaN values found")
    
    # 3. Infinite values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    inf_counts = np.isinf(df[numeric_cols]).sum()
    inf_counts = inf_counts[inf_counts > 0]
    if len(inf_counts) > 0:
        print(f"\n⚠ WARNING: Infinite values found:")
        print(inf_counts)
    else:
        print("✓ No infinite values")
    
    # 4. CLV range validation
    clv_min, clv_max = df["clv"].min(), df["clv"].max()
    if clv_min < -1.01 or clv_max > 1.01:  # Allow small float precision error
        print(f"\n⚠ WARNING: CLV out of range [-1, 1]: min={clv_min:.4f}, max={clv_max:.4f}")
    else:
        print(f"✓ CLV range valid: [{clv_min:.4f}, {clv_max:.4f}]")
    
    # 5. Volume ratio stats
    vol_ratio_stats = df["volume_ratio"].describe()
    print(f"\nVolume Ratio distribution:")
    print(f"  Mean: {vol_ratio_stats['mean']:.3f} (should be ~1.0)")
    print(f"  Median: {vol_ratio_stats['50%']:.3f}")
    print(f"  Std: {vol_ratio_stats['std']:.3f}")
    
    # 6. ATR sanity check
    if df["atr_14"].max() > df["close"].mean() * 0.5:
        print(f"\n⚠ WARNING: ATR seems unusually high (max={df['atr_14'].max():.2f})")
    else:
        print(f"✓ ATR values seem reasonable (max={df['atr_14'].max():.2f})")
    
    # 7. Donchian shift verification
    breakout_count = (df["high"] > df["high_20_prev"]).sum()
    print(f"\nDonchian breakouts detected: {breakout_count:,} ({100*breakout_count/len(df):.2f}%)")
    
    print(f"{'='*60}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build feature engineering outputs for 15m and 1h BTC data."
    )
    parser.add_argument(
        "--data-dir",
        default="velocity_breakout/data/raw",
        help="Directory containing BTC-USD_15m.csv and BTC-USD_1h.csv",
    )
    parser.add_argument(
        "--out-dir",
        default="velocity_breakout/data/feature_engineered",
        help="Directory to write feature CSVs",
    )
    parser.add_argument(
        "--add-1h-ema",
        action="store_true",
        help="Merge 1h EMA50 into 15m data for higher timeframe filter (optional)",
    )
    parser.add_argument(
        "--daily-regime-path",
        default=None,
        help="Path to daily HMM regime CSV (optional, for regime filtering)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run validation checks and print diagnostics",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load raw data
    print("Loading raw data...")
    df_15m = pd.read_csv(data_dir / "BTC-USD_15m.csv")
    df_1h = pd.read_csv(data_dir / "BTC-USD_1h.csv")
    
    print(f"15m data: {len(df_15m):,} rows")
    print(f"1h data: {len(df_1h):,} rows")

    # Build features
    print("\nBuilding 15m features...")
    feat_15m = build_15m_features(df_15m, trim_nans=True)
    
    print("Building 1h features...")
    feat_1h = build_1h_features(df_1h, trim_nans=True)

    # Optional: merge 1h EMA into 15m data
    if args.add_1h_ema:
        print("\nMerging 1h EMA50 into 15m data...")
        feat_15m = merge_1h_ema_to_15m(feat_15m, feat_1h)
        print("✓ 1h EMA50 merged")

    # Optional: merge daily regime
    if args.daily_regime_path:
        regime_path = Path(args.daily_regime_path)
        if regime_path.exists():
            print(f"\nMerging daily regime from {regime_path}...")
            df_daily = pd.read_csv(regime_path)
            feat_15m = merge_daily_regime(feat_15m, df_daily)
            print("✓ Daily regime merged")
        else:
            print(f"⚠ WARNING: Regime file not found at {regime_path}")

    # Validation
    if args.validate:
        validate_features(feat_15m, "15m")
        validate_features(feat_1h, "1h")

    # Save outputs
    print("\nSaving feature-engineered data...")
    feat_15m.to_csv(out_dir / "BTC-USD_15m_features.csv", index=False)
    feat_1h.to_csv(out_dir / "BTC-USD_1h_features.csv", index=False)
    
    print(f"\n✓ Features saved to {out_dir}")
    print(f"  - BTC-USD_15m_features.csv ({len(feat_15m):,} rows)")
    print(f"  - BTC-USD_1h_features.csv ({len(feat_1h):,} rows)")
    
    # Summary of columns
    print(f"\n15m columns ({len(feat_15m.columns)}):")
    print(list(feat_15m.columns))
    print(f"\n1h columns ({len(feat_1h.columns)}):")
    print(list(feat_1h.columns))


if __name__ == "__main__":
    main()
