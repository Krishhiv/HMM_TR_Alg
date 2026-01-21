import argparse
from pathlib import Path

import numpy as np
import pandas as pd


FEATURE_COLS = ["spread", "spread_vel", "vol_pct_500", "time_since_vwap"]


def _parse_horizons(raw: str) -> list[int]:
    if raw.strip() == "16-21":
        return list(range(16, 22))
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    return [int(p) for p in parts]


def _add_labels(df: pd.DataFrame, horizons: list[int]) -> pd.DataFrame:
    touch = df["touch_vwap"].fillna(0).astype(int).to_numpy()
    n = len(touch)
    out = df.copy()
    for h in horizons:
        label = np.full(n, np.nan, dtype=float)
        for i in range(0, n - h):
            label[i] = touch[i + 1 : i + h + 1].max()
        out[f"y_{h}"] = label
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Build label dataset for mean reversion logistic regression.")
    parser.add_argument(
        "--in-file",
        default="EngineB/Data/BTC-USD_15m_features.csv",
        help="Input feature CSV.",
    )
    parser.add_argument(
        "--out-file",
        default="EngineB/Data/BTC-USD_15m_lr_dataset.csv",
        help="Output dataset with labels.",
    )
    parser.add_argument(
        "--horizons",
        default="16-21",
        help="Horizons as '16-21' or comma list like '16,17,18'.",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.in_file)
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    for col in FEATURE_COLS + ["touch_vwap"]:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    horizons = _parse_horizons(args.horizons)
    out = _add_labels(df, horizons)

    Path(args.out_file).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out_file, index=False)
    print(f"[saved] labels -> {args.out_file}")


if __name__ == "__main__":
    main()
