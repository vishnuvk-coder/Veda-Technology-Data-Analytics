# Veda Technology - Data Analytics Internship

## Task 1: Data Cleaning and Preprocessing

This project is part of my **45-Day Data Analytics Internship at Veda Technology**.

The objective of this task is to clean, validate, explore, and prepare the Titanic dataset for further data analysis.

---

## 📌 Project Overview

Data cleaning is an important step in the data analytics process. Raw datasets may contain:

* Missing values
* Duplicate records
* Inconsistent values
* Incorrect data types
* Invalid values
* Unnecessary columns

In this project, Python and Pandas were used to inspect, clean, validate, and analyze the Titanic dataset.

---

## 🛠️ Tools and Technologies

* Python
* Pandas
* Matplotlib
* Jupyter Notebook / Python
* Microsoft Excel
* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
Veda-Technology-Data-Analytics/

│
├── data/
│   └── titanic_raw.csv
│
├── notebook/
│   ├── data_cleaning.py
│   └── eda_analysis.py
│
├── output/
│   ├── titanic_missing_values_handled.csv
│   ├── titanic_cleaned.csv
│   ├── change_log.csv
│   ├── outlier_summary.csv
│   ├── survival_rate_by_gender.png
│   ├── survival_rate_by_class.png
│   ├── survival_rate_by_age_group.png
│   ├── survival_rate_by_embarkation.png
│   ├── survival_rate_by_fare_group.png
│   ├── survival_rate_by_gender_and_class.png
│   ├── survival_rate_by_family_size.png
│   ├── survival_rate_by_travel_group.png
│   ├── survival_rate_by_passenger_status.png
│   ├── survival_rate_by_alone_status.png
│   ├── passenger_distribution_by_age_group.png
│   ├── passenger_distribution_by_gender.png
│   ├── passenger_distribution_by_class.png
│   ├── passenger_distribution_by_family_size.png
│   ├── passenger_distribution_by_travel_status.png
│   ├── correlation_heatmap.png
│   ├── age_vs_survival.png
│   ├── fare_vs_survival.png
│   ├── class_vs_fare.png
│   ├── family_size_vs_survival.png
│   ├── survival_rate_by_age_group_and_gender.png
│   ├── survival_rate_by_class_and_gender.png
│   ├── survival_rate_by_class_and_age_group.png
│   ├── age_outlier_boxplot.png
│   ├── fare_outlier_boxplot.png
│   ├── family_size_outlier_boxplot.png
│   ├── survival_rate_by_fare_group_and_class.csv
│   └── survival_rate_by_fare_group_and_class.png
│
└── README.md
```

> **Note:** The raw Titanic dataset is kept locally for reference and is not pushed to GitHub.

---

## 🧹 Data Cleaning and Preprocessing

The following data cleaning steps were performed:

### Missing Values

* **Age:** 177 missing values were filled using the median age of **28.0**.
* **Embarked:** 2 missing values were filled using the mode **S**.
* **Embark Town:** 2 missing values were filled using the corresponding embarkation code mapping.
* **Deck:** Removed because approximately **77.22%** of its values were missing.

### Duplicate Records

* Initially identified **107 exact duplicate row occurrences**.
* Duplicate rows were removed while keeping the first occurrence.
* After further cleaning, 4 additional duplicate rows were identified and removed.
* Final dataset contains **0 duplicate rows**.

### Data Validation

The cleaned dataset was checked for:

* Missing values
* Duplicate rows
* Incorrect data types
* Invalid ranges
* Inconsistent categorical values
* Column structure
* Column order
* Logical relationships between related columns

All final integrity checks passed successfully.

---

## 📊 Final Dataset

After cleaning:

* **Original rows:** 891
* **Final rows:** 780
* **Original columns:** 15
* **Final columns:** 14
* **Missing values:** 0
* **Duplicate rows:** 0

---

# 📈 Exploratory Data Analysis

After completing the data cleaning process, exploratory data analysis was performed using Pandas and Matplotlib.

## Day 14 – Basic Exploratory Data Analysis

The dataset was explored to understand:

* Number of rows and columns
* Column names
* Data types
* Statistical summary
* Unique values
* Missing values
* Duplicate records
* Passenger distribution
* Survival distribution
* Gender distribution
* Passenger class distribution
* Embarkation distribution

---

## Day 15 – Survival Analysis by Gender and Class

Survival rates were analyzed based on passenger gender and passenger class.

### Overall Survival Rate

The overall survival rate in the cleaned dataset was:

**41.28%**

### Survival Rate by Gender

| Gender | Survival Rate |
| ------ | ------------: |
| Female |        73.97% |
| Male   |        21.72% |

### Survival Rate by Passenger Class

| Class        | Survival Rate |
| ------------ | ------------: |
| First Class  |        63.68% |
| Second Class |        50.61% |
| Third Class  |        25.74% |

Visualization files were created and saved in the `output` folder.

---

## Day 16 – Survival Analysis by Age Group

Passenger ages were divided into five groups:

* Child
* Teenager
* Young Adult
* Adult
* Senior

### Results

| Age Group   | Passenger Count | Survival Rate |
| ----------- | --------------: | ------------: |
| Child       |              68 |        57.35% |
| Teenager    |              67 |        44.78% |
| Young Adult |             433 |        39.72% |
| Adult       |             191 |        39.79% |
| Senior      |              21 |        23.81% |

### Visualization

`output/survival_rate_by_age_group.png`

---

## Day 17 – Survival Analysis by Embarkation Port

Survival rates were analyzed based on the passenger's embarkation port.

### Embarkation Ports

* **C** – Cherbourg
* **Q** – Queenstown
* **S** – Southampton

### Results

| Embarkation Port | Passenger Count | Survived | Survival Rate |
| ---------------- | --------------: | -------: | ------------: |
| Cherbourg (C)    |             155 |       90 |        58.06% |
| Queenstown (Q)   |              58 |       20 |        34.48% |
| Southampton (S)  |             567 |      212 |        37.39% |

### Day 17 Work Completed

* Calculated passenger count by embarkation port
* Calculated survival count by embarkation port
* Calculated survival rate by embarkation port
* Created a bar chart using Matplotlib
* Saved the visualization in the `output` folder

### Visualization

`output/survival_rate_by_embarkation.png`

---

## Day 18 – Survival Analysis by Fare Group

Survival rates were analyzed based on passenger fare groups.

### Fare Groups

Fare values were divided into five groups:

* **Low** – Fare up to 10
* **Medium** – Fare from 10 to 25
* **Moderate** – Fare from 25 to 50
* **High** – Fare from 50 to 100
* **Very High** – Fare above 100

### Analysis Performed

* Calculated passenger count by fare group
* Calculated survival count by fare group
* Calculated survival rate by fare group
* Created a bar chart using Matplotlib
* Saved the visualization in the `output` folder

### Visualization

`output/survival_rate_by_fare_group.png`

---

## Day 19 – Survival Analysis by Gender and Passenger Class

On Day 19, survival rates were analyzed by combining passenger **gender** and **passenger class**.

### Analysis Performed

* Calculated passenger count by gender and passenger class
* Calculated survival count by gender and passenger class
* Calculated survival rate by gender and passenger class
* Created a grouped bar chart using Matplotlib

### Results

| Gender | Passenger Class | Survival Rate |
| ------ | --------------: | ------------: |
| Female |       1st Class |        96.77% |
| Female |       2nd Class |        91.67% |
| Female |       3rd Class |        47.24% |
| Male   |       1st Class |        37.82% |
| Male   |       2nd Class |        18.48% |
| Male   |       3rd Class |        15.88% |

### Visualization

`output/survival_rate_by_gender_and_class.png`

---

## Day 20 – Survival Analysis by Family Size

On Day 20, survival rates were analyzed based on **family size**.

Family size was calculated using siblings/spouses (`sibsp`) and parents/children (`parch`):

```text
Family Size = sibsp + parch + 1
```

The passenger's own record is included as `+1`.

### Family Size Groups

Passengers were classified into four groups:

* **Alone** – Family size = 1
* **Small** – Family size = 2–4
* **Medium** – Family size = 5–7
* **Large** – Family size greater than 7

### Analysis Performed

* Calculated family size for each passenger
* Created family size groups
* Calculated passenger count by family size group
* Calculated survival count by family size group
* Calculated survival rate by family size group
* Calculated survival rate by exact family size
* Created a bar chart using Matplotlib
* Saved the visualization in the `output` folder

### Visualization

`output/survival_rate_by_family_size.png`

---

## Day 21 – Survival Analysis by Travel Group Size

On Day 21, survival rates were analyzed based on the size of the passenger's travel group.

Travel group size was calculated using siblings/spouses and parents/children:

```text
Travel Group Size = sibsp + parch + 1
```

The passenger's own record is included as `+1`.

### Travel Group Categories

Passengers were classified into four groups:

* **Alone** – Travel group size = 1
* **Small Group** – Travel group size = 2–4
* **Medium Group** – Travel group size = 5–7
* **Large Group** – Travel group size greater than 7

### Analysis Performed

* Calculated travel group size for each passenger
* Created travel group categories
* Calculated passenger count by travel group
* Calculated survival count by travel group
* Calculated survival rate by travel group
* Calculated survival rate by exact travel group size
* Compared passengers traveling alone with passengers traveling with others
* Created a bar chart using Matplotlib
* Saved the visualization in the `output` folder

### Visualization

`output/survival_rate_by_travel_group.png`

---

## Day 22 – Survival Analysis by Passenger Status

On Day 22, survival rates were analyzed based on **passenger status** using the existing passenger classification information in the cleaned dataset.

The Titanic dataset contains the `who` column, which categorizes passengers into groups such as:

* Man
* Woman
* Child

### Analysis Performed

* Calculated passenger count by passenger status
* Calculated survival count by passenger status
* Calculated survival rate by passenger status
* Compared survival patterns across passenger status categories
* Created a bar chart using Matplotlib
* Saved the visualization in the `output` folder

### Visualization

`output/survival_rate_by_passenger_status.png`

> **Note:** A cabin-group analysis was not performed because the final cleaned dataset does not contain a `cabin` column.

---

## Day 23 – Survival Analysis by Alone Status

On Day 23, survival rates were analyzed based on whether passengers were traveling **alone or with others**.

The existing `alone` column in the cleaned Titanic dataset was used for this analysis.

### Analysis Performed

* Calculated passenger count by alone status
* Calculated survival count by alone status
* Calculated survival rate by alone status
* Compared passengers traveling alone with passengers traveling with others
* Created a travel status classification:

  * **Alone**
  * **With Others**
* Created a bar chart using Matplotlib
* Saved the visualization in the `output` folder

### Visualization

`output/survival_rate_by_alone_status.png`

---

## Day 24 – Passenger Demographic Distribution Analysis

On Day 24, the analysis was expanded from survival rates to **passenger demographic distribution**.

The objective was to understand how the 780 cleaned Titanic passengers were distributed across different demographic and travel-related categories.

### 1. Passenger Distribution by Age Group

Passengers were categorized into:

* Child
* Teenager
* Young Adult
* Adult
* Senior

Passenger counts were calculated for each age group and visualized using a bar chart.

### 2. Passenger Distribution by Gender

Passenger counts were analyzed using the `sex` column.

The analysis compared:

* Female passengers
* Male passengers

### 3. Passenger Distribution by Passenger Class

Passenger counts were analyzed across:

* First Class
* Second Class
* Third Class

### 4. Passenger Distribution by Family Size

Passengers were grouped into:

* Alone
* Small
* Medium
* Large

The distribution was calculated using the previously created `family_size_group` column.

### 5. Passenger Distribution by Travel Status

Passengers were classified as:

* Alone
* With Others

The distribution was calculated using the previously created `travel_status` column.

### Analysis Performed

* Calculated passenger distribution by age group
* Calculated passenger distribution by gender
* Calculated passenger distribution by passenger class
* Calculated passenger distribution by family size
* Calculated passenger distribution by travel status
* Created five bar-chart visualizations using Matplotlib
* Saved all visualizations in the `output` folder

### Visualizations

```text
output/passenger_distribution_by_age_group.png
output/passenger_distribution_by_gender.png
output/passenger_distribution_by_class.png
output/passenger_distribution_by_family_size.png
output/passenger_distribution_by_travel_status.png
```

### Day 24 Summary

The demographic analysis provides a descriptive overview of the cleaned Titanic dataset and complements the previous survival-rate analyses.

---

## Day 25 – Correlation and Relationship Analysis

On Day 25, correlation and relationship analysis was performed to understand relationships between numerical variables in the cleaned Titanic dataset.

### 1. Correlation Matrix

A correlation matrix was calculated for:

* Survived
* Passenger Class
* Age
* SibSp
* Parch
* Fare
* Alone

### Key Correlation Values

| Variables                   | Correlation |
| --------------------------- | ----------: |
| Survived vs Passenger Class |       -0.34 |
| Survived vs Fare            |        0.25 |
| Survived vs Alone Status    |       -0.18 |
| Survived vs Age             |       -0.08 |
| SibSp vs Alone Status       |       -0.61 |
| Parch vs Alone Status       |       -0.57 |
| Passenger Class vs Fare     |       -0.55 |

A correlation heatmap was created to visually represent these relationships.

### Visualization

`output/correlation_heatmap.png`

### 2. Age vs Survival

Average age was compared between passengers who survived and those who did not.

| Survival Status | Average Age |
| --------------- | ----------: |
| Did Not Survive |       30.50 |
| Survived        |       28.33 |

### Visualization

`output/age_vs_survival.png`

### 3. Fare vs Survival

Average fare was compared between passengers who survived and those who did not.

| Survival Status | Average Fare |
| --------------- | -----------: |
| Did Not Survive |        24.03 |
| Survived        |        50.19 |

### Visualization

`output/fare_vs_survival.png`

### 4. Passenger Class vs Fare

Average fare was analyzed by passenger class.

| Passenger Class | Average Fare |
| --------------- | -----------: |
| First Class     |        85.16 |
| Second Class    |        21.89 |
| Third Class     |        13.67 |

### Visualization

`output/class_vs_fare.png`

### 5. Family Size vs Survival

Survival rates were analyzed by exact family size.

| Family Size | Survival Rate |
| ----------: | ------------: |
|           1 |        33.71% |
|           2 |        55.19% |
|           3 |        57.43% |
|           4 |        71.43% |
|           5 |        23.08% |
|           6 |        13.64% |
|           7 |        33.33% |
|           8 |         0.00% |
|          11 |         0.00% |

### Visualization

`output/family_size_vs_survival.png`

### Day 25 Work Completed

* Calculated the correlation matrix
* Created a correlation heatmap
* Compared age with survival status
* Compared fare with survival status
* Analyzed passenger class and fare relationship
* Analyzed family size and survival rate
* Created five visualizations using Matplotlib
* Saved all visualizations in the `output` folder

---

## Day 26 – Multi-Variable Survival Analysis

On Day 26, the analysis was expanded to examine survival patterns using multiple passenger characteristics together.

The analysis combined **age group, gender, and passenger class** to understand survival rates across different combinations of passenger characteristics.

### 1. Survival Rate by Age Group and Gender

| Age Group   | Gender | Passenger Count | Survived | Survival Rate |
| ----------- | ------ | --------------: | -------: | ------------: |
| Child       | Female |              31 |       18 |        58.06% |
| Child       | Male   |              37 |       21 |        56.76% |
| Teenager    | Female |              36 |       27 |        75.00% |
| Teenager    | Male   |              31 |        3 |         9.68% |
| Young Adult | Female |             154 |      116 |        75.32% |
| Young Adult | Male   |             279 |       56 |        20.07% |
| Adult       | Female |              68 |       52 |        76.47% |
| Adult       | Male   |             123 |       24 |        19.51% |
| Senior      | Female |               3 |        3 |       100.00% |
| Senior      | Male   |              18 |        2 |        11.11% |

### Visualization

`output/survival_rate_by_age_group_and_gender.png`

### 2. Survival Rate by Passenger Class and Gender

| Passenger Class | Gender | Passenger Count | Survived | Survival Rate |
| --------------- | ------ | --------------: | -------: | ------------: |
| 1st Class       | Female |              93 |       90 |        96.77% |
| 1st Class       | Male   |             119 |       45 |        37.82% |
| 2nd Class       | Female |              72 |       66 |        91.67% |
| 2nd Class       | Male   |              92 |       17 |        18.48% |
| 3rd Class       | Female |             127 |       60 |        47.24% |
| 3rd Class       | Male   |             277 |       44 |        15.88% |

### Visualization

`output/survival_rate_by_class_and_gender.png`

### 3. Survival Rate by Passenger Class and Age Group

| Passenger Class | Age Group   | Passenger Count | Survived | Survival Rate |
| --------------- | ----------- | --------------: | -------: | ------------: |
| 1st Class       | Child       |               4 |        3 |        75.00% |
| 1st Class       | Teenager    |              12 |       11 |        91.67% |
| 1st Class       | Young Adult |              93 |       63 |        67.74% |
| 1st Class       | Adult       |              90 |       55 |        61.11% |
| 1st Class       | Senior      |              13 |        3 |        23.08% |
| 2nd Class       | Child       |              17 |       17 |       100.00% |
| 2nd Class       | Teenager    |              11 |        6 |        54.55% |
| 2nd Class       | Young Adult |              89 |       43 |        48.31% |
| 2nd Class       | Adult       |              44 |       16 |        36.36% |
| 2nd Class       | Senior      |               3 |        1 |        33.33% |
| 3rd Class       | Child       |              47 |       19 |        40.43% |
| 3rd Class       | Teenager    |              44 |       13 |        29.55% |
| 3rd Class       | Young Adult |             251 |       66 |        26.29% |
| 3rd Class       | Adult       |              57 |        5 |         8.77% |
| 3rd Class       | Senior      |               5 |        1 |        20.00% |

### Visualization

`output/survival_rate_by_class_and_age_group.png`

### 4. Three-Variable Survival Analysis

A detailed three-variable analysis was performed using:

* Age Group
* Gender
* Passenger Class

This analysis examined survival rates across combinations of all three passenger characteristics.

### Analysis Performed

* Calculated survival rate by age group and gender
* Calculated survival rate by passenger class and gender
* Calculated survival rate by passenger class and age group
* Performed three-variable analysis using age group, gender, and passenger class
* Created three visualizations using Matplotlib
* Saved the visualizations in the `output` folder

### Visualizations

```text
output/survival_rate_by_age_group_and_gender.png
output/survival_rate_by_class_and_gender.png
output/survival_rate_by_class_and_age_group.png
```

### Day 26 Summary

Multi-variable analysis provided a deeper descriptive view of survival patterns by examining age group, gender, and passenger class together rather than analyzing each variable independently.

---

## Day 27 – Outlier Detection and Analysis

On Day 27, outlier detection was performed on important numerical variables using the **Interquartile Range (IQR) method**.

The objective was to identify unusual observations and determine whether they should be removed or retained.

### Outlier Detection Method

The IQR method was used:

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Values below the lower bound or above the upper bound were identified as potential outliers.

### Variables Analyzed

* Age
* Fare
* SibSp
* Parch
* Family Size

### Outlier Results

| Column      |    Q1 |    Q3 |   IQR | Lower Bound | Upper Bound | Outlier Count |
| ----------- | ----: | ----: | ----: | ----------: | ----------: | ------------: |
| Age         | 21.75 | 36.00 | 14.25 |        0.38 |       57.38 |            32 |
| Fare        |  8.05 | 34.38 | 26.32 |      -31.44 |       73.86 |            97 |
| SibSp       |  0.00 |  1.00 |  1.00 |       -1.50 |        2.50 |            39 |
| Parch       |  0.00 |  1.00 |  1.00 |       -1.50 |        2.50 |            15 |
| Family Size |  1.00 |  2.00 |  1.00 |       -0.50 |        3.50 |            83 |

### Outlier Handling

The identified outliers were **retained** rather than removed.

These values may represent genuine passenger observations, such as:

* Older passengers
* Higher passenger fares
* Passengers traveling with larger families or groups
* Passengers with higher numbers of siblings, spouses, parents, or children

Removing these observations without additional evidence could result in loss of meaningful information.

### Analysis Performed

* Selected numerical variables for outlier analysis
* Calculated Q1 and Q3
* Calculated IQR
* Calculated lower and upper bounds
* Identified potential outliers
* Created an outlier summary table
* Saved the outlier summary as a CSV file
* Created box plots for age, fare, and family size
* Reviewed the identified outliers and retained them

### Output Files

```text
output/outlier_summary.csv
output/age_outlier_boxplot.png
output/fare_outlier_boxplot.png
output/family_size_outlier_boxplot.png
```

### Day 27 Summary

Outlier detection was successfully completed using the IQR method. Potential outliers were identified across age, fare, SibSp, Parch, and family size. The observations were retained because they may represent genuine passenger characteristics rather than data errors.

---

## Day 28 – Fare Group and Passenger Class Survival Analysis

On Day 28, survival patterns were analyzed by combining **fare groups** and **passenger class**.

The objective was to understand how fare level and passenger class together relate to passenger survival.

### Fare Groups

The fare values were divided into five groups:

* **Low** – Fare up to 10
* **Medium** – Fare from 10 to 25
* **Moderate** – Fare from 25 to 50
* **High** – Fare from 50 to 100
* **Very High** – Fare above 100

### Analysis Performed

* Created fare groups using passenger fare values
* Combined fare groups with passenger class
* Calculated passenger count for each fare group and passenger class combination
* Calculated survival count for each combination
* Calculated survival rate for each fare group and passenger class
* Calculated overall survival rate by fare group
* Created a grouped bar chart using Matplotlib
* Saved the detailed analysis as a CSV file
* Saved the visualization in the `output` folder

### Output Files

```text
output/survival_rate_by_fare_group_and_class.csv

