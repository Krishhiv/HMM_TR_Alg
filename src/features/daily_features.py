"""
Daily (1D) feature engineering for HMM regime detection.

Creates volatility and trend features from daily OHLCV data.
"""

import numpy as np
import pandas as pd
from pathlib import Path


def compute_daily_features(df: pd.DataFrame, n: int = 20) -> pd.DataFrame:
    """
    Compute daily features for HMM training.
    
    Args:
        df: DataFrame with OHLCV columns (Open, High, Low, Close, Volume)
        n: Rolling window size (default 20)
    
    Returns:
        DataFrame with added feature columns
    """
    df = df.copy()
    
    # Ensure required columns exist
    required = ["Open", "High", "Low", "Close", "Volume"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # Log returns (stationary)
    df["Log_Returns"] = np.log(df["Close"] / df["Close"].shift(1))
    
    # Absolute and squared returns
    df["Abs_Return"] = np.abs(df["Log_Returns"])
    df["Squared_Return"] = df["Log_Returns"] ** 2
    
    # ===== Volatility Features =====
    
    # Realized volatility from squared returns
    df[f"RealizedVol_{n}"] = (
        df["Squared_Return"]
        .rolling(window=n, min_periods=n)
        .mean()
        .pipe(np.sqrt)
    )
    
    # Parkinson range-based volatility (High/Low)
    hl_log = np.log(df["High"] / df["Low"])
    df[f"ParkinsonVol_{n}"] = np.sqrt(
        (hl_log.pow(2).rolling(window=n, min_periods=n).sum()) / (4 * n * np.log(2))
    )
    
    # Garman-Klass volatility (uses O/H/L/C)
    gk_var_bar = (
        0.5 * (np.log(df["High"] / df["Low"]) ** 2)
        - (2 * np.log(2) - 1) * (np.log(df["Close"] / df["Open"]) ** 2)
    )
    df[f"GKVol_{n}"] = np.sqrt(
        gk_var_bar.rolling(window=n, min_periods=n).mean()
    )
    
    # Volume z-score
    vol_mean = df["Volume"].rolling(window=n, min_periods=n).mean()
    vol_std = df["Volume"].rolling(window=n, min_periods=n).std()
    df[f"VolZ_{n}"] = (df["Volume"] - vol_mean) / vol_std
    
    # ===== Trend Features =====

    # Exponential moving average
    df[f"EMA_{n}"] = df["Close"].ewm(span=n, adjust=False).mean()

    # EMA slope
    df[f"EMA_{n}_slope"] = df[f"EMA_{n}"].diff()

    # Linear-regression R² on log(Close) over 14 days.
    # R² ≈ 1  → prices trace a clean linear path (trending regime)
    # R² ≈ 0  → prices are choppy/mean-reverting
    # This is the key feature that separates "trending bull" from "choppy bull".
    _r2_window = 14
    _log_close = np.log(df["Close"])
    _x = np.arange(_r2_window, dtype=float)
    _x -= _x.mean()          # centre for numerical stability
    _ss_x = (_x * _x).sum()

    def _r2(y: np.ndarray) -> float:
        y_c = y - y.mean()
        ss_tot = (y_c * y_c).sum()
        if ss_tot < 1e-15:
            return 1.0
        beta = (_x * y_c).sum() / _ss_x
        ss_res = ((y_c - beta * _x) * (y_c - beta * _x)).sum()
        return max(0.0, 1.0 - ss_res / ss_tot)

    df[f"LinReg_R2_{_r2_window}"] = (
        _log_close.rolling(window=_r2_window, min_periods=_r2_window)
        .apply(_r2, raw=True)
    )

    return df


def load_and_process(
    in_csv: Path,
    out_csv: Path,
    date_col: str = "time",
    n: int = 20,
) -> pd.DataFrame:
    """
    Load raw daily OHLCV, compute features, and save.
    
    Args:
        in_csv: Path to input CSV
        out_csv: Path for output CSV
        date_col: Name of date column in input
        n: Rolling window size
    
    Returns:
        Processed DataFrame
    """
    # Load
    df = pd.read_csv(in_csv)
    
    # Parse date index
    if date_col in df.columns:
        df["Date"] = pd.to_datetime(df[date_col], utc=True, errors="coerce")
        df = df.drop(columns=[date_col] if date_col != "Date" else [])
        df = df.set_index("Date").sort_index()
    else:
        df.index = pd.to_datetime(df.index, utc=True, errors="coerce")
        df = df.sort_index()
    
    # Compute features
    df = compute_daily_features(df, n=n)
    
    # Drop warmup NaNs
    df = df.dropna()
    
    # Save with Date column
    out = df.reset_index()
    if "Date" not in out.columns and "index" in out.columns:
        out = out.rename(columns={"index": "Date"})
    
    # Strip timezone for cleaner CSV
    if pd.api.types.is_datetime64tz_dtype(out["Date"]):
        out["Date"] = out["Date"].dt.tz_convert("UTC").dt.tz_localize(None)
    
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_csv, index=False)
    print(f"Saved: {out_csv} ({len(out)} rows)")
    
    return df


if __name__ == "__main__":
    from pathlib import Path
    
    # Default paths
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    IN_CSV = PROJECT_ROOT / "data/raw/btc_1d_coinbase.csv"
    OUT_CSV = PROJECT_ROOT / "data/processed/btc_1d_features.csv"
    
    if IN_CSV.exists():
        load_and_process(IN_CSV, OUT_CSV)
    else:
        print(f"Input not found: {IN_CSV}")
        print("Run src/data/coinbase_downloader.py first to download data.")
