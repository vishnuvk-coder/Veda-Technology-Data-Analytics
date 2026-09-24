import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("output/titanic_cleaned.csv")

print("=" * 60)
print("DAY 15 - SURVIVAL RATE ANALYSIS")
print("=" * 60)

# ---------------------------------------------------------
# 1. Overall Survival Rate
# ---------------------------------------------------------

print("\n1. Overall Survival Analysis")

survival_count = df["survived"].value_counts()
survival_rate = df["survived"].mean() * 100

print("\nSurvival Count:")
print(survival_count)

print(f"\nOverall Survival Rate: {survival_rate:.2f}%")

# ---------------------------------------------------------
# 2. Survival by Gender
# ---------------------------------------------------------

print("\n2. Survival Analysis by Gender")

gender_survival_count = pd.crosstab(
    df["sex"],
    df["survived"]
)

print("\nSurvival Count by Gender:")
print(gender_survival_count)

gender_survival_rate = (
    df.groupby("sex")["survived"]
    .mean()
    .mul(100)
)

print("\nSurvival Rate by Gender:")
print(gender_survival_rate.round(2))

# ---------------------------------------------------------
# 3. Survival by Passenger Class
# ---------------------------------------------------------

print("\n3. Survival Analysis by Passenger Class")

class_survival_count = pd.crosstab(
    df["pclass"],
    df["survived"]
)

print("\nSurvival Count by Passenger Class:")
print(class_survival_count)

class_survival_rate = (
    df.groupby("pclass")["survived"]
    .mean()
    .mul(100)
)

print("\nSurvival Rate by Passenger Class:")
print(class_survival_rate.round(2))

# ---------------------------------------------------------
# 4. Survival by Gender and Passenger Class
# ---------------------------------------------------------

print("\n4. Survival Rate by Gender and Passenger Class")

gender_class_survival = (
    df.groupby(["sex", "pclass"])["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(gender_class_survival)

# ---------------------------------------------------------
# 5. Visualization - Survival Rate by Gender
# ---------------------------------------------------------

gender_survival_rate.plot(
    kind="bar",
    title="Titanic Survival Rate by Gender",
    xlabel="Gender",
    ylabel="Survival Rate (%)"
)

plt.tight_layout()
plt.savefig("output/survival_rate_by_gender.png")
plt.close()

# ---------------------------------------------------------
# 6. Visualization - Survival Rate by Passenger Class
# ---------------------------------------------------------

class_survival_rate.plot(
    kind="bar",
    title="Titanic Survival Rate by Passenger Class",
    xlabel="Passenger Class",
    ylabel="Survival Rate (%)"
)

plt.tight_layout()
plt.savefig("output/survival_rate_by_class.png")
plt.close()

# ---------------------------------------------------------
# Final Message
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("DAY 15 SURVIVAL ANALYSIS COMPLETED")
print("=" * 60)

# 7. Survival Analysis by Age Group
print("\n7. Survival Analysis by Age Group")

# Create age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"]
)

# Passenger count by age group
age_group_count = df["age_group"].value_counts().sort_index()

print("\nPassenger Count by Age Group:")
print(age_group_count)

# Survival rate by age group
age_group_survival_rate = (
    df.groupby("age_group", observed=True)["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print("\nSurvival Rate by Age Group:")
print(age_group_survival_rate)

# Visualization
age_group_survival_rate.plot(
    kind="bar",
    title="Titanic Survival Rate by Age Group",
    xlabel="Age Group",
    ylabel="Survival Rate (%)"
)

plt.tight_layout()
plt.savefig("output/survival_rate_by_age_group.png")
plt.close()

print("\nAge group survival analysis completed.")

# 8. Survival Analysis by Embarkation Port
print("\n8. Survival Analysis by Embarkation Port")

# Passenger count by embarkation port
embarkation_count = df["embarked"].value_counts().sort_index()

print("\nPassenger Count by Embarkation Port:")
print(embarkation_count)

# Survival count by embarkation port
embarkation_survival_count = pd.crosstab(
    df["embarked"],
    df["survived"]
)

print("\nSurvival Count by Embarkation Port:")
print(embarkation_survival_count)

# Survival rate by embarkation port
embarkation_survival_rate = (
    df.groupby("embarked")["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print("\nSurvival Rate by Embarkation Port:")
print(embarkation_survival_rate)

# Visualization
embarkation_survival_rate.plot(
    kind="bar",
    title="Titanic Survival Rate by Embarkation Port",
    xlabel="Embarkation Port",
    ylabel="Survival Rate (%)"
)

plt.tight_layout()
plt.savefig("output/survival_rate_by_embarkation.png")
plt.close()

print("\nEmbarkation survival analysis completed.")

# 9. Survival Analysis by Fare Group
print("\n9. Survival Analysis by Fare Group")

# Create fare groups
df["fare_group"] = pd.cut(
    df["fare"],
    bins=[-1, 10, 25, 50, 100, float("inf")],
    labels=["Low", "Medium", "Moderate", "High", "Very High"]
)

# Passenger count by fare group
fare_group_count = df["fare_group"].value_counts().sort_index()

print("\nPassenger Count by Fare Group:")
print(fare_group_count)

# Survival count by fare group
fare_survival_count = pd.crosstab(
    df["fare_group"],
    df["survived"]
)

print("\nSurvival Count by Fare Group:")
print(fare_survival_count)

# Survival rate by fare group
fare_survival_rate = (
    df.groupby("fare_group", observed=True)["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print("\nSurvival Rate by Fare Group:")
print(fare_survival_rate)

# Visualization
fare_survival_rate.plot(
    kind="bar",
    title="Titanic Survival Rate by Fare Group",
    xlabel="Fare Group",
    ylabel="Survival Rate (%)"
)

plt.tight_layout()
plt.savefig("output/survival_rate_by_fare_group.png")
plt.close()

print("\nFare group survival analysis completed.")