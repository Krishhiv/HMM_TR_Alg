import argparse
from pathlib import Path

import pandas as pd


EXPECTED_COLUMNS = [
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "ema_50",
    "ema_100",
    "tr",
    "atr_14",
    "atr_50_ma",
    "high_20",
    "low_20",
    "volume_ma_20",
    "volume_ratio",
    "roc_3",
    "clv",
    "hour_utc",
    "open_next",
    "timeframe",
]


def _load_features(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.rename(columns={c: c.strip().lower() for c in df.columns})
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df


def _check_columns(df: pd.DataFrame, name: str) -> None:
    cols = df.columns.tolist()
    missing = [c for c in EXPECTED_COLUMNS if c not in cols]
    extra = [c for c in cols if c not in EXPECTED_COLUMNS]
    print(f"[{name}] columns: {len(cols)}")
    if missing:
        print(f"[{name}] missing columns: {missing}")
    if extra:
        print(f"[{name}] extra columns: {extra}")


def _check_monotonic(df: pd.DataFrame, name: str) -> None:
    if "timestamp" not in df.columns:
        print(f"[{name}] timestamp column not found")
        return
    monotonic = df["timestamp"].is_monotonic_increasing
    print(f"[{name}] timestamp monotonic increasing: {monotonic}")


def _check_nulls(df: pd.DataFrame, name: str) -> None:
    null_counts = df.isna().sum()
    total_nulls = int(null_counts.sum())
    print(f"[{name}] total nulls: {total_nulls}")
    if total_nulls:
        top = null_counts[null_counts > 0].sort_values(ascending=False).head(10)
        print(f"[{name}] nulls by column (top 10):")
        for col, val in top.items():
            print(f"  - {col}: {int(val)}")


def _check_ranges(df: pd.DataFrame, name: str) -> None:
    if {"high", "low", "open", "close"}.issubset(df.columns):
        invalid = (df["high"] < df["low"]) | (df["open"] <= 0) | (df["close"] <= 0)
        print(f"[{name}] price sanity failures: {int(invalid.sum())}")
    if "volume" in df.columns:
        neg_vol = (df["volume"] < 0).sum()
        print(f"[{name}] negative volume rows: {int(neg_vol)}")


def _check_timeframe(df: pd.DataFrame, name: str, expected: str) -> None:
    if "timeframe" not in df.columns:
        print(f"[{name}] timeframe column not found")
        return
    invalid = (df["timeframe"] != expected).sum()
    print(f"[{name}] timeframe mismatches: {int(invalid)}")


def _print_last_row(df: pd.DataFrame, name: str) -> None:
    if "timestamp" in df.columns and not df.empty:
        print(f"[{name}] first: {df['timestamp'].iloc[0]}")
        print(f"[{name}] last:  {df['timestamp'].iloc[-1]}")


def qa_dataset(path: Path, expected_timeframe: str) -> None:
    name = path.name
    df = _load_features(path)
    _check_columns(df, name)
    _check_monotonic(df, name)
    _check_nulls(df, name)
    _check_ranges(df, name)
    _check_timeframe(df, name, expected_timeframe)
    _print_last_row(df, name)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="QA checks for feature engineered BTC datasets."
    )
    parser.add_argument(
        "--features-dir",
        default="velocity_breakout/data/feature_engineered",
        help="Directory containing feature CSVs.",
    )
    args = parser.parse_args()

    features_dir = Path(args.features_dir)
    path_15m = features_dir / "BTC-USD_15m_features.csv"
    path_1h = features_dir / "BTC-USD_1h_features.csv"

    if not path_15m.exists() or not path_1h.exists():
        raise FileNotFoundError(
            "Feature CSVs not found. Run feature_engineering.py first."
        )

    qa_dataset(path_15m, expected_timeframe="15m")
    qa_dataset(path_1h, expected_timeframe="1h")


if __name__ == "__main__":
    main()
