from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def load_ohlcv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "Date" not in df.columns:
        raise ValueError("Expected 'Date' column in CSV")
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def kalman_filter_1d(prices: np.ndarray, q: float, r: float) -> np.ndarray:
    mu = np.empty_like(prices, dtype=float)
    p = 1.0
    x = np.nan
    for i, price in enumerate(prices):
        if np.isnan(x):
            x = price
            mu[i] = x
            continue
        x_pred = x
        p_pred = p + q
        k = p_pred / (p_pred + r)
        x = x_pred + k * (price - x_pred)
        p = (1.0 - k) * p_pred
        mu[i] = x
    return mu


def ewma_volatility(prices: np.ndarray,
                        fair_value: np.ndarray,
                        lambda_: float = 0.94,
                        var_floor: float = 1e-12) -> np.ndarray:
    """
    EWMA volatility of deviation (price - fair_value), in PRICE units.
    Guarantees strictly positive output after flooring.
    """
    prices = prices.astype(float)
    fair_value = fair_value.astype(float)

    variance = np.full_like(prices, np.nan, dtype=float)
    var = np.nan

    for i, (price, fv) in enumerate(zip(prices, fair_value)):
        if not (np.isfinite(price) and np.isfinite(fv)):
            continue

        sq_dev = (price - fv) ** 2

        if np.isnan(var):
            var = max(sq_dev, var_floor)
        else:
            var = lambda_ * var + (1.0 - lambda_) * sq_dev
            var = max(var, var_floor)

        variance[i] = var

    return np.sqrt(variance)



def hurst_exponent_window(prices: np.ndarray,
                                lag_max: int = 20,
                                clamp: bool = True) -> float:
    """
    More stable Hurst proxy using log prices and std(diff) scaling:
        std(X_t - X_{t-lag}) ~ lag^H
    So slope of log(std(diff)) vs log(lag) ≈ H
    """
    prices = prices.astype(float)
    prices = prices[np.isfinite(prices)]

    # Need enough points to estimate across lags
    min_len = max(50, 4 * lag_max)  # e.g. lag_max=20 => min_len=80
    if len(prices) < min_len:
        return np.nan

    x = np.log(prices)  # key fix

    max_lag = min(lag_max, len(x) // 4)  # avoid huge lags
    if max_lag < 5:
        return np.nan

    lags = np.arange(2, max_lag + 1)
    tau = np.empty_like(lags, dtype=float)

    for i, lag in enumerate(lags):
        diff = x[lag:] - x[:-lag]
        s = np.std(diff)
        tau[i] = s

    if np.any(tau <= 0) or np.any(~np.isfinite(tau)):
        return np.nan

    slope, _ = np.polyfit(np.log(lags), np.log(tau), 1)
    h = float(slope)

    if clamp:
        # estimator noise can slightly exceed bounds
        h = float(np.clip(h, 0.0, 1.0))

    return h


def rolling_hurst(prices: np.ndarray, window: int = 200, lag_max: int = 20) -> np.ndarray:
    out = np.full(prices.shape, np.nan, dtype=float)
    for i in range(window - 1, len(prices)):
        out[i] = hurst_exponent_window(prices[i - window + 1 : i + 1], lag_max=lag_max, clamp=True)
    return out



def build_features_5m(df_5m: pd.DataFrame, hurst_15m: pd.DataFrame,
                      q: float, r: float, lambda_: float) -> pd.DataFrame:
    close = df_5m["Close"].to_numpy(dtype=float)

    fair_value = kalman_filter_1d(close, q=q, r=r)
    vol = ewma_volatility(close, fair_value, lambda_=lambda_)

    z = np.zeros_like(close, dtype=float)
    valid = vol > 0
    z[valid] = (close[valid] - fair_value[valid]) / vol[valid]

    range_pct = (df_5m["High"] - df_5m["Low"]) / df_5m["Close"]
    liquidity_cost_proxy = np.maximum(0.0002, 0.10 * range_pct)

    features = df_5m.copy()
    features["FairValue"] = fair_value
    features["EWMAVol"] = vol
    features["ZScore"] = z
    features["RangePct"] = range_pct
    features["LiquidityCostProxy"] = liquidity_cost_proxy

    hurst_15m = hurst_15m.sort_values("Date").copy()
    # Hurst for a 15m candle is only known at the candle close.
    hurst_15m["HurstTime"] = hurst_15m["Date"] + pd.Timedelta(minutes=15)
    aligned = pd.merge_asof(
        features.sort_values("Date"),
        hurst_15m[["HurstTime", "Hurst15m"]],
        left_on="Date",
        right_on="HurstTime",
        direction="backward",
    )
    aligned = aligned.drop(columns=["HurstTime"])
    aligned["Hurst15m"] = aligned["Hurst15m"].ffill()

    return aligned


def build_features_15m(df_15m: pd.DataFrame, window: int, lag_max: int) -> pd.DataFrame:
    close = df_15m["Close"].to_numpy(dtype=float)
    hurst = rolling_hurst(close, window=window, lag_max=lag_max)
    out = df_15m.copy()
    out["Hurst15m"] = hurst
    out["Hurst15m"] = out["Hurst15m"].ffill()
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-5m", default="EngineB/Data/BTC-USD_5m.csv")
    parser.add_argument("--input-15m", default="EngineB/Data/BTC-USD_15m.csv")
    parser.add_argument("--out-dir", default="EngineB/Data/Feature-Engineered")
    parser.add_argument("--q", type=float, default=1e-5)
    parser.add_argument("--r", type=float, default=1e-3)
    parser.add_argument("--lambda", dest="lambda_", type=float, default=0.94)
    parser.add_argument("--hurst-window", type=int, default=200)
    parser.add_argument("--hurst-lag-max", type=int, default=20)

    args = parser.parse_args()

    df_5m = load_ohlcv(Path(args.input_5m))
    df_15m = load_ohlcv(Path(args.input_15m))

    features_15m = build_features_15m(df_15m, window=args.hurst_window, lag_max=args.hurst_lag_max)
    features_5m = build_features_5m(df_5m, features_15m, q=args.q, r=args.r, lambda_=args.lambda_)

    end_5m = features_5m["Date"].max()
    end_15m = features_15m["Date"].max()
    aligned_end = min(end_5m, end_15m)
    features_5m = features_5m[features_5m["Date"] <= aligned_end].reset_index(drop=True)
    features_15m = features_15m[features_15m["Date"] <= aligned_end].reset_index(drop=True)
    
    print("Hurst NaN %:", features_15m["Hurst15m"].isna().mean())
    print("Hurst unique (finite):", features_15m["Hurst15m"].dropna().nunique())
    print(features_15m["Hurst15m"].dropna().head(10).to_list())


    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_15m = out_dir / "BTC-USD_15m_features.csv"
    out_5m = out_dir / "BTC-USD_5m_features.csv"

    features_15m.to_csv(out_15m, index=False)
    features_5m.to_csv(out_5m, index=False)

    print(f"Wrote {out_15m}")
    print(f"Wrote {out_5m}")


if __name__ == "__main__":
    main()
