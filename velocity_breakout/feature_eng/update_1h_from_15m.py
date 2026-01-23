import argparse
from pathlib import Path

import pandas as pd


def _read_ohlcv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.rename(columns={c: c.strip() for c in df.columns})
    if "Date" not in df.columns:
        raise ValueError(f"Missing Date column in {path}")
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def _resample_15m_to_1h(df_15m: pd.DataFrame) -> pd.DataFrame:
    df = df_15m.set_index("Date")

    agg = {
        "Open": "first",
        "High": "max",
        "Low": "min",
        "Close": "last",
        "Volume": "sum",
    }

    # Use left-closed, left-labeled hourly bins aligned to the hour.
    out = df.resample("1H", label="left", closed="left").agg(agg)
    out = out.dropna(subset=["Open", "High", "Low", "Close"]).reset_index()
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extend 1h OHLCV using 15m data so time ranges align."
    )
    parser.add_argument(
        "--data-dir",
        default="velocity_breakout/data/raw",
        help="Directory containing BTC-USD_15m.csv and BTC-USD_1h.csv",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output path for updated 1h CSV (default: overwrite BTC-USD_1h.csv)",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    path_15m = data_dir / "BTC-USD_15m.csv"
    path_1h = data_dir / "BTC-USD_1h.csv"

    df_15m = _read_ohlcv(path_15m)
    df_1h = _read_ohlcv(path_1h)

    resampled_1h = _resample_15m_to_1h(df_15m)

    last_1h_ts = df_1h["Date"].iloc[-1]
    to_append = resampled_1h[resampled_1h["Date"] > last_1h_ts]

    updated = pd.concat([df_1h, to_append], ignore_index=True)
    updated = updated.drop_duplicates(subset=["Date"], keep="last")
    updated = updated.sort_values("Date").reset_index(drop=True)

    out_path = Path(args.out) if args.out else path_1h
    updated.to_csv(out_path, index=False)

    print(f"Existing 1h last timestamp: {last_1h_ts}")
    print(f"15m resampled last timestamp: {resampled_1h['Date'].iloc[-1]}")
    print(f"Appended rows: {len(to_append)}")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
