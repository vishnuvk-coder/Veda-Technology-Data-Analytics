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
│   ├── survival_rate_by_gender.png
│   ├── survival_rate_by_class.png
│   ├── survival_rate_by_age_group.png
│   ├── survival_rate_by_embarkation.png
│   ├── survival_rate_by_fare_group.png
│   └── survival_rate_by_gender_and_class.png
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

Visualizations were created and saved in the `output` folder.

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

Visualization:

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

Visualization:

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

Visualization:

`output/survival_rate_by_fare_group.png`

---

## Day 19 – Survival Analysis by Gender and Passenger Class

On Day 19, survival rates were analyzed by combining passenger **gender** and **passenger class**.

This analysis was performed to understand how survival rates varied when both factors were considered together.

### Analysis Performed

* Calculated passenger count by gender and passenger class
* Calculated survival count by gender and passenger class
* Calculated survival rate by gender and passenger class
* Created a grouped bar chart using Matplotlib
* Saved the visualization in the `output` folder

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

**Day 19 / 45 completed**

**Progress: 42.2%**

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

The project demonstrates practical use of **Python, Pandas, Matplotlib, data cleaning, data validation, exploratory data analysis, and Git/GitHub**.

---

## 👨‍💻 Author

**Vishnu Kumar**

Data Analytics Intern
Veda Technology

GitHub:

https://github.com/vishnuvk-coder/Veda-Technology-Data-Analytics
