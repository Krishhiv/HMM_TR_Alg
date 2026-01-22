from __future__ import annotations

import argparse
from datetime import timezone
from pathlib import Path

import pandas as pd


def _load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "Date" not in df.columns:
        raise ValueError("Expected 'Date' column in CSV")
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    df = df.sort_values("Date")
    return df


def _qa_report(df: pd.DataFrame, freq: str) -> str:
    lines = []
    lines.append(f"rows: {len(df)}")
    if df.empty:
        lines.append("empty dataset")
        return "\n".join(lines)

    start = df["Date"].iloc[0]
    end = df["Date"].iloc[-1]
    lines.append(f"start: {start.isoformat()}")
    lines.append(f"end: {end.isoformat()}")

    expected = pd.date_range(start=start, end=end, freq=freq, tz=timezone.utc)
    missing = expected.difference(df["Date"])
    lines.append(f"expected_bars: {len(expected)}")
    lines.append(f"missing_bars: {len(missing)}")
    if len(missing) > 0:
        lines.append(f"first_missing: {missing[0].isoformat()}")

    dup_count = df.duplicated(subset=["Date"]).sum()
    lines.append(f"duplicate_dates: {int(dup_count)}")

    ohlc_cols = ["Open", "High", "Low", "Close"]
    missing_cols = [c for c in ohlc_cols + ["Volume"] if c not in df.columns]
    if missing_cols:
        lines.append(f"missing_columns: {', '.join(missing_cols)}")
        return "\n".join(lines)

    invalid_ohlc = (
        (df["High"] < df[["Open", "Close"]].max(axis=1))
        | (df["Low"] > df[["Open", "Close"]].min(axis=1))
        | (df["High"] < df["Low"])
    )
    lines.append(f"invalid_ohlc_rows: {int(invalid_ohlc.sum())}")

    close = df["Close"]
    returns = close.pct_change().abs()
    outliers = returns > 0.10
    lines.append(f"return_outliers_gt_10pct: {int(outliers.sum())}")
    if outliers.any():
        first_idx = outliers.idxmax()
        lines.append(f"first_outlier_date: {df.loc[first_idx, 'Date'].isoformat()}")

    zero_volume = (df["Volume"] == 0).sum()
    lines.append(f"zero_volume_rows: {int(zero_volume)}")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="EngineB/Data/BTC-USD_5m.csv")
    parser.add_argument("--out", default="EngineB/Outputs/QA/qa_report_5m.txt")
    args = parser.parse_args()

    df = _load_csv(Path(args.input))
    report = _qa_report(df, freq="5min")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
