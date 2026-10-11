
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
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

# Load the same training and test datasets used on Day 33
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
    raise ValueError("Target column is missing from the test dataset.")

# Separate features and target
X_train = train_df.drop(columns=[target])
y_train = train_df[target]

X_test = test_df.drop(columns=[target])
y_test = test_df[target]

# Make sure both datasets have the same feature columns
if set(X_train.columns) != set(X_test.columns):
    raise ValueError("Training and testing feature columns do not match.")

X_test = X_test[X_train.columns]

# Identify numeric and categorical features
numeric_columns = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()


def create_preprocessor():
    """Create preprocessing steps fitted only on training data."""

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ]
    )


# Compare both models on the same split
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(
        max_depth=5,
        random_state=42,
    ),
}

results = []
prediction_results = pd.DataFrame({
    "actual_survived": y_test.to_numpy()
})

for model_name, classifier in models.items():

    model = Pipeline(
        steps=[
            ("preprocessor", create_preprocessor()),
            ("classifier", classifier),
        ]
    )

    # Train using training data only
    model.fit(X_train, y_train)

    # Evaluate on the held-out test dataset
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    results.append({
        "model": model_name,
        "training_accuracy": accuracy_score(
            y_train, train_predictions
        ),
        "test_accuracy": accuracy_score(
            y_test, test_predictions
        ),
        "precision_weighted": precision_score(
            y_test, test_predictions,
            average="weighted", zero_division=0
        ),
        "recall_weighted": recall_score(
            y_test, test_predictions,
            average="weighted", zero_division=0
        ),
        "f1_weighted": f1_score(
            y_test, test_predictions,
            average="weighted", zero_division=0
        ),
    })

    prediction_results[
        model_name.lower().replace(" ", "_") + "_prediction"
    ] = test_predictions

# Save comparison results
comparison_df = pd.DataFrame(results)
comparison_file = OUTPUT_DIR / "model_comparison.csv"
comparison_df.to_csv(comparison_file, index=False)

# Save predictions from both models
predictions_file = OUTPUT_DIR / "model_comparison_predictions.csv"
prediction_results.to_csv(predictions_file, index=False)

# Display results
print("\n===== MODEL COMPARISON =====")
print(comparison_df.round(4).to_string(index=False))

best_model = comparison_df.loc[
    comparison_df["test_accuracy"].idxmax()
]

print(f"\nBest model by test accuracy: {best_model['model']}")
print(f"Test accuracy: {best_model['test_accuracy']:.4f}")

print("\nFiles saved:")
print(comparison_file)
print(predictions_file)
