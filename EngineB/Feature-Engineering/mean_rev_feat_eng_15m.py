import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def _rolling_percentile(series: pd.Series, window: int) -> pd.Series:
    def _pct_rank(x: np.ndarray) -> float:
        if len(x) == 0:
            return np.nan
        last = x[-1]
        return float(np.sum(x <= last) / len(x))

    return series.rolling(window=window, min_periods=window).apply(_pct_rank, raw=True)


def _compute_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["Date"] = pd.to_datetime(out["Date"], utc=True, errors="coerce")
    out = out.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    # Daily VWAP (UTC reset)
    out["date"] = out["Date"].dt.date
    out["pv"] = out["Close"] * out["Volume"]
    grouped = out.groupby("date", sort=False)
    out["cum_pv"] = grouped["pv"].cumsum()
    out["cum_vol"] = grouped["Volume"].cumsum()
    out["vwap"] = out["cum_pv"] / out["cum_vol"]

    # Normalized spread
    out["diff"] = out["Close"] - out["vwap"]
    out["sigma_100"] = out["diff"].rolling(window=100, min_periods=100).std()
    out["spread"] = out["diff"] / out["sigma_100"]

    # Spread velocity
    out["spread_vel"] = out["spread"] - out["spread"].shift(1)

    # ATR(14)
    high = out["High"]
    low = out["Low"]
    close = out["Close"]
    prev_close = close.shift(1)
    tr = pd.concat(
        [
            (high - low),
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    out["atr_14"] = tr.rolling(window=14, min_periods=14).mean()

    # Volatility percentile (ATR over 500 bars)
    out["vol_pct_500"] = _rolling_percentile(out["atr_14"], window=500)

    # Time decay / inventory risk (bars since VWAP touch)
    touch = (out["Low"] <= out["vwap"]) & (out["High"] >= out["vwap"])
    out["touch_vwap"] = touch.astype(int)
    time_since = np.zeros(len(out), dtype=int)
    last = 0
    for i, is_touch in enumerate(touch):
        if is_touch:
            last = 0
        else:
            last += 1
        time_since[i] = last
    out["time_since_vwap"] = time_since

    # Cleanup
    drop_cols = ["date", "pv", "cum_pv", "cum_vol", "diff"]
    out = out.drop(columns=[c for c in drop_cols if c in out.columns])
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Build 15m mean reversion features for BTC.")
    parser.add_argument("--in-dir", default="EngineB/Data", help="Input directory with 15m CSVs.")
    parser.add_argument("--out-dir", default="EngineB/Data", help="Output directory for feature CSVs.")
    args = parser.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    symbol = "BTC-USD"
    src = in_dir / f"{symbol}_15m.csv"
    if not src.exists():
        print(f"[skip] {symbol}: missing {src}")
        return
    df = pd.read_csv(src)
    out = _compute_features(df)
    dst = out_dir / f"{symbol}_15m_features.csv"
    out.to_csv(dst, index=False)
    print(f"[saved] {symbol} -> {dst}")


if __name__ == "__main__":
    main()
