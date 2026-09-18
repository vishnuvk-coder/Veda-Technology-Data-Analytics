import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("output/titanic_cleaned.csv")

print("Dataset shape:", df.shape)

# ---------------------------------------------------
# Day 11: Final Data Consistency Checks
# ---------------------------------------------------

print("\nFinal data consistency checks:")

# 1. Check embarked and embark_town consistency
embark_mapping = {
    "S": "Southampton",
    "C": "Cherbourg",
    "Q": "Queenstown"
}

expected_town = df["embarked"].map(embark_mapping)
invalid_embark_mapping = df["embark_town"] != expected_town

print(
    "Inconsistent embarked and embark_town values:",
    invalid_embark_mapping.sum()
)


# 2. Check pclass and class consistency
class_mapping = {
    1: "First",
    2: "Second",
    3: "Third"
}

expected_class = df["pclass"].map(class_mapping)
invalid_class_mapping = df["class"] != expected_class

print(
    "Inconsistent pclass and class values:",
    invalid_class_mapping.sum()
)


# 3. Check survived and alive consistency
alive_mapping = {
    0: "no",
    1: "yes"
}

expected_alive = df["survived"].map(alive_mapping)
invalid_alive_mapping = df["alive"] != expected_alive

print(
    "Inconsistent survived and alive values:",
    invalid_alive_mapping.sum()
)


# 4. Check alone consistency
expected_alone = (df["sibsp"] == 0) & (df["parch"] == 0)

invalid_alone = df["alone"] != expected_alone

print(
    "Inconsistent alone values:",
    invalid_alone.sum()
)


# 5. Review adult_male consistency
adult_male_review = df[
    (df["adult_male"] == True) &
    (df["sex"] != "male")
]

print(
    "adult_male=True but sex is not male:",
    len(adult_male_review)
)


# ---------------------------------------------------
# Final result
# ---------------------------------------------------

total_inconsistencies = (
    invalid_embark_mapping.sum()
    + invalid_class_mapping.sum()
    + invalid_alive_mapping.sum()
    + invalid_alone.sum()
    + len(adult_male_review)
)

print("\nTotal inconsistencies found:", total_inconsistencies)

if total_inconsistencies == 0:
    print("All consistency checks passed.")
else:
    print("Inconsistencies were found and need further review.")


# ---------------------------------------------------
# Review of adult_male records
# ---------------------------------------------------

print("\nReviewing adult_male values:")

if len(adult_male_review) == 0:
    print("All adult_male=True records have sex='male'.")
else:
    print(adult_male_review[["age", "sex", "who", "adult_male"]])


print("\nDay 11 final consistency checks completed.")