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