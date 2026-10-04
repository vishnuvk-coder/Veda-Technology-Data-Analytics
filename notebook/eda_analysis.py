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

# ============================================================
# DAY 25 - CORRELATION AND RELATIONSHIP ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("DAY 25 - CORRELATION AND RELATIONSHIP ANALYSIS")
print("=" * 60)

# ------------------------------------------------------------
# 1. Correlation Matrix
# ------------------------------------------------------------

print("\n1. Correlation Matrix")

correlation_columns = [
    "survived",
    "pclass",
    "age",
    "sibsp",
    "parch",
    "fare",
    "alone"
]

correlation_matrix = df[correlation_columns].corr()

print(correlation_matrix.round(2))


# ------------------------------------------------------------
# 2. Correlation Heatmap
# ------------------------------------------------------------

plt.figure(figsize=(10, 7))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    interpolation="nearest"
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap - Titanic Dataset")
plt.tight_layout()

plt.savefig(
    "output/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Visualization saved:")
print("output/correlation_heatmap.png")


# ------------------------------------------------------------
# 3. Age vs Survival
# ------------------------------------------------------------

print("\n2. Age vs Survival")

age_survival = df.groupby("survived")["age"].mean()

print("Average Age by Survival Status:")
print(age_survival.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    ["Did Not Survive", "Survived"],
    age_survival.values
)

plt.title("Average Age by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Average Age")

plt.tight_layout()

plt.savefig(
    "output/age_vs_survival.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Visualization saved:")
print("output/age_vs_survival.png")


# ------------------------------------------------------------
# 4. Fare vs Survival
# ------------------------------------------------------------

print("\n3. Fare vs Survival")

fare_survival = df.groupby("survived")["fare"].mean()

print("Average Fare by Survival Status:")
print(fare_survival.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    ["Did Not Survive", "Survived"],
    fare_survival.values
)

plt.title("Average Fare by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Average Fare")

plt.tight_layout()

plt.savefig(
    "output/fare_vs_survival.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Visualization saved:")
print("output/fare_vs_survival.png")


# ------------------------------------------------------------
# 5. Passenger Class vs Fare
# ------------------------------------------------------------

print("\n4. Passenger Class vs Fare")

class_fare = df.groupby("pclass")["fare"].mean()

print("Average Fare by Passenger Class:")
print(class_fare.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    class_fare.index.astype(str),
    class_fare.values
)

plt.title("Average Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")

plt.tight_layout()

plt.savefig(
    "output/class_vs_fare.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Visualization saved:")
print("output/class_vs_fare.png")


# ------------------------------------------------------------
# 6. Family Size vs Survival
# ------------------------------------------------------------

print("\n5. Family Size vs Survival")

family_survival = df.groupby("family_size")["survived"].mean() * 100

print("Survival Rate by Family Size:")
print(family_survival.round(2))

plt.figure(figsize=(9, 5))

plt.bar(
    family_survival.index.astype(str),
    family_survival.values
)

plt.title("Survival Rate by Family Size")
plt.xlabel("Family Size")
plt.ylabel("Survival Rate (%)")

plt.tight_layout()

plt.savefig(
    "output/family_size_vs_survival.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Visualization saved:")
print("output/family_size_vs_survival.png")


# ------------------------------------------------------------
# DAY 25 SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DAY 25 CORRELATION AND RELATIONSHIP ANALYSIS COMPLETED")
print("=" * 60)

# ============================================================
# DAY 26 - MULTI-VARIABLE SURVIVAL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("DAY 26 - MULTI-VARIABLE SURVIVAL ANALYSIS")
print("=" * 60)

# ------------------------------------------------------------
# 1. Survival Rate by Age Group and Gender
# ------------------------------------------------------------

