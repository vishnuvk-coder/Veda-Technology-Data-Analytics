import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/titanic_cleaned.csv")

print("=" * 60)
print("DAY 14 - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# 1. Dataset shape
print("\n1. Dataset Shape")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Column names
print("\n2. Column Names")
print(df.columns.tolist())

# 3. Data types
print("\n3. Data Types")
print(df.dtypes)

# 4. Basic statistical summary
print("\n4. Statistical Summary")
print(df.describe())

# 5. Unique values
print("\n5. Unique Values")
for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")

# 6. Missing values
print("\n6. Missing Values")
print(df.isnull().sum())

# 7. Duplicate rows
print("\n7. Duplicate Rows")
print(df.duplicated().sum())

# 8. Survival distribution
print("\n8. Survival Distribution")
print(df["survived"].value_counts())

# 9. Gender distribution
print("\n9. Gender Distribution")
print(df["sex"].value_counts())

# 10. Passenger class distribution
print("\n10. Passenger Class Distribution")
print(df["pclass"].value_counts().sort_index())

# 11. Embarkation distribution
print("\n11. Embarkation Distribution")
print(df["embarked"].value_counts())

print("\n" + "=" * 60)
print("EDA BASIC ANALYSIS COMPLETED")
print("=" * 60)