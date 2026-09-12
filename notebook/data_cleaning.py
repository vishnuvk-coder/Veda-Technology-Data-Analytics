import pandas as pd

# ============================================================
# VEDA TECHNOLOGY - DATA ANALYTICS INTERNSHIP
# DAY 5: HANDLING MISSING VALUES
# DATASET: TITANIC
# ============================================================

# ------------------------------------------------------------
# 1. LOAD RAW DATASET
# ------------------------------------------------------------
df = pd.read_csv("data/titanic_raw.csv")

print("===== ORIGINAL DATASET =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# ------------------------------------------------------------
# 2. CHECK MISSING VALUES BEFORE CLEANING
# ------------------------------------------------------------
print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())

# Save the original missing-value count
missing_before = df.isnull().sum()

# ------------------------------------------------------------
# 3. HANDLE MISSING VALUES IN AGE
# ------------------------------------------------------------
age_median = df["age"].median()

df["age"] = df["age"].fillna(age_median)

print("\n===== AGE COLUMN =====")
print("Missing age values filled with median:", age_median)

# ------------------------------------------------------------
# 4. HANDLE MISSING VALUES IN EMBARKED
# ------------------------------------------------------------
embarked_mode = df["embarked"].mode()[0]

df["embarked"] = df["embarked"].fillna(embarked_mode)

print("\n===== EMBARKED COLUMN =====")
print("Missing embarked values filled with mode:", embarked_mode)

# ------------------------------------------------------------
# 5. HANDLE MISSING VALUES IN EMBARK_TOWN
# ------------------------------------------------------------
embark_mapping = {
    "S": "Southampton",
    "C": "Cherbourg",
    "Q": "Queenstown"
}

df["embark_town"] = df["embark_town"].fillna(
    df["embarked"].map(embark_mapping)
)

print("\n===== EMBARK_TOWN COLUMN =====")
print("Missing embark_town values filled using embarked values.")

# ------------------------------------------------------------
# 6. REMOVE DECK COLUMN
# ------------------------------------------------------------
df = df.drop(columns=["deck"])

print("\n===== DECK COLUMN =====")
print("The deck column was removed because it contained many missing values.")

# ------------------------------------------------------------
# 7. CHECK MISSING VALUES AFTER CLEANING
# ------------------------------------------------------------
print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

# ------------------------------------------------------------
# 8. DISPLAY FINAL DATASET INFORMATION
# ------------------------------------------------------------
print("\n===== FINAL DATASET INFORMATION =====")
df.info()

print("\n===== FINAL DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# ------------------------------------------------------------
# 9. SAVE CLEANED DATASET
# ------------------------------------------------------------
output_path = "output/titanic_missing_values_handled.csv"

df.to_csv(output_path, index=False)

print("\n===== FILE SAVED =====")
print("Cleaned dataset saved to:", output_path)