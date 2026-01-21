import argparse
from pathlib import Path

import joblib
import numpy as np
import pandas as pd


FEATURE_COLS = ["spread", "spread_vel", "vol_pct_500", "time_since_vwap"]


def _load_models(models_dir: Path) -> dict[int, object]:
    models = {}
    for path in sorted(models_dir.glob("model_y_*.joblib")):
        payload = joblib.load(path)
        horizon = int(payload["horizon"])
        models[horizon] = payload["model"]
    if not models:
        raise ValueError(f"No models found in {models_dir}")
    return models


def main() -> None:
    parser = argparse.ArgumentParser(description="Score 15m features with LR ensemble (Option A).")
    parser.add_argument(
        "--features-file",
        default="EngineB/Data/BTC-USD_15m_features.csv",
        help="Feature file to score.",
    )
    parser.add_argument(
        "--models-dir",
        default="EngineB/Logistic-Reg/models",
        help="Directory with trained models.",
    )
    parser.add_argument(
        "--out-file",
        default="EngineB/Data/BTC-USD_15m_lr_scored.csv",
        help="Output file with probabilities.",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.features_file)
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")

    for col in FEATURE_COLS:
        if col not in df.columns:
            raise ValueError(f"Missing required feature column: {col}")

    models = _load_models(Path(args.models_dir))
    horizons = sorted(models.keys())

    mask = df[FEATURE_COLS].notna().all(axis=1)
    X = df.loc[mask, FEATURE_COLS].values

    probs = {}
    for h in horizons:
        probs[h] = models[h].predict_proba(X)[:, 1]
        df.loc[mask, f"P_{h}"] = probs[h]

    p_stack = np.column_stack([probs[h] for h in horizons])
    df.loc[mask, "P_mean"] = p_stack.mean(axis=1)
    df.loc[mask, "P_max"] = p_stack.max(axis=1)

    out_path = Path(args.out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"[saved] scored -> {out_path}")


if __name__ == "__main__":
    main()
