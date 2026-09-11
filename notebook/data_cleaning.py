import pandas as pd

# ============================================================
# VEDA TECHNOLOGY - DATA ANALYTICS INTERNSHIP
# TASK 1: DATA CLEANING AND PREPROCESSING
# Dataset: Titanic
# ============================================================


# ------------------------------------------------------------
# 1. LOAD RAW DATASET
# ------------------------------------------------------------

df = pd.read_csv("data/titanic_raw.csv")


# ------------------------------------------------------------
# 2. FIRST 5 ROWS
# ------------------------------------------------------------

print("===== FIRST 5 ROWS =====")
print(df.head())


# ------------------------------------------------------------
# 3. DATASET INFORMATION
# ------------------------------------------------------------

print("\n===== DATASET INFORMATION =====")
df.info()


# ------------------------------------------------------------
# 4. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# ------------------------------------------------------------
# 5. CHECK DUPLICATE ROWS
# ------------------------------------------------------------

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 6. DISPLAY DUPLICATE RECORDS
# ------------------------------------------------------------

print("\n===== DUPLICATE RECORDS =====")

duplicates = df[df.duplicated(keep=False)]

print(duplicates.head(20))

print("\nTotal duplicate records:", len(duplicates))


# ------------------------------------------------------------
# 7. DUPLICATE FREQUENCY
# ------------------------------------------------------------

print("\n===== DUPLICATE FREQUENCY =====")

duplicate_counts = (
    df.value_counts()
    .reset_index(name="count")
)

print(duplicate_counts.head(20))


# ------------------------------------------------------------
# 8. MISSING VALUE PERCENTAGE
# ------------------------------------------------------------

print("\n===== MISSING VALUE PERCENTAGE =====")

missing_percentage = (
    df.isnull().sum() / len(df) * 100
).round(2)

print(
    missing_percentage[missing_percentage > 0]
)


# ------------------------------------------------------------
# 9. DATASET SHAPE
# ------------------------------------------------------------

print("\n===== DATASET SHAPE =====")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


# ------------------------------------------------------------
# 10. COLUMN NAMES
# ------------------------------------------------------------

print("\n===== COLUMN NAMES =====")

print(df.columns.tolist())