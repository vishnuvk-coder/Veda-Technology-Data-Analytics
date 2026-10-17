
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project paths
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

INPUT_FILE = OUTPUT_DIR / "threshold_analysis.csv"
SUMMARY_FILE = OUTPUT_DIR / "threshold_selection_summary.csv"
CHART_FILE = OUTPUT_DIR / "threshold_selection_comparison.png"


def main():
    print("Day 40: Threshold Selection Analysis")

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {INPUT_FILE}. Run the Day 39 script first."
        )

    df = pd.read_csv(INPUT_FILE)

    required_columns = [
        "threshold",
        "accuracy",
        "precision_survived",
        "recall_survived",
        "f1_survived",
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df[required_columns] = df[required_columns].apply(
        pd.to_numeric, errors="raise"
    )

    if df.empty:
        raise ValueError("The threshold results file is empty.")

    # Identify the best threshold for each metric
    metric_columns = {
        "accuracy": "Best Accuracy",
        "precision_survived": "Best Precision",
        "recall_survived": "Best Recall",
        "f1_survived": "Best F1 Score",
    }

    summary_rows = []

    for metric, label in metric_columns.items():
        best_row = df.loc[df[metric].idxmax()]

        summary_rows.append({
            "selection_metric": label,
            "selected_threshold": best_row["threshold"],
            "score": best_row[metric],
            "accuracy": best_row["accuracy"],
            "precision_survived": best_row["precision_survived"],
            "recall_survived": best_row["recall_survived"],
            "f1_survived": best_row["f1_survived"],
            "reason": f"Highest {label.lower()} among tested thresholds",
        })

    summary = pd.DataFrame(summary_rows)
    summary.to_csv(SUMMARY_FILE, index=False)

    # For this educational analysis, use F1 as the balanced metric
    best_f1_row = df.loc[df["f1_survived"].idxmax()]
    selected_threshold = best_f1_row["threshold"]

    # Plot metric comparisons
    plt.figure(figsize=(10, 6))

    plot_metrics = {
        "accuracy": "Accuracy",
        "precision_survived": "Precision",
        "recall_survived": "Recall",
        "f1_survived": "F1 Score",
    }

    for column, label in plot_metrics.items():
        plt.plot(
            df["threshold"],
            df[column],
            marker="o",
            label=label,
        )

    plt.axvline(
        selected_threshold,
        linestyle="--",
        label=f"Best F1 threshold: {selected_threshold:.2f}",
    )

    plt.xlabel("Prediction Threshold")
    plt.ylabel("Score")
    plt.title("Day 40: Comparing Threshold Selection Metrics")
    plt.xticks(df["threshold"])
    plt.ylim(0, 1.05)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()

    print("\nBest threshold for each metric:")
    print(
        summary[
            ["selection_metric", "selected_threshold", "score"]
        ].to_string(index=False)
    )

    print(f"\nF1-based threshold recommendation: {selected_threshold:.2f}")
    print(f"Saved summary: {SUMMARY_FILE}")
    print(f"Saved chart: {CHART_FILE}")
    print("\nDay 40 analysis finished.")


if __name__ == "__main__":
    main()
