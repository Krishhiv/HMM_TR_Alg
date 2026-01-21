import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze LR model metrics and select best horizon.")
    parser.add_argument(
        "--report-file",
        default="EngineB/Logistic-Reg/outputs/train_report.json",
        help="Path to training report JSON.",
    )
    parser.add_argument(
        "--out-file",
        default="EngineB/Logistic-Reg/outputs/model_analysis.txt",
        help="Output analysis text file.",
    )
    args = parser.parse_args()

    report_path = Path(args.report_file)
    if not report_path.exists():
        raise FileNotFoundError(f"Missing report file: {report_path}")

    report = json.loads(report_path.read_text())
    models = report.get("models", {})
    if not models:
        raise ValueError("No models found in report.")

    rows = []
    for label, payload in models.items():
        metrics = payload.get("metrics", {})
        rows.append(
            {
                "label": label,
                "model_path": payload.get("model_path", ""),
                "test_auc": metrics.get("test_auc"),
                "test_log_loss": metrics.get("test_log_loss"),
                "test_brier": metrics.get("test_brier"),
                "val_auc": metrics.get("val_auc"),
                "val_log_loss": metrics.get("val_log_loss"),
                "val_brier": metrics.get("val_brier"),
            }
        )

    # Primary selection: maximize test_auc, then minimize test_log_loss, then minimize test_brier
    rows_sorted = sorted(
        rows,
        key=lambda r: (
            -(r["test_auc"] if r["test_auc"] is not None else -1),
            r["test_log_loss"] if r["test_log_loss"] is not None else 1e9,
            r["test_brier"] if r["test_brier"] is not None else 1e9,
        ),
    )
    best = rows_sorted[0]

    lines = []
    lines.append("=== Logistic Regression Model Analysis ===")
    lines.append(f"Report: {report_path}")
    lines.append("")
    lines.append("Per-horizon metrics (test):")
    for r in rows_sorted:
        lines.append(
            f"- {r['label']}: AUC={r['test_auc']:.4f} "
            f"logloss={r['test_log_loss']:.4f} brier={r['test_brier']:.4f} "
            f"(model={r['model_path']})"
        )

    lines.append("")
    lines.append("Selection rule:")
    lines.append("- Maximize test AUC")
    lines.append("- Tie-breaker: minimize test log loss")
    lines.append("- Tie-breaker: minimize test Brier score")
    lines.append("")
    lines.append("Best model:")
    lines.append(
        f"- {best['label']} | AUC={best['test_auc']:.4f} "
        f"logloss={best['test_log_loss']:.4f} brier={best['test_brier']:.4f}"
    )
    lines.append(f"- path: {best['model_path']}")

    out_path = Path(args.out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines))
    print(f"[saved] {out_path}")


if __name__ == "__main__":
    main()
