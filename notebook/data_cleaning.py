import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("output/titanic_cleaned.csv")

print("Dataset shape:", df.shape)

# 1. Display data types
print("\nCurrent data types:")
print(df.dtypes)

# 2. Check unique values in text columns
text_columns = [
    "sex",
    "embarked",
    "class",
    "who",
    "embark_town",
    "alive"
]

print("\nUnique values in text columns:")

for column in text_columns:
    print(f"\n{column}:")
    print(df[column].unique())

# 3. Check unique values in Boolean columns
boolean_columns = [
    "adult_male",
    "alone"
]

print("\nUnique values in Boolean columns:")

for column in boolean_columns:
    print(f"\n{column}:")
    print(df[column].unique())

# 4. Check numeric columns
numeric_columns = [
    "survived",
    "pclass",
    "age",
    "sibsp",
    "parch",
    "fare"
]

print("\nNumeric column summary:")
print(df[numeric_columns].describe())

# 5. Check for unexpected values
print("\nValue checks:")

print("survived values:", df["survived"].unique())
print("pclass values:", df["pclass"].unique())
print("embarked values:", df["embarked"].unique())
print("sex values:", df["sex"].unique())
print("alive values:", df["alive"].unique())

print("\nDay 9 data type and consistency checks completed.")

# Check for leading or trailing spaces in text columns
print("\nChecking for extra spaces:")

for column in text_columns:
    values_with_spaces = df[column].astype(str).str.strip()

    if not (df[column].astype(str) == values_with_spaces).all():
        print(f"{column}: Extra spaces found")
    else:
        print(f"{column}: No extra spaces")

# Check text capitalization consistency
print("\nChecking text capitalization:")

for column in text_columns:
    print(f"{column}:")
    print(df[column].value_counts())

print("\nText consistency checks completed.")