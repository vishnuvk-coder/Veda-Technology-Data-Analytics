
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

TRAIN_FILE = OUTPUT_DIR / "survival_train.csv"
TEST_FILE = OUTPUT_DIR / "survival_test.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load training and testing data
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

# Identify numeric and categorical features
numeric_columns = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

# Preprocess numeric features
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

# Preprocess categorical features
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

# Combine preprocessing
preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_columns),
    ("categorical", categorical_pipeline, categorical_columns),
])

# Build the same Logistic Regression model as Day 35
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000)),
])

# Train model using training data only
model.fit(X_train, y_train)

# Measure feature importance on held-out test data
importance = permutation_importance(
    model,
    X_test,
    y_test,
    scoring="accuracy",
    n_repeats=20,
    random_state=42,
    n_jobs=1,
)

# Create results table
importance_df = pd.DataFrame({
    "feature": X_test.columns,
    "importance_mean": importance.importances_mean,
    "importance_std": importance.importances_std,
})

importance_df = importance_df.sort_values(
    "importance_mean",
    ascending=False,
)

# Save results as CSV
csv_file = OUTPUT_DIR / "feature_importance.csv"
importance_df.to_csv(csv_file, index=False)

# Create feature importance chart
plot_df = importance_df.sort_values(
    "importance_mean",
    ascending=True,
)

plt.figure(figsize=(10, 6))

plt.barh(
    plot_df["feature"],
    plot_df["importance_mean"],
    xerr=plot_df["importance_std"],
    capsize=3,
)

plt.axvline(0, linewidth=1)
plt.xlabel("Decrease in accuracy after shuffling")
plt.ylabel("Passenger feature")
plt.title("Titanic Survival Model - Feature Importance")
plt.tight_layout()

chart_file = OUTPUT_DIR / "feature_importance.png"
plt.savefig(chart_file, dpi=300, bbox_inches="tight")
plt.close()

# Display results
print("\n===== DAY 36: FEATURE IMPORTANCE =====")
print(importance_df.round(4).to_string(index=False))

print("\nFiles saved:")
print(csv_file)
print(chart_file)
