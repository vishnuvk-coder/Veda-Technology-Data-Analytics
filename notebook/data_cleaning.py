import pandas as pd

# Load the original dataset
df = pd.read_csv("data/titanic_raw.csv")

print("Original dataset shape:", df.shape)

# Check duplicate rows in the raw dataset
raw_duplicates = df.duplicated().sum()
print("Duplicate rows in raw dataset:", raw_duplicates)

# Remove exact duplicate rows
df = df.drop_duplicates(keep="first").copy()

print("Shape after duplicate removal:", df.shape)
print("Duplicates after removal:", df.duplicated().sum())

# Handle missing values in age
age_median = df["age"].median()
df["age"] = df["age"].fillna(age_median)

# Handle missing values in embarked
embarked_mode = df["embarked"].mode()[0]
df["embarked"] = df["embarked"].fillna(embarked_mode)

# Fill missing embark_town values
embark_mapping = {
    "S": "Southampton",
    "C": "Cherbourg",
    "Q": "Queenstown"
}

df["embark_town"] = df["embark_town"].fillna(
    df["embarked"].map(embark_mapping)
)

# Remove the deck column because it has many missing values
df = df.drop(columns=["deck"])

# Remove any duplicates created after cleaning
final_duplicates_before = df.duplicated().sum()

print("\nDuplicates before final verification:", final_duplicates_before)

df = df.drop_duplicates(keep="first").copy()

final_duplicates_after = df.duplicated().sum()

print("Duplicates after final verification:", final_duplicates_after)

# Check missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Display final dataset information
print("\nFinal dataset information:")
df.info()

print("\nFinal dataset shape:", df.shape)

# Save the final cleaned dataset
df.to_csv("output/titanic_cleaned.csv", index=False)

print("\nFinal cleaned dataset saved successfully.")