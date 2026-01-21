import argparse
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


FEATURE_COLS = ["spread", "spread_vel", "vol_pct_500", "time_since_vwap"]


def _parse_horizons(raw: str) -> list[int]:
    if raw.strip() == "16-21":
        return list(range(16, 22))
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    return [int(p) for p in parts]


def _split_masks(df: pd.DataFrame, train_end: str, val_end: str) -> tuple[pd.Series, pd.Series, pd.Series]:
    train_end_dt = pd.to_datetime(train_end, utc=True)
    val_end_dt = pd.to_datetime(val_end, utc=True)
    idx = df["Date"]
    train_mask = idx <= train_end_dt
    val_mask = (idx > train_end_dt) & (idx <= val_end_dt)
    test_mask = idx > val_end_dt
    return train_mask, val_mask, test_mask


def _fit_calibrated_logreg(X_train, y_train, X_val, y_val):
    base = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("lr", LogisticRegression(max_iter=2000)),
        ]
    )
    base.fit(X_train, y_train)
    cal = CalibratedClassifierCV(base, method="sigmoid", cv="prefit")
    cal.fit(X_val, y_val)
    return cal


def main() -> None:
    parser = argparse.ArgumentParser(description="Train logistic regression models for MR labels (Option A).")
    parser.add_argument(
        "--data-file",
        default="EngineB/Data/BTC-USD_15m_lr_dataset.csv",
        help="Dataset with labels.",
    )
    parser.add_argument("--train-end", default="2019-12-31", help="Train end date (UTC).")
    parser.add_argument("--val-end", default="2021-12-31", help="Validation end date (UTC).")
    parser.add_argument("--horizons", default="16-21", help="Horizons list or range.")
    parser.add_argument("--out-dir", default="EngineB/Logistic-Reg/models", help="Model output dir.")
    parser.add_argument("--report-file", default="EngineB/Logistic-Reg/outputs/train_report.json")
    args = parser.parse_args()

    df = pd.read_csv(args.data_file)
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)

    for col in FEATURE_COLS:
        if col not in df.columns:
            raise ValueError(f"Missing required feature column: {col}")

    horizons = _parse_horizons(args.horizons)
    models_dir = Path(args.out_dir)
    models_dir.mkdir(parents=True, exist_ok=True)
    Path(args.report_file).parent.mkdir(parents=True, exist_ok=True)

    report = {
        "data_file": args.data_file,
        "train_end": args.train_end,
        "val_end": args.val_end,
        "features": FEATURE_COLS,
        "models": {},
    }

    for h in horizons:
        label_col = f"y_{h}"
        if label_col not in df.columns:
            raise ValueError(f"Missing label column: {label_col}")

        df_h = df.dropna(subset=FEATURE_COLS + [label_col]).copy()
        train_mask, val_mask, test_mask = _split_masks(df_h, args.train_end, args.val_end)

        if train_mask.sum() == 0 or val_mask.sum() == 0 or test_mask.sum() == 0:
            raise ValueError(f"Insufficient rows for horizon {h} after split.")

        X_train = df_h.loc[train_mask, FEATURE_COLS].values
        y_train = df_h.loc[train_mask, label_col].astype(int).values
        X_val = df_h.loc[val_mask, FEATURE_COLS].values
        y_val = df_h.loc[val_mask, label_col].astype(int).values
        X_test = df_h.loc[test_mask, FEATURE_COLS].values
        y_test = df_h.loc[test_mask, label_col].astype(int).values

        model = _fit_calibrated_logreg(X_train, y_train, X_val, y_val)

        p_val = model.predict_proba(X_val)[:, 1]
        p_test = model.predict_proba(X_test)[:, 1]

        metrics = {
            "val_auc": float(roc_auc_score(y_val, p_val)),
            "val_log_loss": float(log_loss(y_val, p_val)),
            "val_brier": float(brier_score_loss(y_val, p_val)),
            "test_auc": float(roc_auc_score(y_test, p_test)),
            "test_log_loss": float(log_loss(y_test, p_test)),
            "test_brier": float(brier_score_loss(y_test, p_test)),
            "train_rows": int(len(y_train)),
            "val_rows": int(len(y_val)),
            "test_rows": int(len(y_test)),
        }

        model_path = models_dir / f"model_y_{h}.joblib"
        joblib.dump(
            {
                "model": model,
                "horizon": h,
                "features": FEATURE_COLS,
                "train_end": args.train_end,
                "val_end": args.val_end,
            },
            model_path,
        )

        report["models"][f"y_{h}"] = {
            "model_path": str(model_path),
            "metrics": metrics,
        }
        print(f"[saved] model y_{h} -> {model_path}")

    with open(args.report_file, "w") as f:
        json.dump(report, f, indent=2)
    print(f"[saved] report -> {args.report_file}")


if __name__ == "__main__":
    main()