output/survival_rate_by_fare_group_and_class.png
```

### Day 28 Summary

The analysis provided a deeper comparison of survival patterns by examining **fare level and passenger class together** rather than analyzing these variables independently. This helped create a more detailed view of survival patterns across different passenger groups.

---

## 📝 Change Log

The following changes were made during data cleaning:

| Issue                            | Column      | Action Taken                      |
| -------------------------------- | ----------- | --------------------------------- |
| Missing values                   | Age         | Filled using median               |
| Missing values                   | Embarked    | Filled using mode                 |
| Missing values                   | Embark Town | Filled using embarkation mapping  |
| High missing values              | Deck        | Removed column                    |
| Duplicate records                | All columns | Removed exact duplicates          |
| Duplicate records after cleaning | All columns | Removed additional duplicate rows |

A detailed change log is available in:

`output/change_log.csv`

---

## 📊 Current Internship Progress

**Day 28 / 45 completed**

**Progress: 62.2%**

### Completed Work

* Day 1: Internship setup and understanding Task 1
* Day 2: GitHub repository and project structure
* Day 3: Titanic dataset and column understanding
* Day 4: Raw dataset inspection
* Day 5: Missing value handling
* Day 6: Data cleaning change log
* Day 7: Duplicate record handling
* Day 8: Final duplicate verification
* Day 9: Data type and text consistency checks
* Day 10: Range and validity checks
* Day 11: Data consistency checks
* Day 12: Final dataset integrity validation
* Day 13: Final cleaning documentation
* Day 14: Exploratory data analysis
* Day 15: Survival analysis by gender and class
* Day 16: Survival analysis by age group
* Day 17: Survival analysis by embarkation port
* Day 18: Survival analysis by fare group
* Day 19: Survival analysis by gender and passenger class
* Day 20: Survival analysis by family size
* Day 21: Survival analysis by travel group size
* Day 22: Survival analysis by passenger status
* Day 23: Survival analysis by alone status
* Day 24: Passenger demographic distribution analysis
* Day 25: Correlation and relationship analysis
* Day 26: Multi-variable survival analysis
* Day 27: Outlier detection and analysis
* Day 28: Fare group and passenger class survival analysis

---

## ✅ Final Outcome

The Titanic dataset was successfully cleaned, validated, and analyzed.

The final dataset contains:

* No missing values
* No duplicate rows
* Valid data ranges
* Consistent categorical values
* Correct data types
* Valid column structure

Exploratory analysis was performed to understand survival patterns based on:

* Gender
* Passenger class
* Age group
* Embarkation port
* Fare group
* Gender and passenger class together
* Family size
* Travel group size
* Passenger status
* Alone status
* Fare group and passenger class

Passenger demographic distribution was also analyzed across:

* Age groups
* Gender
* Passenger class
* Family size
* Travel status

Correlation and relationship analysis was performed across:

* Survival and passenger class
* Survival and fare
* Survival and age
* Survival and alone status
* SibSp and alone status
* Parch and alone status
* Passenger class and fare
* Family size and survival

Multi-variable survival analysis was performed using:

* Age group and gender
* Passenger class and gender
* Passenger class and age group
* Age group, gender, and passenger class

Outlier analysis was performed using the IQR method across:

* Age
* Fare
* SibSp
* Parch
* Family size

The identified outliers were reviewed and retained because they may represent genuine passenger observations.

Fare group and passenger class analysis was also performed to examine survival patterns across combined fare and class categories.

The project demonstrates practical use of **Python, Pandas, Matplotlib, data cleaning, data validation, exploratory data analysis, correlation analysis, relationship analysis, multi-variable analysis, outlier detection, grouped analysis, and Git/GitHub**.

---

## 👨‍💻 Author

**Vishnu Kumar**

Data Analytics Intern

Veda Technology

GitHub:

https://github.com/vishnuvk-coder/Veda-Technology-Data-Analytics
