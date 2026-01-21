import argparse
from pathlib import Path

import pandas as pd


REQUIRED_COLS = [
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "vwap",
    "sigma_100",
    "spread",
    "spread_vel",
    "atr_14",
    "vol_pct_500",
    "touch_vwap",
    "time_since_vwap",
]


def qa_features(path: Path) -> None:
    df = pd.read_csv(path)
    print(f"--- QA: {path} ---")

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    extra = [c for c in df.columns if c not in REQUIRED_COLS]
    print(f"missing_cols: {missing}")
    print(f"extra_cols: {extra}")

    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    dupes = int(df["Date"].duplicated().sum())
    expected = pd.date_range(df["Date"].iloc[0], df["Date"].iloc[-1], freq="15min", tz="UTC")
    missing_bars = int(len(expected) - df["Date"].nunique())

    print(f"start: {df['Date'].iloc[0]}")
    print(f"end:   {df['Date'].iloc[-1]}")
    print(f"dupes: {dupes}")
    print(f"missing_15m: {missing_bars}")

    nulls = df[REQUIRED_COLS].isna().sum().sort_values(ascending=False)
    print("\nnull_counts (top 10):")
    print(nulls.head(10).to_string())

    for col in ["spread", "atr_14", "vol_pct_500"]:
        if col in df.columns:
            s = df[col].dropna()
            if not s.empty:
                print(f"\n{col} stats: min={s.min():.4f} max={s.max():.4f} mean={s.mean():.4f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sanity QA for BTC 15m mean reversion features.")
    parser.add_argument(
        "--file",
        default="EngineB/Data/BTC-USD_15m_features.csv",
        help="Path to feature engineered CSV.",
    )
    args = parser.parse_args()
    qa_features(Path(args.file))


if __name__ == "__main__":
    main()
