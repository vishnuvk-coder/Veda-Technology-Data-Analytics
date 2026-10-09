
import pandas as pd
from sklearn.model_selection import train_test_split

# Day 32: Prepare training and testing datasets

input_path = "output/survival_model_ready.csv"
df = pd.read_csv(input_path)

print("Original dataset shape:", df.shape)

# Separate target from input features
X = df.drop(columns=["survived"])
y = df["survived"]

# Split: 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Keep features and target together in each output file
train_df = X_train.copy()
train_df["survived"] = y_train

test_df = X_test.copy()
test_df["survived"] = y_test

# Save the datasets
train_df.to_csv("output/survival_train.csv", index=False)
test_df.to_csv("output/survival_test.csv", index=False)

# Create a summary
summary = pd.DataFrame({
    "Metric": [
        "Original rows",
        "Training rows",
        "Testing rows",
        "Feature columns",
        "Target column",
        "Training missing values",
        "Testing missing values",
        "Training duplicate rows",
        "Testing duplicate rows",
        "Random state",
        "Test size"
    ],
    "Value": [
        len(df),
        len(train_df),
        len(test_df),
        len(X.columns),
        "survived",
        int(train_df.isnull().sum().sum()),
        int(test_df.isnull().sum().sum()),
        int(train_df.duplicated().sum()),
        int(test_df.duplicated().sum()),
        42,
        "20%"
    ]
})

summary.to_csv("output/train_test_split_summary.csv", index=False)

print("\nTraining dataset shape:", train_df.shape)
print("Testing dataset shape:", test_df.shape)
print("\nTraining survival distribution:")
print(train_df["survived"].value_counts(normalize=True).round(3))
print("\nTesting survival distribution:")
print(test_df["survived"].value_counts(normalize=True).round(3))

print("\nSummary:")
print(summary.to_string(index=False))

print("\nSaved files:")
print("output/survival_train.csv")
print("output/survival_test.csv")
print("output/train_test_split_summary.csv")

print("\nDay 32 completed successfully.")