age_gender_analysis = (
    df.groupby(["age_group", "sex"])["survived"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

age_gender_analysis["survival_rate"] = age_gender_analysis["mean"] * 100

print("\n1. Survival Rate by Age Group and Gender")
print(age_gender_analysis[
    ["age_group", "sex", "count", "sum", "survival_rate"]
].round(2))

plt.figure(figsize=(10, 6))

age_gender_pivot = age_gender_analysis.pivot(
    index="age_group",
    columns="sex",
    values="survival_rate"
)

age_gender_pivot.plot(kind="bar", ax=plt.gca())

plt.title("Survival Rate by Age Group and Gender")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.tight_layout()

plt.savefig("output/survival_rate_by_age_group_and_gender.png")
plt.close()

print(
    "Visualization saved: "
    "output/survival_rate_by_age_group_and_gender.png"
)


# ------------------------------------------------------------
# 2. Survival Rate by Passenger Class and Gender
# ------------------------------------------------------------

class_gender_analysis = (
    df.groupby(["pclass", "sex"])["survived"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

class_gender_analysis["survival_rate"] = (
    class_gender_analysis["mean"] * 100
)

print("\n2. Survival Rate by Passenger Class and Gender")
print(class_gender_analysis[
    ["pclass", "sex", "count", "sum", "survival_rate"]
].round(2))

plt.figure(figsize=(10, 6))

class_gender_pivot = class_gender_analysis.pivot(
    index="pclass",
    columns="sex",
    values="survival_rate"
)

class_gender_pivot.plot(kind="bar", ax=plt.gca())

plt.title("Survival Rate by Passenger Class and Gender")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.legend(title="Gender")
plt.tight_layout()

plt.savefig("output/survival_rate_by_class_and_gender.png")
plt.close()

print(
    "Visualization saved: "
    "output/survival_rate_by_class_and_gender.png"
)


# ------------------------------------------------------------
# 3. Survival Rate by Passenger Class and Age Group
# ------------------------------------------------------------

class_age_analysis = (
    df.groupby(["pclass", "age_group"])["survived"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

class_age_analysis["survival_rate"] = (
    class_age_analysis["mean"] * 100
)

print("\n3. Survival Rate by Passenger Class and Age Group")
print(class_age_analysis[
    ["pclass", "age_group", "count", "sum", "survival_rate"]
].round(2))

plt.figure(figsize=(12, 6))

class_age_pivot = class_age_analysis.pivot(
    index="age_group",
    columns="pclass",
    values="survival_rate"
)

class_age_pivot.plot(kind="bar", ax=plt.gca())

plt.title("Survival Rate by Passenger Class and Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=45)
plt.legend(title="Passenger Class")
plt.tight_layout()

plt.savefig("output/survival_rate_by_class_and_age_group.png")
plt.close()

print(
    "Visualization saved: "
    "output/survival_rate_by_class_and_age_group.png"
)


# ------------------------------------------------------------
# 4. Three-Variable Survival Analysis
#    Age Group + Gender + Passenger Class
# ------------------------------------------------------------

three_variable_analysis = (
    df.groupby(["age_group", "sex", "pclass"])["survived"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

three_variable_analysis["survival_rate"] = (
    three_variable_analysis["mean"] * 100
)

print("\n4. Survival Rate by Age Group, Gender and Passenger Class")
print(three_variable_analysis[
    [
        "age_group",
        "sex",
        "pclass",
        "count",
        "sum",
        "survival_rate"
    ]
].round(2))

print("\n" + "=" * 60)
print("DAY 26 MULTI-VARIABLE SURVIVAL ANALYSIS COMPLETED")
print("=" * 60)

# ============================================================
# DAY 27 - OUTLIER DETECTION AND ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("DAY 27 - OUTLIER DETECTION AND ANALYSIS")
print("=" * 60)

# 1. Numerical columns for outlier analysis
print("\n1. Numerical Columns for Outlier Analysis")

outlier_columns = [
    "age",
    "fare",
    "sibsp",
    "parch",
    "family_size"
]

print(outlier_columns)


# 2. Detect outliers using the IQR method
print("\n2. Outlier Detection Using IQR Method")

outlier_summary = []

for column in outlier_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    outlier_count = len(outliers)

    outlier_summary.append({
        "column": column,
        "Q1": round(Q1, 2),
        "Q3": round(Q3, 2),
        "IQR": round(IQR, 2),
        "lower_bound": round(lower_bound, 2),
        "upper_bound": round(upper_bound, 2),
        "outlier_count": outlier_count
    })

    print(f"\n{column}:")
    print(f"Q1: {Q1:.2f}")
    print(f"Q3: {Q3:.2f}")
    print(f"IQR: {IQR:.2f}")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")
    print(f"Outlier Count: {outlier_count}")


# 3. Create outlier summary DataFrame
outlier_summary_df = pd.DataFrame(outlier_summary)

print("\n3. Outlier Summary")
print(outlier_summary_df)


# 4. Save outlier summary
outlier_summary_df.to_csv(
    "output/outlier_summary.csv",
    index=False
)

print("\nOutlier summary saved:")
print("output/outlier_summary.csv")


# 5. Box plot for Age
print("\n4. Creating Age Box Plot")

df["age"].plot(
    kind="box",
    title="Age Distribution and Outliers",
    ylabel="Age"
)

plt.tight_layout()
plt.savefig("output/age_outlier_boxplot.png")
plt.close()

print("Visualization saved:")
print("output/age_outlier_boxplot.png")


# 6. Box plot for Fare
print("\n5. Creating Fare Box Plot")

df["fare"].plot(
    kind="box",
    title="Fare Distribution and Outliers",
    ylabel="Fare"
)

plt.tight_layout()
plt.savefig("output/fare_outlier_boxplot.png")
plt.close()

print("Visualization saved:")
print("output/fare_outlier_boxplot.png")


# 7. Box plot for Family Size
print("\n6. Creating Family Size Box Plot")

df["family_size"].plot(
    kind="box",
    title="Family Size Distribution and Outliers",
    ylabel="Family Size"
)

plt.tight_layout()
plt.savefig("output/family_size_outlier_boxplot.png")
plt.close()

print("Visualization saved:")
print("output/family_size_outlier_boxplot.png")


# 8. Outlier analysis conclusion
print("\n7. Outlier Analysis Conclusion")

print(
    "Outliers were identified using the IQR method. "
    "The identified values were retained because they may represent "
    "genuine passenger observations."
)

print("\n" + "=" * 60)
print("DAY 27 OUTLIER DETECTION AND ANALYSIS COMPLETED")
print("=" * 60)