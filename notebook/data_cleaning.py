import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("output/titanic_cleaned.csv")

print("Dataset shape:", df.shape)

# ---------------------------------------------------
# Day 10: Range and Validity Checks
# ---------------------------------------------------

print("\nRange and validity checks:")

# 1. Check survived values
invalid_survived = ~df["survived"].isin([0, 1])
print("Invalid survived values:", invalid_survived.sum())

# 2. Check passenger class
invalid_pclass = ~df["pclass"].isin([1, 2, 3])
print("Invalid pclass values:", invalid_pclass.sum())

# 3. Check age
invalid_age = (df["age"] < 0) | (df["age"] > 100)
print("Invalid age values:", invalid_age.sum())

# 4. Check siblings/spouses
invalid_sibsp = df["sibsp"] < 0
print("Invalid sibsp values:", invalid_sibsp.sum())

# 5. Check parents/children
invalid_parch = df["parch"] < 0
print("Invalid parch values:", invalid_parch.sum())

# 6. Check fare
invalid_fare = df["fare"] < 0
print("Invalid fare values:", invalid_fare.sum())

# 7. Check sex
invalid_sex = ~df["sex"].isin(["male", "female"])
print("Invalid sex values:", invalid_sex.sum())

# 8. Check embarked
invalid_embarked = ~df["embarked"].isin(["S", "C", "Q"])
print("Invalid embarked values:", invalid_embarked.sum())

# 9. Check Boolean columns
invalid_adult_male = ~df["adult_male"].isin([True, False])
print("Invalid adult_male values:", invalid_adult_male.sum())

invalid_alone = ~df["alone"].isin([True, False])
print("Invalid alone values:", invalid_alone.sum())


# ---------------------------------------------------
# Final result
# ---------------------------------------------------

total_invalid = (
    invalid_survived.sum()
    + invalid_pclass.sum()
    + invalid_age.sum()
    + invalid_sibsp.sum()
    + invalid_parch.sum()
    + invalid_fare.sum()
    + invalid_sex.sum()
    + invalid_embarked.sum()
    + invalid_adult_male.sum()
    + invalid_alone.sum()
)

print("\nTotal invalid values found:", total_invalid)

if total_invalid == 0:
    print("All range and validity checks passed.")
else:
    print("Invalid values were found and need further review.")

print("\nDay 10 range and validity checks completed.")