
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Project paths
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "output" / "titanic_cleaned.csv"
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TARGET = "survived"
THRESHOLDS = [0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]


def main():
    print("Day 39: Prediction Threshold Analysis")

    df = pd.read_csv(DATA_PATH)

    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' not found.")

    # Separate features and target
    X = df.drop(columns=[TARGET]).copy()
    y = df[TARGET].copy()

    # Use numeric columns for this baseline model
    X = X.select_dtypes(include="number")

    if X.empty:
        raise ValueError("No numeric feature columns were found.")

    # Reproduce a stratified 80/20 split with random_state=42
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            class_weight="balanced",
        )),
    ])

    model.fit(X_train, y_train)

    # Probability of survival (class 1)
    classes = list(model.named_steps["classifier"].classes_)
    if 1 not in classes:
        raise ValueError("The target must contain survival class 1.")

    survival_index = classes.index(1)
    probabilities = model.predict_proba(X_test)[:, survival_index]

    rows = []

    for threshold in THRESHOLDS:
        predictions = (probabilities >= threshold).astype(int)

        rows.append({
            "threshold": threshold,
            "accuracy": accuracy_score(y_test, predictions),
            "precision_survived": precision_score(
                y_test, predictions, zero_division=0
            ),
            "recall_survived": recall_score(
                y_test, predictions, zero_division=0
            ),
            "f1_survived": f1_score(
                y_test, predictions, zero_division=0
            ),
            "predicted_survivors": int(predictions.sum()),
            "actual_survivors": int((y_test == 1).sum()),
        })

    results = pd.DataFrame(rows)
    csv_path = OUTPUT_DIR / "threshold_analysis.csv"
    results.to_csv(csv_path, index=False)

    # Plot the metrics against the threshold
    plt.figure(figsize=(10, 6))

    for column in [
        "accuracy",
        "precision_survived",
        "recall_survived",
        "f1_survived",
    ]:
        plt.plot(
            results["threshold"],
            results[column],
            marker="o",
            label=column.replace("_", " ").title(),
        )

    plt.xlabel("Prediction Threshold")
    plt.ylabel("Score")
    plt.title("Day 39: Model Performance by Prediction Threshold")
    plt.ylim(0, 1.05)
    plt.xticks(THRESHOLDS)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    chart_path = OUTPUT_DIR / "threshold_analysis.png"
    plt.savefig(chart_path, dpi=150)
    plt.close()

    print("\nThreshold comparison:")
    print(results.round(4).to_string(index=False))
    print(f"\nSaved: {csv_path}")
    print(f"Saved: {chart_path}")
    print("\nDay 39 analysis finished.")


if __name__ == "__main__":
    main()
