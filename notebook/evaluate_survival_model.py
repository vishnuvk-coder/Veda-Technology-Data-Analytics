
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
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

# Load prepared datasets
train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)

# Find the target column
target_matches = [
    col for col in train_df.columns
    if col.lower() == "survived"
]

if not target_matches:
    raise ValueError("Target column 'survived' was not found.")

target = target_matches[0]

if target not in test_df.columns:
    raise ValueError("The test dataset is missing the target column.")

# Separate features and target
X_train = train_df.drop(columns=[target])
y_train = train_df[target]

X_test = test_df.drop(columns=[target])
y_test = test_df[target]

# Validate feature columns
if set(X_train.columns) != set(X_test.columns):
    raise ValueError(
        "Training and testing feature columns do not match."
    )

X_test = X_test[X_train.columns]

# Identify numeric and categorical columns
numeric_columns = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

# Prepare numeric features
numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

# Prepare categorical features
categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_pipeline, numeric_columns),
        ("categorical", categorical_pipeline, categorical_columns),
    ]
)

# Build and train Logistic Regression
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)

model.fit(X_train, y_train)

# Get survival probabilities
classes = list(model.named_steps["classifier"].classes_)

if 1 not in classes:
    raise ValueError("The model does not contain survival class 1.")

survival_index = classes.index(1)
survival_probabilities = model.predict_proba(X_test)[:, survival_index]

# Compare different classification thresholds
thresholds = [0.30, 0.40, 0.50, 0.60, 0.70]
threshold_results = []

for threshold in thresholds:
    predictions = (
        survival_probabilities >= threshold
    ).astype(int)

    threshold_results.append({
        "threshold": threshold,
        "accuracy": accuracy_score(y_test, predictions),
        "precision_survived": precision_score(
            y_test, predictions, pos_label=1, zero_division=0
        ),
        "recall_survived": recall_score(
            y_test, predictions, pos_label=1, zero_division=0
        ),
        "f1_survived": f1_score(
            y_test, predictions, pos_label=1, zero_division=0
        ),
    })

threshold_df = pd.DataFrame(threshold_results)

threshold_file = OUTPUT_DIR / "threshold_comparison.csv"
threshold_df.to_csv(threshold_file, index=False)

# Evaluate using the standard threshold of 0.50
default_threshold = 0.50

default_predictions = (
    survival_probabilities >= default_threshold
).astype(int)

# Save the classification report
report = classification_report(
    y_test,
    default_predictions,
    labels=[0, 1],
    target_names=["Did not survive", "Survived"],
    output_dict=True,
    zero_division=0,
)

report_df = pd.DataFrame(report).transpose()

report_file = OUTPUT_DIR / "classification_report.csv"
report_df.to_csv(report_file)

# Save the confusion matrix without overwriting the existing file
matrix = confusion_matrix(
    y_test, default_predictions, labels=[0, 1]
)

matrix_df = pd.DataFrame(
    matrix,
    index=["actual_0_not_survived", "actual_1_survived"],
    columns=["predicted_0_not_survived", "predicted_1_survived"],
)

matrix_file = OUTPUT_DIR / "evaluation_confusion_matrix.csv"
matrix_df.to_csv(matrix_file)

# Save test predictions and survival probabilities
predictions_df = X_test.copy()
predictions_df["actual_survived"] = y_test.to_numpy()
predictions_df["survival_probability"] = survival_probabilities
predictions_df["predicted_survived_at_0_50"] = default_predictions

predictions_file = OUTPUT_DIR / "survival_test_evaluation.csv"
predictions_df.to_csv(predictions_file, index=False)

# Display results
print("\n===== MODEL EVALUATION =====")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print(f"Features before encoding: {X_train.shape[1]}")

print("\n===== THRESHOLD COMPARISON =====")
print(threshold_df.round(4).to_string(index=False))

print("\n===== CLASSIFICATION REPORT =====")
print(classification_report(
    y_test,
    default_predictions,
    labels=[0, 1],
    target_names=["Did not survive", "Survived"],
    zero_division=0,
))

print("\n===== CONFUSION MATRIX =====")
print(matrix_df)

print("\nFiles saved:")
print(threshold_file)
print(report_file)
print(matrix_file)
print(predictions_file)
