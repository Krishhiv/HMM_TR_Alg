from __future__ import annotations

import argparse
from datetime import timezone
from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "Date" not in df.columns:
        raise ValueError("Expected 'Date' column in CSV")
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def qa_report(df: pd.DataFrame, freq: str) -> str:
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

    required_cols = [
        "Open", "High", "Low", "Close", "Volume",
        "FairValue", "EWMAVol", "ZScore", "RangePct",
        "LiquidityCostProxy", "Hurst15m",
    ]
    missing_cols = [c for c in required_cols if c not in df.columns]
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

    nan_counts = df[["FairValue", "EWMAVol", "ZScore", "Hurst15m"]].isna().sum()
    lines.append(f"nan_fair_value: {int(nan_counts['FairValue'])}")
    lines.append(f"nan_ewma_vol: {int(nan_counts['EWMAVol'])}")
    lines.append(f"nan_zscore: {int(nan_counts['ZScore'])}")
    lines.append(f"nan_hurst15m: {int(nan_counts['Hurst15m'])}")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-5m", default="EngineB/Data/Feature-Engineered/BTC-USD_5m_features.csv")
    parser.add_argument("--input-15m", default="EngineB/Data/Feature-Engineered/BTC-USD_15m_features.csv")
    parser.add_argument("--out-dir", default="EngineB/Outputs/QA")
    args = parser.parse_args()

    df_5m = load_csv(Path(args.input_5m))
    df_15m = load_csv(Path(args.input_15m))

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    report_5m = qa_report(df_5m, freq="5min")
    report_15m = qa_report(df_15m, freq="15min")

    out_5m = out_dir / "qa_report_5m_fe.txt"
    out_15m = out_dir / "qa_report_15m_fe.txt"

    out_5m.write_text(report_5m)
    out_15m.write_text(report_15m)

    print(f"Wrote {out_5m}")
    print(f"Wrote {out_15m}")


if __name__ == "__main__":
    main()
