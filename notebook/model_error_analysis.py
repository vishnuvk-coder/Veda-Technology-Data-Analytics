
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

TRAIN_FILE = OUTPUT_DIR / "survival_train.csv"
TEST_FILE = OUTPUT_DIR / "survival_test.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)

# Find target column
target_matches = [
    col for col in train_df.columns
    if col.lower() == "survived"
]

if not target_matches:
    raise ValueError("Target column 'survived' was not found.")

target = target_matches[0]

if target not in test_df.columns:
    raise ValueError("Target column is missing from test data.")

# Separate features and target
X_train = train_df.drop(columns=[target])
y_train = train_df[target]

X_test = test_df.drop(columns=[target])
y_test = test_df[target]

if set(X_train.columns) != set(X_test.columns):
    raise ValueError("Training and testing columns do not match.")

X_test = X_test[X_train.columns]

# Identify numeric and categorical columns
numeric_columns = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

# Preprocessing
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

# Logistic Regression model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000)),
])

# Train and predict
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

# Find the probability column for the positive class (1)
classes = list(model.named_steps["classifier"].classes_)

if 1 not in classes:
    raise ValueError("The model does not contain the expected class 1.")

survived_probability = probabilities[:, classes.index(1)]

# Save all test predictions
results = X_test.reset_index(drop=True).copy()
results["actual_survived"] = y_test.reset_index(drop=True)
results["predicted_survived"] = predictions
results["survived_probability"] = survived_probability.round(4)

results["prediction_correct"] = (
    results["actual_survived"] == results["predicted_survived"]
)

def error_type(row):
    if row["actual_survived"] == row["predicted_survived"]:
        return "Correct"
    if row["actual_survived"] == 0:
        return "False Positive"
    return "False Negative"

results["prediction_result"] = results.apply(error_type, axis=1)

# Save complete prediction results
results_file = OUTPUT_DIR / "prediction_results.csv"
results.to_csv(results_file, index=False)

# Save only incorrect predictions
errors = results[
    results["prediction_correct"] == False
].copy()

errors_file = OUTPUT_DIR / "misclassified_passengers.csv"
errors.to_csv(errors_file, index=False)

# Overall error summary
total = len(results)
incorrect = len(errors)
correct = total - incorrect
accuracy = accuracy_score(y_test, predictions)

summary_rows = [
    {"metric": "Total test passengers", "value": total},
    {"metric": "Correct predictions", "value": correct},
    {"metric": "Incorrect predictions", "value": incorrect},
    {"metric": "Accuracy percentage", "value": round(accuracy * 100, 2)},
    {
        "metric": "False positives",
        "value": int((results["prediction_result"] == "False Positive").sum()),
    },
    {
        "metric": "False negatives",
        "value": int((results["prediction_result"] == "False Negative").sum()),
    },
]

# Add error rates by available passenger features
group_summaries = []

for feature in ["sex", "pclass", "embarked", "alone"]:
    if feature in results.columns:
        grouped = results.groupby(
            feature, dropna=False
        )["prediction_correct"].agg(["count", "sum"])

        for group_value, row in grouped.iterrows():
            group_summaries.append({
                "metric": f"Error rate by {feature}",
                "group": str(group_value),
                "passengers": int(row["count"]),
                "incorrect_predictions": int(row["count"] - row["sum"]),
                "error_rate_percent": round(
                    (row["count"] - row["sum"]) / row["count"] * 100, 2
                ),
            })

summary_file = OUTPUT_DIR / "error_analysis_summary.csv"

pd.DataFrame(summary_rows).to_csv(
    summary_file, index=False
)

if group_summaries:
    pd.DataFrame(group_summaries).to_csv(
        OUTPUT_DIR / "error_rates_by_group.csv",
        index=False,
    )

# Plot confusion matrix
matrix = confusion_matrix(
    y_test, predictions, labels=[0, 1]
)

fig, ax = plt.subplots(figsize=(6, 5))
image = ax.imshow(matrix)

ax.set_title("Day 37 - Confusion Matrix")
ax.set_xlabel("Predicted outcome")
ax.set_ylabel("Actual outcome")
ax.set_xticks([0, 1], labels=["Did not survive", "Survived"])
ax.set_yticks([0, 1], labels=["Did not survive", "Survived"])

for i in range(2):
    for j in range(2):
        ax.text(j, i, str(matrix[i, j]), ha="center", va="center")

fig.colorbar(image, ax=ax, label="Passenger count")
fig.tight_layout()

chart_file = OUTPUT_DIR / "error_analysis_confusion_matrix.png"
fig.savefig(chart_file, dpi=300, bbox_inches="tight")
plt.close(fig)

# Print results
print("\n===== DAY 37: MODEL ERROR ANALYSIS =====")
print(f"Total test passengers: {total}")
print(f"Correct predictions: {correct}")
print(f"Incorrect predictions: {incorrect}")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\n===== ERROR TYPES =====")
print(results["prediction_result"].value_counts().to_string())

print("\n===== CONFUSION MATRIX =====")
print(pd.DataFrame(
    matrix,
    index=["Actual 0: Did not survive", "Actual 1: Survived"],
    columns=["Predicted 0", "Predicted 1"],
).to_string())

print("\n===== MISCLASSIFIED PASSENGERS (FIRST 10) =====")
if errors.empty:
    print("No incorrect predictions were found.")
else:
    display_columns = [
        col for col in [
            "sex", "age", "pclass", "actual_survived",
            "predicted_survived", "survived_probability",
            "prediction_result",
        ]
        if col in errors.columns
    ]
    print(errors[display_columns].head(10).to_string(index=False))

print("\nFiles saved:")
print(results_file)
print(errors_file)
print(summary_file)
print(OUTPUT_DIR / "error_rates_by_group.csv")
print(chart_file)
