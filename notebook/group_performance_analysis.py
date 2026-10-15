
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

TRAIN_FILE = OUTPUT_DIR / "survival_train.csv"
TEST_FILE = OUTPUT_DIR / "survival_test.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load training and test data
train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)

target_matches = [
    col for col in train_df.columns
    if col.lower() == "survived"
]

if not target_matches:
    raise ValueError("Target column 'survived' was not found.")

target = target_matches[0]

if target not in test_df.columns:
    raise ValueError("Target column is missing from test data.")

X_train = train_df.drop(columns=[target])
y_train = train_df[target]

X_test = test_df.drop(columns=[target])
y_test = test_df[target]

if set(X_train.columns) != set(X_test.columns):
    raise ValueError("Training and testing columns do not match.")

X_test = X_test[X_train.columns]

# Identify feature types
numeric_columns = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

# Preprocessing pipelines
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_columns),
    ("categorical", categorical_pipeline, categorical_columns),
])

# Build and train the Logistic Regression model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)

# Predict on the held-out test data
predictions = model.predict(X_test)

evaluation_df = X_test.reset_index(drop=True).copy()
evaluation_df["actual_survived"] = y_test.reset_index(drop=True)
evaluation_df["predicted_survived"] = predictions

evaluation_df["prediction_correct"] = (
    evaluation_df["actual_survived"]
    == evaluation_df["predicted_survived"]
)

# Create age groups when age is available
if "age" in evaluation_df.columns:
    evaluation_df["age_group"] = pd.cut(
        evaluation_df["age"],
        bins=[0, 12, 18, 35, 60, float("inf")],
        labels=[
            "Child (0-12)",
            "Teen (13-18)",
            "Young adult (19-35)",
            "Adult (36-60)",
            "Senior (60+)",
        ],
        include_lowest=True,
    ).astype("object")

    evaluation_df.loc[
        evaluation_df["age"].isna(), "age_group"
    ] = "Unknown"

# Define groups to analyze
group_columns = [
    col for col in [
        "sex",
        "pclass",
        "age_group",
        "embarked",
        "alone",
    ]
    if col in evaluation_df.columns
]

if not group_columns:
    raise ValueError("No expected passenger group columns were found.")

# Calculate metrics for each group
rows = []

for feature in group_columns:
    for group_value, group_df in evaluation_df.groupby(
        feature, dropna=False, observed=True
    ):
        actual = group_df["actual_survived"]
        predicted = group_df["predicted_survived"]

        rows.append({
            "group_feature": feature,
            "group_value": (
                "Unknown" if pd.isna(group_value) else str(group_value)
            ),
            "passenger_count": len(group_df),
            "accuracy": round(
                accuracy_score(actual, predicted), 4
            ),
            "precision_survived": round(
                precision_score(
                    actual, predicted, pos_label=1, zero_division=0
                ), 4
            ),
            "recall_survived": round(
                recall_score(
                    actual, predicted, pos_label=1, zero_division=0
                ), 4
            ),
            "f1_survived": round(
                f1_score(
                    actual, predicted, pos_label=1, zero_division=0
                ), 4
            ),
            "incorrect_predictions": int(
                (actual != predicted).sum()
            ),
            "error_rate": round(
                (actual != predicted).mean(), 4
            ),
        })

report = pd.DataFrame(rows)

# Save complete group performance report
report_file = OUTPUT_DIR / "group_performance_report.csv"
report.to_csv(report_file, index=False)

# Create accuracy chart
chart_df = report.copy()
chart_df["chart_label"] = (
    chart_df["group_feature"].astype(str)
    + " = "
    + chart_df["group_value"].astype(str)
)

chart_df = chart_df.sort_values("accuracy")

plt.figure(figsize=(11, max(6, len(chart_df) * 0.35)))

plt.barh(
    chart_df["chart_label"],
    chart_df["accuracy"],
)

plt.xlim(0, 1)
plt.xlabel("Accuracy")
plt.ylabel("Passenger group")
plt.title("Day 38 - Model Accuracy by Passenger Group")
plt.tight_layout()

chart_file = OUTPUT_DIR / "group_performance_comparison.png"
plt.savefig(chart_file, dpi=300, bbox_inches="tight")
plt.close()

# Save a separate summary of group sizes and error rates
error_summary = report[[
    "group_feature",
    "group_value",
    "passenger_count",
    "incorrect_predictions",
    "error_rate",
]].copy()

error_file = OUTPUT_DIR / "group_error_summary.csv"
error_summary.to_csv(error_file, index=False)

# Print results
print("\n===== DAY 38: GROUP PERFORMANCE ANALYSIS =====")
print(f"Training passengers: {len(X_train)}")
print(f"Testing passengers: {len(X_test)}")
print(f"Overall accuracy: {accuracy_score(y_test, predictions):.2%}")

print("\n===== PERFORMANCE BY GROUP =====")
print(
    report.sort_values(
        ["group_feature", "accuracy"],
        ascending=[True, False],
    ).to_string(index=False)
)

print("\nFiles saved:")
print(report_file)
print(error_file)
print(chart_file)
