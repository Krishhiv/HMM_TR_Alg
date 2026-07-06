"""
Hourly (1H) feature engineering for TR³ trading strategy.

Creates MR (Mean Reversion), MOM (Momentum), and LVBB (Local Vol BB) features.
Also merges daily HMM regime states into hourly data.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional


def true_range(high: pd.Series, low: pd.Series, close_prev: pd.Series) -> pd.Series:
    """Calculate true range."""
    hl = high - low
    hc = (high - close_prev).abs()
    lc = (low - close_prev).abs()
    return pd.concat([hl, hc, lc], axis=1).max(axis=1)


def atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14) -> pd.Series:
    """Average True Range (Wilder smoothing)."""
    c_prev = close.shift(1)
    tr = true_range(high, low, c_prev)
    return tr.ewm(alpha=1.0 / n, adjust=False).mean()


def rsi_wilder(close: pd.Series, n: int = 14) -> pd.Series:
    """RSI using Wilder's smoothing."""
    diff = close.diff()
    up = diff.clip(lower=0.0)
    dn = -diff.clip(upper=0.0)
    avg_gain = up.ewm(alpha=1.0 / n, adjust=False).mean()
    avg_loss = dn.ewm(alpha=1.0 / n, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + rs))


def rolling_log_vol(close: pd.Series, n: int = 48) -> pd.Series:
    """Rolling log volatility."""
    logp = np.log(close)
    lr = logp.diff()
    return lr.rolling(n, min_periods=n).std()


def donchian(high: pd.Series, low: pd.Series, n: int = 20) -> tuple:
    """Donchian channel (upper, lower, range)."""
    up = high.rolling(n, min_periods=n).max()
    dn = low.rolling(n, min_periods=n).min()
    rng = up - dn
    return up, dn, rng


def rolling_r2(series: pd.Series, window: int) -> pd.Series:
    """Rolling OLS R² of series against time."""
    x = np.arange(window)
    
    def _r2(y_vals: np.ndarray) -> float:
        y = y_vals
        X = np.vstack([np.ones(window), x - x.mean()]).T
        try:
            beta = np.linalg.lstsq(X, y, rcond=None)[0]
            yhat = X @ beta
            ssr = ((yhat - y.mean()) ** 2).sum()
            sst = ((y - y.mean()) ** 2).sum()
            return 0.0 if sst == 0 else float(ssr / sst)
        except Exception:
            return np.nan
    
    return series.rolling(window, min_periods=window).apply(_r2, raw=True)


