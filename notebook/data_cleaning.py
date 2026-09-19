import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("output/titanic_cleaned.csv")

print("Dataset shape:", df.shape)

# ---------------------------------------------------
# Day 12: Final Dataset Integrity Checks
# ---------------------------------------------------

print("\nFinal dataset integrity checks:")

# 1. Check expected columns
expected_columns = [
    "survived",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
    "class",
    "who",
    "adult_male",
    "embark_town",
    "alive",
    "alone"
]

missing_columns = [
    column for column in expected_columns
    if column not in df.columns
]

unexpected_columns = [
    column for column in df.columns
    if column not in expected_columns
]

print("Missing expected columns:", len(missing_columns))
print("Unexpected columns:", len(unexpected_columns))


# 2. Check column names for extra spaces
columns_with_spaces = [
    column for column in df.columns
    if column != column.strip()
]

print("Column names with extra spaces:", len(columns_with_spaces))


# 3. Check duplicate column names
duplicate_column_names = df.columns.duplicated().sum()

print("Duplicate column names:", duplicate_column_names)


# 4. Check row count
expected_rows = 780

print("Expected rows:", expected_rows)
print("Actual rows:", len(df))

if len(df) == expected_rows:
    print("Row count check: PASSED")
else:
    print("Row count check: REVIEW REQUIRED")


# 5. Check missing values
total_missing = df.isnull().sum().sum()

print("Total missing values:", total_missing)


# 6. Check duplicate rows
total_duplicates = df.duplicated().sum()

print("Total duplicate rows:", total_duplicates)


# 7. Check final column order
columns_match = list(df.columns) == expected_columns

print("Column order check:", columns_match)


# ---------------------------------------------------
# Final result
# ---------------------------------------------------

total_issues = (
    len(missing_columns)
    + len(unexpected_columns)
    + len(columns_with_spaces)
    + duplicate_column_names
    + total_missing
    + total_duplicates
)

print("\nTotal integrity issues found:", total_issues)

if (
    total_issues == 0
    and len(df) == expected_rows
    and columns_match
):
    print("All final dataset integrity checks passed.")
else:
    print("Some integrity checks require further review.")

print("\nDay 12 dataset integrity checks completed.")