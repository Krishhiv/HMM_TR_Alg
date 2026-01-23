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


def _trim_to_last(df: pd.DataFrame, last_ts: pd.Timestamp) -> pd.DataFrame:
    return df[df["Date"] <= last_ts].reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Trim 1h and 15m BTC datasets to specified last timestamps."
    )
    parser.add_argument(
        "--data-dir",
        default="velocity_breakout/data/raw",
        help="Directory containing BTC-USD_15m.csv and BTC-USD_1h.csv",
    )
    parser.add_argument(
        "--last-1h",
        default="2026-01-21 05:00:00+00:00",
        help="Last timestamp to keep for 1h data (UTC).",
    )
    parser.add_argument(
        "--last-15m",
        default="2026-01-21 05:45:00+00:00",
        help="Last timestamp to keep for 15m data (UTC).",
    )
    parser.add_argument(
        "--out-1h",
        default=None,
        help="Output path for trimmed 1h CSV (default: overwrite BTC-USD_1h.csv)",
    )
    parser.add_argument(
        "--out-15m",
        default=None,
        help="Output path for trimmed 15m CSV (default: overwrite BTC-USD_15m.csv)",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    path_15m = data_dir / "BTC-USD_15m.csv"
    path_1h = data_dir / "BTC-USD_1h.csv"

    df_15m = _read_ohlcv(path_15m)
    df_1h = _read_ohlcv(path_1h)

    last_1h = pd.to_datetime(args.last_1h, utc=True)
    last_15m = pd.to_datetime(args.last_15m, utc=True)

    trimmed_1h = _trim_to_last(df_1h, last_1h)
    trimmed_15m = _trim_to_last(df_15m, last_15m)

    out_1h = Path(args.out_1h) if args.out_1h else path_1h
    out_15m = Path(args.out_15m) if args.out_15m else path_15m

    trimmed_1h.to_csv(out_1h, index=False)
    trimmed_15m.to_csv(out_15m, index=False)

    print(f"1h rows: {len(df_1h)} -> {len(trimmed_1h)} (last={trimmed_1h['Date'].iloc[-1]})")
    print(f"15m rows: {len(df_15m)} -> {len(trimmed_15m)} (last={trimmed_15m['Date'].iloc[-1]})")
    print(f"Wrote: {out_1h}")
    print(f"Wrote: {out_15m}")


if __name__ == "__main__":
    main()