def compute_adx(
    high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14
) -> pd.Series:
    """Average Directional Index."""
    up_move = (high - high.shift(1)).clip(lower=0)
    down_move = (low.shift(1) - low).clip(lower=0)
    plus_dm = up_move.where(up_move > down_move, 0.0)
    minus_dm = down_move.where(down_move > up_move, 0.0)
    
    tr = pd.concat([
        (high - low),
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    
    atr_val = tr.ewm(alpha=1 / n, adjust=False).mean()
    plus_di = 100 * (plus_dm.ewm(alpha=1 / n, adjust=False).mean() / atr_val.replace(0, np.nan))
    minus_di = 100 * (minus_dm.ewm(alpha=1 / n, adjust=False).mean() / atr_val.replace(0, np.nan))
    dx = ((plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)) * 100
    adx = dx.ewm(alpha=1 / n, adjust=False).mean()
    return adx


def compute_hourly_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute all hourly features for TR³ strategy.
    
    Categories:
        - MR (Mean Reversion): EMA, ATR, Bollinger Bands, RSI
        - MOM (Momentum): EMAs, Donchian, ROC
        - LVBB (Local Vol BB): Local volatility metrics
        - PRIME extras: Squeeze, R², ADX
    
    Args:
        df: DataFrame with OHLCV columns
    
    Returns:
        DataFrame with added feature columns
    """
    df = df.copy()
    
    # Validate columns
    required = ["Open", "High", "Low", "Close", "Volume"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # ===== MR (Mean Reversion) =====
    df["MR_ema20"] = df["Close"].ewm(span=20, adjust=False).mean()
    df["MR_atr14"] = atr(df["High"], df["Low"], df["Close"], n=14)
    
    scale = df["MR_atr14"].replace(0, np.nan)
    df["MR_z_ema20_atr"] = (df["Close"] - df["MR_ema20"]) / scale
    
    # Bollinger Bands
    sma20 = df["Close"].rolling(20, min_periods=20).mean()
    std20 = df["Close"].rolling(20, min_periods=20).std()
    df["MR_bb_mid"] = sma20
    df["MR_bb_std"] = std20
    df["MR_bb_up"] = sma20 + 2.0 * std20
    df["MR_bb_dn"] = sma20 - 2.0 * std20
    df["MR_bb_pctB"] = (df["Close"] - df["MR_bb_dn"]) / (df["MR_bb_up"] - df["MR_bb_dn"])
    
    df["MR_rsi14"] = rsi_wilder(df["Close"], n=14)
    
    # ===== MOM (Momentum) =====
    df["MOM_ema50"] = df["Close"].ewm(span=50, adjust=False).mean()
    df["MOM_ema200"] = df["Close"].ewm(span=200, adjust=False).mean()
    df["MOM_ema50_slope"] = df["MOM_ema50"].pct_change()
    
    d_up, d_dn, d_rng = donchian(df["High"], df["Low"], n=20)
    # Shift by 1 so the channel excludes the current bar's High/Low.
    # Without the shift, High[t] >= Close[t] guarantees Close > channel is
    # always False, silently killing the Donchian breakout signal.
    df["MOM_donchian20_up"] = d_up.shift(1)
    df["MOM_donchian20_dn"] = d_dn.shift(1)
    df["MOM_donchian20_rng"] = d_rng.shift(1)
    df["MOM_dist_to_donchian_up"] = (df["Close"] - df["MOM_donchian20_up"]) / df["MOM_donchian20_up"]
    df["MOM_dist_to_donchian_dn"] = (df["Close"] - df["MOM_donchian20_dn"]) / df["MOM_donchian20_dn"]
    
    df["MOM_roc_24h"] = df["Close"].pct_change(24)
    
    # ===== LVBB (Local Vol BB) =====
    df["LVBB_sigma_log_48"] = rolling_log_vol(df["Close"], n=48)
    df["LVBB_ema48"] = df["Close"].ewm(span=48, adjust=False).mean()
    df["LVBB_sigma_price_48"] = df["Close"] * df["LVBB_sigma_log_48"]
    
    # ===== Utility =====
    df["RET_1h"] = df["Close"].pct_change().fillna(0.0)
    df["LOGRET_1h"] = np.log(df["Close"]).diff()
    
    vmean = df["Volume"].rolling(48, min_periods=48).mean()
    vstd = df["Volume"].rolling(48, min_periods=48).std()
    df["VOL_z48"] = (df["Volume"] - vmean) / vstd
    
    # ===== PRIME extras =====
    # Squeeze indicators
    df["BBW"] = (df["MR_bb_up"] - df["MR_bb_dn"]) / df["MR_bb_mid"].replace(0, np.nan)
    df["KC_up"] = df["MR_ema20"] + 1.5 * df["MR_atr14"]
    df["KC_dn"] = df["MR_ema20"] - 1.5 * df["MR_atr14"]
    df["SQZ"] = (df["MR_bb_up"] < df["KC_up"]) & (df["MR_bb_dn"] > df["KC_dn"])
    df["RECENT_SQZ"] = df["SQZ"].rolling(24, min_periods=1).max().astype(bool)
    
    df["BBW_MED20"] = df["BBW"].rolling(20, min_periods=20).median()
    df["EXPANDING"] = (df["BBW"] > df["BBW_MED20"]) & (df["BBW"] - df["BBW"].shift(3) > 0)
    
    # Trend quality
    df["R2_ema50"] = rolling_r2(df["MOM_ema50"], window=72)
    df["ADX14"] = compute_adx(df["High"], df["Low"], df["Close"], n=14)
    
    # Micro-breakout strength
    df["S_VNB"] = (df["Close"] - df["MOM_donchian20_up"]) / df["MR_atr14"].replace(0, np.nan)
    df["DIST_up_ATR"] = df["S_VNB"]
    
    return df


def merge_daily_states(
    hourly_df: pd.DataFrame,
    daily_states: pd.Series,
) -> pd.DataFrame:
    """
    Merge daily HMM states into hourly data.
    
    Creates:
        - D1_State_same_day: State for current calendar day
        - D1_State_lag1d: State lagged by 1 day (for trading, avoids lookahead)
    
    Args:
        hourly_df: Hourly DataFrame with datetime index
        daily_states: Series of states indexed by date
    
    Returns:
        Hourly DataFrame with state columns added
    """
    df = hourly_df.copy()
    
    # Normalize to calendar day
    day_idx = df.index.normalize()
    
    same_map = daily_states.to_dict()
    lag_map = daily_states.shift(1).to_dict()
    
    df["D1_State_same_day"] = day_idx.map(same_map).astype("float")
    df["D1_State_lag1d"] = day_idx.map(lag_map).astype("float")
    
    return df


def to_utc_index(df: pd.DataFrame, date_col: str = "Date") -> pd.DataFrame:
    """Ensure DataFrame has UTC datetime index."""
    if date_col in df.columns:
        idx = pd.to_datetime(df[date_col], utc=True, errors="coerce")
        df = df.set_index(idx).drop(columns=[date_col])
    else:
        df.index = pd.to_datetime(df.index, utc=True, errors="coerce")
    return df.sort_index()


def load_and_process(
    hourly_csv: Path,
    daily_states_csv: Optional[Path] = None,
    out_csv: Optional[Path] = None,
) -> pd.DataFrame:
    """
    Load hourly OHLCV, compute features, optionally merge states, and save.
    
    Args:
        hourly_csv: Path to hourly OHLCV CSV
        daily_states_csv: Optional path to daily states CSV (with State_K* column)
        out_csv: Optional output path
    
    Returns:
        Processed DataFrame
    """
    # Load hourly
    df = pd.read_csv(hourly_csv)
    if "Date" not in df.columns and "time" in df.columns:
        df = df.rename(columns={"time": "Date"})
    df = to_utc_index(df, "Date")
    
    # Compute features
    df = compute_hourly_features(df)
    
    # Merge daily states if provided
    if daily_states_csv and daily_states_csv.exists():
        # Load daily states
        states_df = pd.read_csv(daily_states_csv)
        
        # Find date column
        date_col = "Date" if "Date" in states_df.columns else states_df.columns[0]
        states_df[date_col] = pd.to_datetime(states_df[date_col], utc=True, errors="coerce")
        states_df = states_df.set_index(date_col).sort_index()
        
        # Find state column
        state_cols = [c for c in states_df.columns if c.startswith("State_K")]
        if state_cols:
            state_col = state_cols[0]
            S = states_df[state_col].astype("Int64")
            S_by_day = S.groupby(S.index.normalize()).last()
            S_by_day.index.name = "Date"
            df = merge_daily_states(df, S_by_day)
    
    # Save
    if out_csv:
        out = df.reset_index()
        out = out.rename(columns={"index": "Date"})
        if pd.api.types.is_datetime64tz_dtype(out["Date"]):
            out["Date"] = out["Date"].dt.tz_convert("UTC").dt.tz_localize(None)
        out_csv.parent.mkdir(parents=True, exist_ok=True)
        out.to_csv(out_csv, index=False)
        print(f"Saved: {out_csv} ({len(out)} rows)")
    
    return df


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    
    HOURLY_CSV = PROJECT_ROOT / "data/raw/btc_1h_coinbase.csv"
    STATES_CSV = PROJECT_ROOT / "data/processed/btc_1d_with_states.csv"
    OUT_CSV = PROJECT_ROOT / "data/processed/btc_1h_features.csv"
    
    if HOURLY_CSV.exists():
        load_and_process(HOURLY_CSV, STATES_CSV, OUT_CSV)
    else:
        print(f"Input not found: {HOURLY_CSV}")
