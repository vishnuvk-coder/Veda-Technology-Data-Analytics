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

# 10. Survival Analysis by Gender and Passenger Class
print("\n10. Survival Analysis by Gender and Passenger Class")

# Passenger count by gender and class
gender_class_count = pd.crosstab(
    df["sex"],
    df["pclass"]
)

print("\nPassenger Count by Gender and Class:")
print(gender_class_count)

# Survival count by gender and class
gender_class_survival_count = pd.crosstab(
    [df["sex"], df["pclass"]],
    df["survived"]
)

print("\nSurvival Count by Gender and Class:")
print(gender_class_survival_count)

# Survival rate by gender and class
gender_class_survival_rate = (
    df.groupby(["sex", "pclass"], observed=True)["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print("\nSurvival Rate by Gender and Class:")
print(gender_class_survival_rate)

# Visualization
gender_class_survival_rate.unstack().plot(
    kind="bar",
    title="Titanic Survival Rate by Gender and Passenger Class",
    xlabel="Gender",
    ylabel="Survival Rate (%)"
)

plt.tight_layout()
plt.savefig("output/survival_rate_by_gender_and_class.png")
plt.close()

print("\nGender and class survival analysis completed.")

# ============================================================
# DAY 20 - SURVIVAL ANALYSIS BY FAMILY SIZE
# ============================================================

print("\n" + "=" * 60)
print("DAY 20 - SURVIVAL ANALYSIS BY FAMILY SIZE")
print("=" * 60)

# Create family size
df["family_size"] = df["sibsp"] + df["parch"] + 1

# Create family size groups
def classify_family_size(size):
    if size == 1:
        return "Alone"
    elif size <= 4:
        return "Small"
    elif size <= 7:
        return "Medium"
    else:
        return "Large"


df["family_size_group"] = df["family_size"].apply(classify_family_size)

# 1. Passenger count by family size group
print("\n1. Passenger Count by Family Size Group")

family_count = df["family_size_group"].value_counts()

print(family_count)

# 2. Survival count by family size group
print("\n2. Survival Count by Family Size Group")

survival_count = pd.crosstab(
    df["family_size_group"],
    df["survived"]
)

print(survival_count)

# 3. Survival rate by family size group
print("\n3. Survival Rate by Family Size Group")

survival_rate = (
    df.groupby("family_size_group")["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(survival_rate)

# 4. Survival rate by exact family size
print("\n4. Survival Rate by Exact Family Size")

exact_family_survival = (
    df.groupby("family_size")["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(exact_family_survival)

# 5. Create visualization
import matplotlib.pyplot as plt

group_order = ["Alone", "Small", "Medium", "Large"]

plot_data = survival_rate.reindex(group_order)

plt.figure(figsize=(8, 5))
plot_data.plot(kind="bar")

plt.title("Survival Rate by Family Size Group")
plt.xlabel("Family Size Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("output/survival_rate_by_family_size.png")
plt.close()

print("\nVisualization saved:")
print("output/survival_rate_by_family_size.png")

print("\n" + "=" * 60)
print("DAY 20 FAMILY SIZE ANALYSIS COMPLETED")
print("=" * 60)

# ============================================================
# DAY 21 - SURVIVAL ANALYSIS BY TRAVEL GROUP SIZE
# ============================================================

print("\n" + "=" * 60)
print("DAY 21 - SURVIVAL ANALYSIS BY TRAVEL GROUP SIZE")
print("=" * 60)

# Create travel group size
df["travel_group_size"] = df["sibsp"] + df["parch"] + 1

# Create travel group category
def classify_travel_group(size):
    if size == 1:
        return "Alone"
    elif size <= 4:
        return "Small Group"
    elif size <= 7:
        return "Medium Group"
    else:
        return "Large Group"


df["travel_group"] = df["travel_group_size"].apply(
    classify_travel_group
)

# ------------------------------------------------------------
# 1. Passenger Count by Travel Group
# ------------------------------------------------------------

print("\n1. Passenger Count by Travel Group")

travel_group_count = (
    df["travel_group"]
    .value_counts()
)

print(travel_group_count)

# ------------------------------------------------------------
# 2. Survival Count by Travel Group
# ------------------------------------------------------------

print("\n2. Survival Count by Travel Group")

travel_group_survival_count = pd.crosstab(
    df["travel_group"],
    df["survived"]
)

print(travel_group_survival_count)

# ------------------------------------------------------------
# 3. Survival Rate by Travel Group
# ------------------------------------------------------------

print("\n3. Survival Rate by Travel Group")

travel_group_survival_rate = (
    df.groupby("travel_group", observed=True)["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(travel_group_survival_rate)

# ------------------------------------------------------------
# 4. Survival Rate by Exact Travel Group Size
# ------------------------------------------------------------

print("\n4. Survival Rate by Exact Travel Group Size")

exact_travel_survival = (
    df.groupby("travel_group_size")["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(exact_travel_survival)

# ------------------------------------------------------------
# 5. Traveling Alone vs With Others
# ------------------------------------------------------------

print("\n5. Traveling Alone vs With Others")

df["travel_status"] = df["travel_group_size"].apply(
    lambda x: "Alone" if x == 1 else "With Others"
)

travel_status_survival = (
    df.groupby("travel_status")["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print("\nSurvival Rate:")
print(travel_status_survival)

# ------------------------------------------------------------
# 6. Visualization
# ------------------------------------------------------------

group_order = [
    "Alone",
    "Small Group",
    "Medium Group",
    "Large Group"
]

plot_data = travel_group_survival_rate.reindex(group_order)

plt.figure(figsize=(8, 5))

plot_data.plot(kind="bar")

plt.title("Titanic Survival Rate by Travel Group Size")
plt.xlabel("Travel Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "output/survival_rate_by_travel_group.png"
)

plt.close()

print("\nVisualization saved:")
print("output/survival_rate_by_travel_group.png")

print("\n" + "=" * 60)
print("DAY 21 TRAVEL GROUP ANALYSIS COMPLETED")
print("=" * 60)

# ============================================================
# DAY 22 - SURVIVAL ANALYSIS BY PASSENGER STATUS
# ============================================================

print("\n" + "=" * 60)
print("DAY 22 - SURVIVAL ANALYSIS BY PASSENGER STATUS")
print("=" * 60)

# Convert alone values into readable passenger status
df["passenger_status"] = df["alone"].map({
    True: "Traveling Alone",
    False: "Traveling With Others",
    1: "Traveling Alone",
    0: "Traveling With Others"
})

# ------------------------------------------------------------
# 1. Passenger Count by Passenger Status
# ------------------------------------------------------------

print("\n1. Passenger Count by Passenger Status")

passenger_status_count = (
    df["passenger_status"]
    .value_counts()
)

print(passenger_status_count)

# ------------------------------------------------------------
# 2. Survival Count by Passenger Status
# ------------------------------------------------------------

print("\n2. Survival Count by Passenger Status")

passenger_status_survival_count = pd.crosstab(
    df["passenger_status"],
    df["survived"]
)

print(passenger_status_survival_count)

# ------------------------------------------------------------
# 3. Survival Rate by Passenger Status
# ------------------------------------------------------------

print("\n3. Survival Rate by Passenger Status")

passenger_status_survival_rate = (
    df.groupby("passenger_status", observed=True)["survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(passenger_status_survival_rate)

# ------------------------------------------------------------
# 4. Visualization
# ------------------------------------------------------------

status_order = [
    "Traveling Alone",
    "Traveling With Others"
]

plot_data = passenger_status_survival_rate.reindex(status_order)

plt.figure(figsize=(8, 5))

plot_data.plot(kind="bar")

plt.title("Titanic Survival Rate by Passenger Status")
plt.xlabel("Passenger Status")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "output/survival_rate_by_passenger_status.png"
)

plt.close()

print("\nVisualization saved:")
print("output/survival_rate_by_passenger_status.png")

print("\n" + "=" * 60)
print("DAY 22 PASSENGER STATUS ANALYSIS COMPLETED")
print("=" * 60)

# ============================================================
# DAY 23 - SURVIVAL ANALYSIS BY ALONE STATUS
# ============================================================

print("\n" + "=" * 60)
print("DAY 23 - SURVIVAL ANALYSIS BY ALONE STATUS")
print("=" * 60)

# Check whether alone column exists
if "alone" in df.columns:

    # --------------------------------------------------------
    # 1. Passenger Count by Alone Status
    # --------------------------------------------------------

    print("\n1. Passenger Count by Alone Status")

    alone_count = df["alone"].value_counts().sort_index()

    print(alone_count)

    # --------------------------------------------------------
    # 2. Survival Count by Alone Status
    # --------------------------------------------------------

    print("\n2. Survival Count by Alone Status")

    alone_survival_count = pd.crosstab(
        df["alone"],
        df["survived"]
    )

    print(alone_survival_count)

    # --------------------------------------------------------
    # 3. Survival Rate by Alone Status
    # --------------------------------------------------------

    print("\n3. Survival Rate by Alone Status")

    alone_survival_rate = (
        df.groupby("alone", observed=True)["survived"]
        .mean()
        .mul(100)
        .round(2)
    )

    print(alone_survival_rate)

    # --------------------------------------------------------
    # 4. Compare Alone vs With Others
    # --------------------------------------------------------

    print("\n4. Alone vs With Others")

    df["travel_status"] = df["alone"].map({
        True: "Alone",
        False: "With Others",
        1: "Alone",
        0: "With Others"
    })

    travel_status_survival_rate = (
        df.groupby("travel_status", observed=True)["survived"]
        .mean()
        .mul(100)
        .round(2)
    )

    print("\nSurvival Rate:")
    print(travel_status_survival_rate)

    # --------------------------------------------------------
    # 5. Visualization
    # --------------------------------------------------------

    print("\n5. Creating Visualization")

    plot_order = ["Alone", "With Others"]

    plot_data = travel_status_survival_rate.reindex(
        plot_order
    )

    plt.figure(figsize=(8, 5))

    plot_data.plot(kind="bar")

    plt.title("Titanic Survival Rate: Alone vs With Others")
    plt.xlabel("Travel Status")
    plt.ylabel("Survival Rate (%)")
    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        "output/survival_rate_by_alone_status.png"
    )

    plt.close()

    print("\nVisualization saved:")
    print("output/survival_rate_by_alone_status.png")

else:

    print("\n'alone' column is not available in the cleaned dataset.")

print("\n" + "=" * 60)
print("DAY 23 ALONE STATUS ANALYSIS COMPLETED")
print("=" * 60)

# ============================================================
# DAY 24 - PASSENGER DEMOGRAPHIC DISTRIBUTION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("DAY 24 - PASSENGER DEMOGRAPHIC DISTRIBUTION ANALYSIS")
print("=" * 60)

# ============================================================
# 1. Passenger Distribution by Age Group
# ============================================================

print("\n1. Passenger Distribution by Age Group")

age_distribution = (
    df["age_group"]
    .value_counts()
    .sort_index()
)

print("\nPassenger Count by Age Group:")
print(age_distribution)

# Visualization
plt.figure(figsize=(8, 5))

age_distribution.plot(
    kind="bar",
    title="Titanic Passenger Distribution by Age Group",
    xlabel="Age Group",
    ylabel="Passenger Count"
)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "output/passenger_distribution_by_age_group.png"
)

plt.close()

print("\nVisualization saved:")
print("output/passenger_distribution_by_age_group.png")


# ============================================================
# 2. Passenger Distribution by Gender
# ============================================================

print("\n2. Passenger Distribution by Gender")

gender_distribution = df["sex"].value_counts()

print("\nPassenger Count by Gender:")
print(gender_distribution)

# Visualization
plt.figure(figsize=(8, 5))

gender_distribution.plot(
    kind="bar",
    title="Titanic Passenger Distribution by Gender",
    xlabel="Gender",
    ylabel="Passenger Count"
)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "output/passenger_distribution_by_gender.png"
)

plt.close()

print("\nVisualization saved:")
print("output/passenger_distribution_by_gender.png")


# ============================================================
# 3. Passenger Distribution by Passenger Class
# ============================================================

print("\n3. Passenger Distribution by Passenger Class")

class_distribution = (
    df["pclass"]
    .value_counts()
    .sort_index()
)

print("\nPassenger Count by Passenger Class:")
print(class_distribution)

# Visualization
plt.figure(figsize=(8, 5))

class_distribution.plot(
    kind="bar",
    title="Titanic Passenger Distribution by Passenger Class",
    xlabel="Passenger Class",
    ylabel="Passenger Count"
)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "output/passenger_distribution_by_class.png"
)

plt.close()

print("\nVisualization saved:")
print("output/passenger_distribution_by_class.png")


# ============================================================
# 4. Passenger Distribution by Family Size
# ============================================================

print("\n4. Passenger Distribution by Family Size")

family_distribution = (
    df["family_size_group"]
    .value_counts()
)

group_order = [
    "Alone",
    "Small",
    "Medium",
    "Large"
]

family_distribution = family_distribution.reindex(
    group_order
)

print("\nPassenger Count by Family Size Group:")
print(family_distribution)

# Visualization
plt.figure(figsize=(8, 5))

family_distribution.plot(
    kind="bar",
    title="Titanic Passenger Distribution by Family Size",
    xlabel="Family Size Group",
    ylabel="Passenger Count"
)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "output/passenger_distribution_by_family_size.png"
)

plt.close()

print("\nVisualization saved:")
print("output/passenger_distribution_by_family_size.png")


# ============================================================
# 5. Passenger Distribution by Travel Status
# ============================================================

print("\n5. Passenger Distribution by Travel Status")

travel_status_distribution = (
    df["travel_status"]
    .value_counts()
)

print("\nPassenger Count by Travel Status:")
print(travel_status_distribution)

# Visualization
plt.figure(figsize=(8, 5))

travel_status_distribution.plot(
    kind="bar",
    title="Titanic Passenger Distribution by Travel Status",
    xlabel="Travel Status",
    ylabel="Passenger Count"
)

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "output/passenger_distribution_by_travel_status.png"
)

plt.close()

print("\nVisualization saved:")
print("output/passenger_distribution_by_travel_status.png")


# ============================================================
# 6. Summary of Demographic Analysis
# ============================================================

print("\n" + "=" * 60)
print("DAY 24 DEMOGRAPHIC ANALYSIS SUMMARY")
print("=" * 60)

print("\nTotal Passengers:", len(df))

print("\nGender Distribution:")
print(gender_distribution)

print("\nPassenger Class Distribution:")
print(class_distribution)

print("\nAge Group Distribution:")
print(age_distribution)

print("\nFamily Size Distribution:")
print(family_distribution)

print("\nTravel Status Distribution:")
print(travel_status_distribution)

print("\n" + "=" * 60)
print("DAY 24 DEMOGRAPHIC ANALYSIS COMPLETED")
print("=" * 60)