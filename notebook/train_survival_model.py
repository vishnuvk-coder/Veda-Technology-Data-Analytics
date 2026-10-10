
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

TRAIN_FILE = OUTPUT_DIR / "survival_train.csv"
TEST_FILE = OUTPUT_DIR / "survival_test.csv"

# Load the prepared datasets
train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)

# Find the target column without depending on capitalization
target_matches = [
    col for col in train_df.columns
    if col.lower() == "survived"
]

if not target_matches:
    raise ValueError(
        "Target column 'survived' was not found in the training CSV."
    )

target = target_matches[0]

if target not in test_df.columns:
    raise ValueError("The test dataset does not contain the target column.")

# Separate features (X) and target (y)
X_train = train_df.drop(columns=[target])
y_train = train_df[target]

X_test = test_df.drop(columns=[target])
y_test = test_df[target]

# Check that training and testing features match
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
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore"),
        ),
    ]
)

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_pipeline, numeric_columns),
        ("categorical", categorical_pipeline, categorical_columns),
    ]
)

# Build the machine learning pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)

# Train the model
model.fit(X_train, y_train)

# Predict outcomes for the test dataset
y_pred = model.predict(X_test)

# Calculate evaluation metrics
metrics = {
    "model": "Logistic Regression",
    "training_rows": len(X_train),
    "testing_rows": len(X_test),
    "features_before_encoding": X_train.shape[1],
    "accuracy": accuracy_score(y_test, y_pred),
    "precision_weighted": precision_score(
        y_test, y_pred, average="weighted", zero_division=0
    ),
    "recall_weighted": recall_score(
        y_test, y_pred, average="weighted", zero_division=0
    ),
    "f1_weighted": f1_score(
        y_test, y_pred, average="weighted", zero_division=0
    ),
}

# Save evaluation metrics
metrics_file = OUTPUT_DIR / "logistic_regression_metrics.csv"
pd.DataFrame([metrics]).to_csv(metrics_file, index=False)

# Save predictions alongside actual outcomes
predictions = X_test.copy()
predictions["actual_survived"] = y_test.to_numpy()
predictions["predicted_survived"] = y_pred

predictions_file = OUTPUT_DIR / "survival_test_predictions.csv"
predictions.to_csv(predictions_file, index=False)

# Save the confusion matrix
labels = sorted(pd.concat([y_test, pd.Series(y_pred)]).unique())
matrix = confusion_matrix(y_test, y_pred, labels=labels)

matrix_df = pd.DataFrame(
    matrix,
    index=[f"actual_{label}" for label in labels],
    columns=[f"predicted_{label}" for label in labels],
)

matrix_file = OUTPUT_DIR / "confusion_matrix.csv"
matrix_df.to_csv(matrix_file)

# Print the results
print("\n===== LOGISTIC REGRESSION RESULTS =====")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print(f"Accuracy: {metrics['accuracy']:.4f}")
print(f"Weighted precision: {metrics['precision_weighted']:.4f}")
print(f"Weighted recall: {metrics['recall_weighted']:.4f}")
print(f"Weighted F1-score: {metrics['f1_weighted']:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(matrix_df)

print("\nFiles saved:")
print(metrics_file)
print(predictions_file)
print(matrix_file)
