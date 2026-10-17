Veda Technology - Data Analytics Internship
Task 1: Data Cleaning and Preprocessing
This project is part of my 45-Day Data Analytics Internship at Veda Technology.
The objective of this task is to clean, validate, explore, and prepare the Titanic dataset for further data analysis.
📌 Project Overview
Data cleaning is an important step in the data analytics process. Raw datasets may contain:
- Missing values
- Duplicate records
- Inconsistent values
- Incorrect data types
- Invalid values
- Unnecessary columns
In this project, Python and Pandas were used to inspect, clean, validate, and analyze the Titanic dataset.
🛠️ Tools and Technologies
- Python
- Pandas
- Matplotlib
- Jupyter Notebook / Python
- Microsoft Excel
- Git
- GitHub
- VS Code
📂 Project Structure
Veda-Technology-Data-Analytics/
├── data/
│   └── titanic_raw.csv                 # Local raw dataset; not pushed to GitHub
├── notebook/
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── model_train_test_split.py
│   ├── train_survival_model.py
│   ├── compare_models.py
│   ├── evaluate_survival_model.py
│   ├── feature_importance_analysis.py  # Feature importance analysis
│   ├── model_error_analysis.py         # Model prediction error analysis
│   ├── group_performance_analysis.py   # Performance comparison by passenger group
│   ├── threshold_analysis.py           # Prediction threshold analysis
│   └── threshold_selection_analysis.py # Threshold selection by metric
├── output/
│   ├── survival_train.csv
│   ├── survival_test.csv
│   ├── train_test_split_summary.csv
│   ├── confusion_matrix.csv
│   ├── logistic_regression_metrics.csv
│   ├── survival_test_predictions.csv
│   ├── model_comparison.csv
│   ├── model_comparison_predictions.csv
│   ├── threshold_comparison.csv
│   ├── classification_report.csv
│   ├── evaluation_confusion_matrix.csv
│   ├── survival_test_evaluation.csv
│   ├── feature_importance.csv              # Feature importance results table
│   ├── feature_importance.png              # Feature importance chart
│   ├── prediction_results.csv              # Actual and predicted outcomes for test rows
│   ├── misclassified_passengers.csv        # Incorrect predictions only
│   ├── error_analysis_summary.csv           # Overall error counts and accuracy
│   ├── error_rates_by_group.csv             # Error rates by available passenger groups
│   ├── error_analysis_confusion_matrix.png  # Confusion matrix chart
│   ├── group_performance_report.csv         # Performance metrics by passenger group
│   ├── group_error_summary.csv              # Group sizes and error rates
│   ├── group_performance_comparison.png     # Accuracy comparison chart
│   ├── threshold_analysis.csv               # Metrics across prediction thresholds
│   ├── threshold_analysis.png               # Threshold metrics comparison chart
│   ├── threshold_selection_summary.csv       # Best threshold for each metric
│   ├── threshold_selection_comparison.png    # Metric comparison with selected threshold
│   ├── titanic_missing_values_handled.csv
│   ├── titanic_cleaned.csv
│   ├── change_log.csv
│   ├── outlier_summary.csv
│   ├── feature_engineering_summary.csv
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
│   ├── survival_rate_by_fare_group_and_class.png
│   ├── feature_survival_by_age_group.png
│   ├── feature_survival_by_family_size_group.png
│   ├── feature_survival_by_fare_group.png
│   └── feature_survival_by_travel_status.png
└── README.md
Note: The raw Titanic dataset is kept locally for reference and is not pushed to GitHub.

🧹 Data Cleaning and Preprocessing
The following data cleaning steps were performed:
Missing Values
- Age: 177 missing values were filled using the median age of 28.0.
- Embarked: 2 missing values were filled using the mode S.
- Embark Town: 2 missing values were filled using the corresponding embarkation code mapping.
- Deck: Removed because approximately 77.22% of its values were missing.
Duplicate Records
- Initially identified 107 exact duplicate row occurrences.
- Duplicate rows were removed while keeping the first occurrence.
- After further cleaning, 4 additional duplicate rows were identified and removed.
- Final dataset contains 0 duplicate rows.
Data Validation
The cleaned dataset was checked for:
- Missing values
- Duplicate rows
- Incorrect data types
- Invalid ranges
- Inconsistent categorical values
- Column structure
- Column order
- Logical relationships between related columns
All final integrity checks passed successfully.
📊 Final Dataset
After cleaning:
- Original rows: 891
- Final rows: 780
- Original columns: 15
- Final columns: 14
- Missing values: 0
- Duplicate rows: 0
📈 Exploratory Data Analysis
After completing the data cleaning process, exploratory data analysis was performed using Pandas and Matplotlib.
Day 14 – Basic Exploratory Data Analysis
The dataset was explored to understand:
- Number of rows and columns
- Column names
- Data types
- Statistical summary
- Unique values
- Missing values
- Duplicate records
- Passenger distribution
- Survival distribution
- Gender distribution
- Passenger class distribution
- Embarkation distribution
Day 15 – Survival Analysis by Gender and Class
Survival rates were analyzed based on passenger gender and passenger class.
Overall Survival Rate
The overall survival rate in the cleaned dataset was:
41.28%
Survival Rate by Gender
| Gender | Survival Rate |
| ------ | ------------: |
| Female |        73.97% |
| Male   |        21.72% |
Survival Rate by Passenger Class
| Class        | Survival Rate |
| ------------ | ------------: |
| First Class  |        63.68% |
| Second Class |        50.61% |
| Third Class  |        25.74% |
Visualization files were created and saved in the output folder.
Day 16 – Survival Analysis by Age Group
Passenger ages were divided into five groups:
- Child
- Teenager
- Young Adult
- Adult
- Senior
Results
| Age Group   | Passenger Count | Survival Rate |
| ----------- | --------------: | ------------: |
| Child       |              68 |        57.35% |
| Teenager    |              67 |        44.78% |
| Young Adult |             433 |        39.72% |
| Adult       |             191 |        39.79% |
| Senior      |              21 |        23.81% |
Visualization
output/survival_rate_by_age_group.png
Day 17 – Survival Analysis by Embarkation Port
Survival rates were analyzed based on the passenger's embarkation port.
Embarkation Ports
- C – Cherbourg
- Q – Queenstown
- S – Southampton
Results
| Embarkation Port | Passenger Count | Survived | Survival Rate |
| ---------------- | --------------: | -------: | ------------: |
| Cherbourg (C)    |             155 |       90 |        58.06% |
| Queenstown (Q)   |              58 |       20 |        34.48% |
| Southampton (S)  |             567 |      212 |        37.39% |
Day 17 Work Completed
- Calculated passenger count by embarkation port
- Calculated survival count by embarkation port
- Calculated survival rate by embarkation port
- Created a bar chart using Matplotlib
- Saved the visualization in the output folder
Visualization
output/survival_rate_by_embarkation.png
Day 18 – Survival Analysis by Fare Group
Survival rates were analyzed based on passenger fare groups.
Fare Groups
Fare values were divided into five groups:
- Low – Fare up to 10
- Medium – Fare from 10 to 25
- Moderate – Fare from 25 to 50
- High – Fare from 50 to 100
- Very High – Fare above 100
Analysis Performed
- Calculated passenger count by fare group
- Calculated survival count by fare group
- Calculated survival rate by fare group
- Created a bar chart using Matplotlib
- Saved the visualization in the output folder
Visualization
output/survival_rate_by_fare_group.png
Day 19 – Survival Analysis by Gender and Passenger Class
On Day 19, survival rates were analyzed by combining gender and passenger class.
Analysis Performed
- Calculated passenger count by gender and passenger class
- Calculated survival count by gender and passenger class
- Calculated survival rate by gender and passenger class
- Created a grouped bar chart using Matplotlib
Results
| Gender | Passenger Class | Survival Rate |
| ------ | --------------: | ------------: |
| Female |       1st Class |        96.77% |
| Female |       2nd Class |        91.67% |
| Female |       3rd Class |        47.24% |
| Male   |       1st Class |        37.82% |
| Male   |       2nd Class |        18.48% |
| Male   |       3rd Class |        15.88% |
Visualization
output/survival_rate_by_gender_and_class.png
Day 20 – Survival Analysis by Family Size
On Day 20, survival rates were analyzed based on family size.
Family size was calculated using siblings/spouses (sibsp) and parents/children (parch):

Family Size = sibsp + parch + 1

The passenger's own record is included as +1.
Family Size Groups
Passengers were classified into four groups:
- Alone – Family size = 1
- Small – Family size = 2–4
- Medium – Family size = 5–7
- Large – Family size greater than 7
Analysis Performed
- Calculated family size for each passenger
- Created family size groups
- Calculated passenger count by family size group
- Calculated survival count by family size group
- Calculated survival rate by family size group
- Calculated survival rate by exact family size
- Created a bar chart using Matplotlib
- Saved the visualization in the output folder
Visualization
output/survival_rate_by_family_size.png
Day 21 – Survival Analysis by Travel Group Size
On Day 21, survival rates were analyzed based on the size of the passenger's travel group.
Travel group size was calculated using siblings/spouses and parents/children:

Travel Group Size = sibsp + parch + 1

The passenger's own record is included as +1.
Travel Group Categories
Passengers were classified into four groups:
- Alone – Travel group size = 1
- Small Group – Travel group size = 2–4
- Medium Group – Travel group size = 5–7
- Large Group – Travel group size greater than 7
Analysis Performed
- Calculated travel group size for each passenger
- Created travel group categories
- Calculated passenger count by travel group
- Calculated survival count by travel group
- Calculated survival rate by travel group
- Calculated survival rate by exact travel group size
- Compared passengers traveling alone with passengers traveling with others
- Created a bar chart using Matplotlib
- Saved the visualization in the output folder
Visualization
output/survival_rate_by_travel_group.png
Day 22 – Survival Analysis by Passenger Status
On Day 22, survival rates were analyzed based on passenger status using the existing passenger classification information in the cleaned dataset.
The Titanic dataset contains the who column, which categorizes passengers into groups such as:
- Man
- Woman
- Child
Analysis Performed
- Calculated passenger count by passenger status
- Calculated survival count by passenger status
- Calculated survival rate by passenger status
- Compared survival patterns across passenger status categories
- Created a bar chart using Matplotlib
- Saved the visualization in the output folder
Visualization
output/survival_rate_by_passenger_status.png
Note: A cabin-group analysis was not performed because the final cleaned dataset does not contain a cabin column.

Day 23 – Survival Analysis by Alone Status
On Day 23, survival rates were analyzed based on whether passengers were traveling alone or with others.
The existing alone column in the cleaned Titanic dataset was used for this analysis.
Analysis Performed
- Calculated passenger count by alone status
- Calculated survival count by alone status
- Calculated survival rate by alone status
- Compared passengers traveling alone with passengers traveling with others
- Created a travel status classification:
  * Alone
  * With Others
- Created a bar chart using Matplotlib
- Saved the visualization in the output folder
Visualization
output/survival_rate_by_alone_status.png
Day 24 – Passenger Demographic Distribution Analysis
On Day 24, the analysis was expanded from survival rates to passenger demographic distribution.
The objective was to understand how the 780 cleaned Titanic passengers were distributed across different demographic and travel-related categories.
1. Passenger Distribution by Age Group
Passengers were categorized into:
- Child
- Teenager
- Young Adult
- Adult
- Senior
Passenger counts were calculated for each age group and visualized using a bar chart.
2. Passenger Distribution by Gender
Passenger counts were analyzed using the sex column.
The analysis compared:
- Female passengers
- Male passengers
3. Passenger Distribution by Passenger Class
Passenger counts were analyzed across:
- First Class
- Second Class
- Third Class
4. Passenger Distribution by Family Size
Passengers were grouped into:
- Alone
- Small
- Medium
- Large
The distribution was calculated using the previously created family_size_group column.
5. Passenger Distribution by Travel Status
Passengers were classified as:
- Alone
- With Others
The distribution was calculated using the travel_status column.
Analysis Performed
- Calculated passenger distribution by age group
- Calculated passenger distribution by gender
- Calculated passenger distribution by passenger class
- Calculated passenger distribution by family size
- Calculated passenger distribution by travel status
- Created five bar-chart visualizations using Matplotlib
- Saved all visualizations in the output folder
Visualizations

output/passenger_distribution_by_age_group.png

output/passenger_distribution_by_gender.png

output/passenger_distribution_by_class.png

output/passenger_distribution_by_family_size.png

output/passenger_distribution_by_travel_status.png

Day 24 Summary
The demographic analysis provides a descriptive overview of the cleaned Titanic dataset and complements the previous survival-rate analyses.
Day 25 – Correlation and Relationship Analysis
On Day 25, correlation and relationship analysis was performed to understand relationships between numerical variables in the cleaned Titanic dataset.
1. Correlation Matrix
A correlation matrix was calculated for:
- Survived
- Passenger Class
- Age
- SibSp
- Parch
- Fare
- Alone
Key Correlation Values
| Variables                   | Correlation |
| --------------------------- | ----------: |
| Survived vs Passenger Class |       -0.34 |
| Survived vs Fare            |        0.25 |
| Survived vs Alone Status    |       -0.18 |
| Survived vs Age             |       -0.08 |
| SibSp vs Alone Status       |       -0.61 |
| Parch vs Alone Status       |       -0.57 |
| Passenger Class vs Fare     |       -0.55 |
A correlation heatmap was created to visually represent these relationships.
Visualization
output/correlation_heatmap.png
2. Age vs Survival
Average age was compared between passengers who survived and those who did not.
| Survival Status | Average Age |
| --------------- | ----------: |
| Did Not Survive |       30.50 |
| Survived        |       28.33 |
Visualization
output/age_vs_survival.png
3. Fare vs Survival
Average fare was compared between passengers who survived and those who did not.
| Survival Status | Average Fare |
| --------------- | -----------: |
| Did Not Survive |        24.03 |
| Survived        |        50.19 |
Visualization
output/fare_vs_survival.png
4. Passenger Class vs Fare
Average fare was analyzed by passenger class.
| Passenger Class | Average Fare |
| --------------- | -----------: |
| First Class     |        85.16 |
| Second Class    |        21.89 |
| Third Class     |        13.67 |
Visualization
output/class_vs_fare.png
5. Family Size vs Survival
Survival rates were analyzed by exact family size.
| Family Size | Survival Rate |
| ----------: | ------------: |
|           1 |        33.71% |
|           2 |        55.19% |
|           3 |        57.43% |
|           4 |        71.43% |
|           5 |        23.08% |
|           6 |        13.64% |
|           7 |        33.33% |
|           8 |         0.00% |
|          11 |         0.00% |
Visualization
output/family_size_vs_survival.png
Day 25 Work Completed
- Calculated the correlation matrix
- Created a correlation heatmap
- Compared age with survival status
- Compared fare with survival status
- Analyzed passenger class and fare relationship
- Analyzed family size and survival rate
- Created five visualizations using Matplotlib
- Saved all visualizations in the output folder
Day 26 – Multi-Variable Survival Analysis
On Day 26, the analysis was expanded to examine survival patterns using multiple passenger characteristics together.
The analysis combined age group, gender, and passenger class to understand survival rates across different combinations of passenger characteristics.
1. Survival Rate by Age Group and Gender
| Age Group   | Gender | Passenger Count | Survived | Survival Rate |
| ----------- | ------ | --------------: | -------: | ------------: |
| Child       | Female |              31 |       18 |        58.06% |
| Child       | Male   |              37 |       21 |        56.76% |
| Teenager    | Female |              36 |       27 |        75.00% |
| Teenager    | Male   |              31 |        3 |         9.68% |
| Young Adult | Female |             154 |      116 |        75.32% |
| Young Adult | Male   |             279 |       56 |        20.07% |
| Adult       | Female |              68 |       52 |        76.47% |
| Adult       | Male   |             123 |       24 |        19.51% |
| Senior      | Female |               3 |        3 |       100.00% |
| Senior      | Male   |              18 |        2 |        11.11% |
Visualization
output/survival_rate_by_age_group_and_gender.png
2. Survival Rate by Passenger Class and Gender
| Passenger Class | Gender | Passenger Count | Survived | Survival Rate |
| --------------- | ------ | --------------: | -------: | ------------: |
| 1st Class       | Female |              93 |       90 |        96.77% |
| 1st Class       | Male   |             119 |       45 |        37.82% |
| 2nd Class       | Female |              72 |       66 |        91.67% |
| 2nd Class       | Male   |              92 |       17 |        18.48% |
| 3rd Class       | Female |             127 |       60 |        47.24% |
| 3rd Class       | Male   |             277 |       44 |        15.88% |
Visualization
output/survival_rate_by_class_and_gender.png
3. Survival Rate by Passenger Class and Age Group
| Passenger Class | Age Group   | Passenger Count | Survived | Survival Rate |
| --------------- | ----------- | --------------: | -------: | ------------: |
| 1st Class       | Child       |               4 |        3 |        75.00% |
| 1st Class       | Teenager    |              12 |       11 |        91.67% |
| 1st Class       | Young Adult |              93 |       63 |        67.74% |
| 1st Class       | Adult       |              90 |       55 |        61.11% |
| 1st Class       | Senior      |              13 |        3 |        23.08% |
| 2nd Class       | Child       |              17 |       17 |       100.00% |
| 2nd Class       | Teenager    |              11 |        6 |        54.55% |
| 2nd Class       | Young Adult |              89 |       43 |        48.31% |
| 2nd Class       | Adult       |              44 |       16 |        36.36% |
| 2nd Class       | Senior      |               3 |        1 |        33.33% |
| 3rd Class       | Child       |              47 |       19 |        40.43% |
| 3rd Class       | Teenager    |              44 |       13 |        29.55% |
| 3rd Class       | Young Adult |             251 |       66 |        26.29% |
| 3rd Class       | Adult       |              57 |        5 |         8.77% |
| 3rd Class       | Senior      |               5 |        1 |        20.00% |
Visualization
output/survival_rate_by_class_and_age_group.png
4. Three-Variable Survival Analysis
A detailed three-variable analysis was performed using:
- Age Group
- Gender
- Passenger Class
This analysis examined survival rates across combinations of all three passenger characteristics.
Analysis Performed
- Calculated survival rate by age group and gender
- Calculated survival rate by passenger class and gender
- Calculated survival rate by passenger class and age group
- Performed three-variable analysis using age group, gender, and passenger class
- Created three visualizations using Matplotlib
- Saved the visualizations in the output folder
Visualizations

output/survival_rate_by_age_group_and_gender.png

output/survival_rate_by_class_and_gender.png

output/survival_rate_by_class_and_age_group.png

Day 26 Summary
Multi-variable analysis provided a deeper descriptive view of survival patterns by examining age group, gender, and passenger class together rather than analyzing each variable independently.
Day 27 – Outlier Detection and Analysis
On Day 27, outlier detection was performed on important numerical variables using the Interquartile Range (IQR) method.
The objective was to identify unusual observations and determine whether they should be removed or retained.
Outlier Detection Method
The IQR method was used:

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Values below the lower bound or above the upper bound were identified as potential outliers.
Variables Analyzed
- Age
- Fare
- SibSp
- Parch
- Family Size
Outlier Results
| Column      |    Q1 |    Q3 |   IQR | Lower Bound | Upper Bound | Outlier Count |
| ----------- | ----: | ----: | ----: | ----------: | ----------: | ------------: |
| Age         | 21.75 | 36.00 | 14.25 |        0.38 |       57.38 |            32 |
| Fare        |  8.05 | 34.38 | 26.32 |      -31.44 |       73.86 |            97 |
| SibSp       |  0.00 |  1.00 |  1.00 |       -1.50 |        2.50 |            39 |
| Parch       |  0.00 |  1.00 |  1.00 |       -1.50 |        2.50 |            15 |
| Family Size |  1.00 |  2.00 |  1.00 |       -0.50 |        3.50 |            83 |
Outlier Handling
The identified outliers were retained rather than removed.
These values may represent genuine passenger observations, such as:
- Older passengers
- Higher passenger fares
- Passengers traveling with larger families or groups
- Passengers with higher numbers of siblings, spouses, parents, or children
Removing these observations without additional evidence could result in loss of meaningful information.
Analysis Performed
- Selected numerical variables for outlier analysis
- Calculated Q1 and Q3
- Calculated IQR
- Calculated lower and upper bounds
- Identified potential outliers
- Created an outlier summary table
- Saved the outlier summary as a CSV file
- Created box plots for age, fare, and family size
- Reviewed the identified outliers and retained them
Output Files

output/outlier_summary.csv

output/age_outlier_boxplot.png

output/fare_outlier_boxplot.png

output/family_size_outlier_boxplot.png

Day 27 Summary
Outlier detection was successfully completed using the IQR method. Potential outliers were identified across age, fare, SibSp, Parch, and family size. The observations were retained because they may represent genuine passenger characteristics rather than data errors.
Day 28 – Fare Group and Passenger Class Survival Analysis
On Day 28, survival patterns were analyzed by combining fare groups and passenger class.
The objective was to understand how fare level and passenger class together relate to passenger survival.
Fare Groups
The fare values were divided into five groups:
- Low – Fare up to 10
- Medium – Fare from 10 to 25
- Moderate – Fare from 25 to 50
- High – Fare from 50 to 100
- Very High – Fare above 100
Analysis Performed
- Created fare groups using passenger fare values
- Combined fare groups with passenger class
- Calculated passenger count for each fare group and passenger class combination
- Calculated survival count for each combination
- Calculated survival rate for each fare group and passenger class
- Calculated overall survival rate by fare group
- Created a grouped bar chart using Matplotlib
- Saved the detailed analysis as a CSV file
- Saved the visualization in the output folder
Output Files

output/survival_rate_by_fare_group_and_class.csv

output/survival_rate_by_fare_group_and_class.png

Day 28 Summary
The analysis provided a deeper comparison of survival patterns by examining fare level and passenger class together rather than analyzing these variables independently. This helped create a more detailed view of survival patterns across different passenger groups.
Day 29 – Feature Engineering and Derived Variable Analysis
On Day 29, feature engineering was performed to create useful derived variables from the cleaned Titanic dataset.
The objective was to transform existing passenger information into analytical features that could be used to identify additional survival patterns.
Derived Features Created
The following features were created:
- Family Size
- Family Size Group
- Age Group
- Fare Group
- Travel Status
1. Family Size
Family size was calculated using:

Family Size = SibSp + Parch + 1

The passenger's own record is included as +1.
Family sizes were then grouped into:
- Alone – Family size = 1
- Small – Family size = 2–4
- Medium – Family size = 5–7
- Large – Family size greater than 7
2. Age Group
Passengers were categorized into:
- Child
- Teenager
- Young Adult
- Adult
- Senior
3. Fare Group
Fare values were categorized into:
- Low
- Medium
- Moderate
- High
- Very High
4. Travel Status
Passengers were classified as:
- Alone
- With Others
Feature Engineering Results
Family Size Group
| Family Size Group | Passenger Count | Survived | Survival Rate |
| ----------------- | --------------: | -------: | ------------: |
| Alone             |             442 |      149 |        33.71% |
| Small             |             283 |      163 |        57.60% |
| Medium            |              47 |       10 |        21.28% |
| Large             |               8 |        0 |         0.00% |
Age Group
| Age Group   | Passenger Count | Survived | Survival Rate |
| ----------- | --------------: | -------: | ------------: |
| Child       |              68 |       39 |        57.35% |
| Teenager    |              42 |       21 |        50.00% |
| Young Adult |             354 |      131 |        37.01% |
| Adult       |             291 |      124 |        42.61% |
| Senior      |              25 |        7 |        28.00% |
Fare Group
| Fare Group | Passenger Count | Survived | Survival Rate |
| ---------- | --------------: | -------: | ------------: |
| Low        |             260 |       59 |        22.69% |
| Medium     |             199 |       85 |        42.71% |
| Moderate   |             169 |       72 |        42.60% |
| High       |              99 |       67 |        67.68% |
| Very High  |              53 |       39 |        73.58% |
Travel Status
| Travel Status | Passenger Count | Survived | Survival Rate |
| ------------- | --------------: | -------: | ------------: |
| Alone         |             442 |      149 |        33.71% |
| With Others   |             338 |      173 |        51.18% |
Key Observations
- Passengers in the Small Family Size group had the highest survival rate among the family-size groups at 57.60%.
- The Large Family Size group had a survival rate of 0.00%, but this group contained only 8 passengers, so the result should be interpreted cautiously.
- Children had a survival rate of 57.35%, the highest among the age groups.
- Passengers in the Very High Fare group had the highest survival rate at 73.58%.
- Passengers in the Low Fare group had the lowest survival rate among fare groups at 22.69%.
- Passengers traveling With Others had a higher survival rate (51.18%) than passengers traveling Alone (33.71%).
Analysis Performed
- Created derived analytical features
- Created family size groups
- Created age groups
- Created fare groups
- Created travel status
- Calculated passenger counts
- Calculated survival counts
- Calculated survival rates
- Created a feature engineering summary CSV
- Created four survival-rate visualizations using Matplotlib
Output Files

output/feature_engineering_summary.csv

output/feature_survival_by_age_group.png

output/feature_survival_by_family_size_group.png

output/feature_survival_by_fare_group.png

output/feature_survival_by_travel_status.png

Day 29 Summary
Feature engineering successfully transformed existing Titanic passenger information into useful derived variables. These features provided additional analytical perspectives on survival patterns related to family size, age, fare level, and travel status.
Day 30 – Key Insights and Findings
On Day 30, the key findings from the completed exploratory data analysis were summarized to identify major survival patterns across gender, passenger class, age, fare, family size, and travel status.
Key Findings
Overall Titanic survival rate was 41.28%.
Female passengers had a much higher survival rate than male passengers.
First-class passengers had a higher survival rate than third-class passengers.
Children showed a relatively high survival rate.
Very-high-fare passengers had a higher survival rate than low-fare passengers.
Passengers travelling with others had a higher survival rate than passengers travelling alone.
Small family groups showed a relatively high survival rate.
Analysis Performed
Summarized overall survival rate.
Compared survival rates by gender.
Compared survival rates by passenger class.
Compared survival rates by age group.
Compared survival rates by fare group.
Compared survival rates by family size group.
Compared survival rates by travel status.
Created a key insights summary CSV file.
Created a visualization of the key survival insights.
Day 30 Output Files
output/key_insights_summary.csv
output/key_survival_insights.png
Day 30 Summary
The key-insights analysis consolidated the major survival patterns identified during the exploratory data analysis and provided a concise summary of the most important findings.
Day 31 – Model Data Preparation
On Day 31, the cleaned Titanic dataset was prepared for future survival prediction by selecting useful features and converting categorical values into numerical form.
Model Preparation
The following columns were selected:
- survived – Target variable
- pclass – Passenger class
- sex – Passenger gender
- age – Passenger age
- sibsp – Number of siblings/spouses aboard
- parch – Number of parents/children aboard
- fare – Passenger fare
- embarked – Port of embarkation
- alone – Whether the passenger was traveling alone
Categorical Encoding
Categorical columns were converted into numerical values for future machine-learning use:
- sex: Female = 0, Male = 1
- embarked: C = 0, Q = 1, S = 2
- alone: False/True converted to 0/1
Columns Excluded
The following descriptive or redundant columns were not included in the model-ready dataset:
- alive – Directly represents the survival outcome and could cause target leakage
- class – Redundant with passenger class
- who – Descriptive passenger category not required for the selected feature set
- embark_town – Redundant with the encoded embarkation column
Validation Performed
- Checked the model-ready dataset shape
- Checked selected columns
- Checked for missing values
- Checked for duplicate rows
- Verified that the target column is survived
- Saved the prepared dataset for future survival prediction work
Output Files
output/survival_model_ready.csv
output/model_preparation_summary.csv
Day 31 Summary
The cleaned Titanic dataset was successfully transformed into a model-ready dataset by selecting relevant features and encoding categorical variables. This prepares the project for future survival prediction and machine-learning analysis.
Day 32 – Train-Test Split Preparation
On Day 32, the model-ready Titanic dataset was divided into training and testing datasets to prepare for future machine-learning experiments.
Split Configuration
- Training set: 80% of the data
- Testing set: 20% of the data
- Random state: 42, to make the split reproducible
- Stratification: Used the survived target column to preserve the target-class proportions in both sets
Process Performed
- Loaded output/survival_model_ready.csv
- Separated the features from the survived target variable
- Used train_test_split to create training and testing datasets
- Applied stratification using the target variable
- Saved the training and testing datasets as separate CSV files
- Created a summary CSV containing the split configuration and dataset sizes
Output Files
notebook/model_train_test_split.py
output/survival_train.csv
output/survival_test.csv
output/train_test_split_summary.csv
output/logistic_regression_metrics.csv
output/survival_test_predictions.csv
output/confusion_matrix.csv
Day 32 Summary
The model-ready dataset was split into training and testing sets using an 80/20 ratio, a fixed random state, and target stratification. This establishes a reproducible data-splitting step for future model training and evaluation. Model training and predictive performance evaluation have not been claimed as part of this step.
Day 33 – Logistic Regression Model Training and Evaluation
On Day 33, a Logistic Regression model was trained using the prepared Titanic training dataset and evaluated on the separate testing dataset. The model used a preprocessing pipeline to handle missing values, scale numeric features, and encode categorical features.
Model Configuration
- Model: Logistic Regression
- Training rows: 624
- Testing rows: 156
- Maximum iterations: 1000
- Evaluation: Predictions were compared with the actual survived values in the test dataset
Evaluation Results
- Accuracy: 80.13%
- Weighted precision: 80.49%
- Weighted recall: 80.13%
- Weighted F1-score: 80.22%
- Correct predictions: 125 out of 156
- Incorrect predictions: 31 out of 156
Confusion Matrix Results
- 74 passengers who did not survive were correctly predicted as not survived
- 51 passengers who survived were correctly predicted as survived
- 18 passengers who did not survive were incorrectly predicted as survived
- 13 passengers who survived were incorrectly predicted as not survived
Output Files
notebook/train_survival_model.py
output/logistic_regression_metrics.csv
output/survival_test_predictions.csv
output/confusion_matrix.csv
Day 33 Summary
The first Logistic Regression model was successfully trained and evaluated. It achieved 80.13% accuracy on the 156-row test dataset. These metrics provide a baseline for later model comparison and improvement; they do not guarantee the same performance on other data.
Day 34 – Machine Learning Model Comparison
On Day 34, Logistic Regression and Decision Tree classifiers were trained and evaluated using the same prepared training and testing datasets. Both models used preprocessing pipelines for missing-value handling, numeric scaling, and categorical encoding. The Decision Tree was configured with max_depth=5 and random_state=42. The goal was to compare model performance on the same held-out test set and identify which model performed better in this experiment.
Model Comparison Results
Metric	Logistic Regression	Decision Tree
Training accuracy	78.21%	83.81%
Test accuracy	80.13%	77.56%
Weighted precision	80.49%	78.71%
Weighted recall	80.13%	77.56%
Weighted F1-score	80.22%	76.51%


Findings
- Logistic Regression achieved the higher test accuracy at 80.13%.
- The Decision Tree achieved 83.81% training accuracy but 77.56% test accuracy, suggesting a possible generalization gap. This result alone does not prove overfitting, but it is worth investigating.
- Logistic Regression performed better across the reported test metrics for this particular split.
- The results are a baseline comparison on the current held-out test set; performance may differ on other data.
Files Created on Day 34
The following three files were created for the model-comparison task:
1. notebook/compare_models.py — Python script that trains Logistic Regression and Decision Tree models, evaluates both models, and compares their performance metrics.
2. output/model_comparison.csv — CSV report containing each model's training accuracy, test accuracy, weighted precision, weighted recall, and weighted F1-score. It records Logistic Regression at 80.13% test accuracy and Decision Tree at 77.56% test accuracy.
3. output/model_comparison_predictions.csv — CSV file containing the test-set predictions from the models, allowing their predictions to be reviewed side by side.
Expected project paths:
notebook/compare_models.py
output/model_comparison.csv
output/model_comparison_predictions.csv
Day 34 Summary
Two classification models were compared using the same train/test split. Logistic Regression was the best-performing model by test accuracy in this experiment, with 80.13% accuracy compared with 77.56% for the Decision Tree.
Day 35 – Logistic Regression Evaluation and Threshold Comparison
On Day 35, the Logistic Regression model was evaluated in more detail using its predicted survival probabilities. Five classification thresholds were compared to understand how the threshold changes accuracy, precision, recall, and F1-score for passengers who survived.
Evaluation Setup
- Training rows: 624
- Testing rows: 156
- Features before encoding: 8
- Model: Logistic Regression
- Thresholds compared: 0.30, 0.40, 0.50, 0.60, and 0.70
- The existing train/test split was reused, and preprocessing was fitted within a pipeline on the training data.
Threshold Comparison Results
Threshold	Accuracy	Survivor Precision	Survivor Recall	Survivor F1-score
0.30	73.72%	63.53%	84.38%	72.48%
0.40	78.85%	71.23%	81.25%	75.91%
0.50	80.13%	73.91%	79.69%	76.69%
0.60	80.13%	82.35%	65.62%	73.04%
0.70	79.49%	94.44%	53.12%	68.00%


Classification Report at Threshold 0.50
Class	Precision	Recall	F1-score	Support
Did not survive	0.85	0.80	0.83	92
Survived	0.74	0.80	0.77	64
Accuracy	—	—	0.80	156
Macro average	0.79	0.80	0.80	156
Weighted average	0.80	0.80	0.80	156


Confusion Matrix at Threshold 0.50
Actual outcome	Predicted not survived	Predicted survived
Did not survive	74	18
Survived	13	51


Interpretation:
- 74 passengers who did not survive were correctly predicted as not survived.
- 51 passengers who survived were correctly predicted as survived.
- 18 passengers who did not survive were incorrectly predicted as survived.
- 13 passengers who survived were incorrectly predicted as not survived.
Key Findings
- Threshold 0.50 achieved 80.13% accuracy and the highest survivor F1-score (76.69%) among the five tested thresholds.
- Threshold 0.30 had the highest survivor recall (84.38%) among the tested thresholds, but lower precision (63.53%).
- Threshold 0.70 had the highest survivor precision (94.44%), but survivor recall fell to 53.12%.
- Threshold 0.60 matched the 0.50 threshold's accuracy (80.13%) but traded recall for higher precision.
- These results show the trade-off between precision and recall: lowering the threshold predicts more survivors, while raising it makes the model more selective.
Threshold comparison on the test set is exploratory. The test results should not be used to choose a final production threshold; threshold selection should be performed with validation data to avoid tuning to the held-out test set.
Files Created on Day 35
1. notebook/evaluate_survival_model.py — trains the Logistic Regression pipeline, calculates survival probabilities, compares five thresholds, and generates evaluation outputs.
2. output/threshold_comparison.csv — stores accuracy, survivor precision, survivor recall, and survivor F1-score for each threshold.
3. output/classification_report.csv — stores class-level precision, recall, F1-score, and support at the standard 0.50 threshold.
4. output/evaluation_confusion_matrix.csv — stores the confusion matrix at threshold 0.50. This separate filename preserves the existing Day 33 confusion_matrix.csv.
5. output/survival_test_evaluation.csv — stores test features, actual survival outcomes, predicted survival probabilities, and predictions at threshold 0.50.
Day 35 Summary
The Logistic Regression model was evaluated at five classification thresholds. At the standard 0.50 threshold, it achieved 80.13% accuracy on the 156-row test set, with 73.91% precision, 79.69% recall, and a 76.69% F1-score for the survivor class. Evaluation reports, a separate confusion matrix, threshold metrics, and test predictions with probabilities were saved for further analysis.
Day 36 – Feature Importance Analysis
On Day 36, permutation importance was used to estimate how much each passenger feature contributed to the Logistic Regression model's predictive accuracy. The model was trained on the existing training dataset, then each feature was shuffled repeatedly on the held-out test dataset. Importance is reported as the mean decrease in accuracy, with the standard deviation across 20 repeats.
Feature Importance Results
Rank	Feature	Mean Importance	Standard Deviation
1	sex	0.1939	0.0235
2	pclass	0.0657	0.0220
3	sibsp	0.0176	0.0157
4	age	0.0112	0.0204
5	parch	0.0080	0.0095
6	fare	0.0074	0.0031
7	embarked	0.0051	0.0043
8	alone	-0.0109	0.0118


Key Findings
- sex had the largest measured importance (0.1939), meaning shuffling it caused the largest average reduction in accuracy.
- pclass was the second most important feature (0.0657).
- sibsp, age, parch, fare, and embarked had smaller measured contributions in this evaluation.
- alone had slightly negative importance (-0.0109), meaning the model's accuracy was marginally higher on average when that feature was shuffled. This can occur due to sampling variability or redundancy with other features.
- Feature importance measures predictive usefulness in this model; it does not establish that a feature causes survival outcomes.
This analysis used the held-out test set, so it should be treated as exploratory. For a final unbiased assessment, feature analysis and model choices should be performed with validation data or cross-validation, leaving the test set for final evaluation.
Files Created on Day 36
1. notebook/feature_importance_analysis.py — preprocesses the features, trains a Logistic Regression pipeline, calculates permutation importance over 20 repeats, and saves a table and chart.
2. output/feature_importance.csv — contains the mean permutation importance and standard deviation for each feature.
3. output/feature_importance.png — visualizes the feature-importance results as a horizontal bar chart with variability bars.
Day 36 Summary
Permutation importance identified sex and pclass as the strongest predictive features in this evaluation. The results table and chart were saved in the output/ directory for documentation and further analysis.
Day 37 – Model Error Analysis
On Day 37, the Logistic Regression pipeline was retrained on the existing training split and evaluated on the same 156-row test split. The script compared predicted outcomes with actual survival labels, identified incorrect predictions, calculated overall error counts, summarized error rates by available passenger groups, and saved a confusion matrix chart.
Model Error Results
Metric	Result
Test passengers	156
Correct predictions	125
Incorrect predictions	31
Accuracy	80.13%
False positives	18
False negatives	13


Confusion Matrix
Actual outcome	Predicted did not survive (0)	Predicted survived (1)
Did not survive (0)	74	18
Survived (1)	13	51


Key Findings
- The model correctly classified 125 of the 156 test passengers and incorrectly classified 31.
- There were 18 false positives: passengers predicted to survive who did not survive.
- There were 13 false negatives: passengers predicted not to survive who survived.
- The accuracy of 80.13% matches the prior evaluation on this same split.
- The error analysis is descriptive. It helps identify patterns in mistakes but does not establish why any individual passenger survived or did not survive.
Files Created on Day 37
1. notebook/model_error_analysis.py — trains the Logistic Regression pipeline, generates test predictions, categorizes prediction errors, calculates error summaries, and creates a confusion matrix chart.
2. output/prediction_results.csv — includes test features, actual outcomes, predictions, predicted survival probabilities, and whether each prediction was correct.
3. output/misclassified_passengers.csv — includes only passengers whose predictions were incorrect.
4. output/error_analysis_summary.csv — records total passengers, correct and incorrect predictions, accuracy, false positives, and false negatives.
5. output/error_rates_by_group.csv — summarizes incorrect predictions and error rates for available groups such as sex, passenger class, embarkation, and alone status.
6. output/error_analysis_confusion_matrix.png — visualizes actual versus predicted outcomes.
Day 37 Summary
The model achieved 80.13% accuracy on the existing 156-row test set, with 31 incorrect predictions (18 false positives and 13 false negatives). Prediction details, misclassified rows, summary metrics, group-level error rates, and a confusion matrix chart were saved in the output/ directory. Because this is the same held-out test set used in earlier work, these findings should be treated as exploratory rather than used repeatedly to tune the model.
Day 38 – Model Performance by Passenger Group
On Day 38, the Logistic Regression pipeline was trained on the existing training split and evaluated on the same held-out test split. Performance was compared across available passenger groups, including sex, passenger class, age group, embarkation code, and alone status.
Overall Results
Metric	Result
Training passengers	624
Test passengers	156
Overall accuracy	80.13%


Selected Group Results
Passenger group	Passengers	Accuracy	Incorrect predictions
Second class (pclass = 2)	30	96.67%	1
Third class (pclass = 3)	76	77.63%	17
First class (pclass = 1)	50	74.00%	13
Young adults (19–35)	86	82.56%	15
Children (0–12)	8	50.00%	4


Key Findings
- The overall test accuracy remained 80.13%.
- Second-class passengers had the highest accuracy among the listed passenger classes, at 96.67% (29 correct out of 30).
- First-class passengers had 74.00% accuracy, and third-class passengers had 77.63% accuracy.
- The child age group had 50.00% accuracy, but it contained only eight passengers, so this result is uncertain and should not be generalized.
- Group metrics depend on group size and class balance. They describe this test split and do not establish causes or guarantee future performance.
- Encoded categorical values such as sex and embarked are retained as numeric codes; they should not be assigned labels unless the encoding mapping is verified.
Files Created on Day 38
1. notebook/group_performance_analysis.py — trains the Logistic Regression pipeline and calculates group-level performance metrics.
2. output/group_performance_report.csv — records passenger count, accuracy, precision, recall, F1-score, incorrect predictions, and error rate for each group.
3. output/group_error_summary.csv — provides a compact summary of group sizes and error rates.
4. output/group_performance_comparison.png — visualizes accuracy across the analyzed groups.
The same held-out test split was used in previous evaluation tasks. This analysis is exploratory and should not be repeatedly used to tune the model against the test data.
Day 39 – Prediction Threshold Analysis
On Day 39, a Random Forest classification pipeline was trained using the numeric feature columns from output/titanic_cleaned.csv. The script compared survival prediction probabilities across thresholds from 0.20 to 0.80. This is a preliminary threshold experiment; the model and feature preparation are not confirmed to be identical to the Logistic Regression workflow used in previous evaluation days.
Results
Threshold	Accuracy	Precision (survived)	Recall (survived)	F1-score (survived)	Predicted survivors
0.20	48.08%	43.09%	82.81%	56.68%	123
0.30	57.05%	48.54%	78.12%	59.88%	103
0.40	61.54%	52.33%	70.31%	60.00%	86
0.50	66.03%	57.97%	62.50%	60.15%	69
0.60	65.38%	58.62%	53.12%	55.74%	58
0.70	63.46%	57.45%	42.19%	48.65%	47
0.80	64.74%	61.54%	37.50%	46.60%	39


Key Findings
- Threshold 0.50 produced the highest accuracy in this run (66.03%) and the highest survivor-class F1-score (60.15%).
- Threshold 0.80 produced the highest survivor-class precision (61.54%), but recall fell to 37.50%.
- Threshold 0.20 produced the highest survivor-class recall (82.81%), but accuracy was 48.08%.
- Lower thresholds classified more passengers as survivors, while higher thresholds classified fewer passengers as survivors in this run.
- Threshold selection depends on the goal and should consider precision, recall, and the costs of different errors rather than accuracy alone.
Files Created on Day 39
1. notebook/threshold_analysis.py — trains the preliminary Random Forest pipeline and compares classification metrics at seven thresholds.
2. output/threshold_analysis.csv — stores accuracy, precision, recall, F1-score, and predicted survivor counts for each threshold.
3. output/threshold_analysis.png — plots the four classification metrics across thresholds.
Important comparability note: Earlier days reported 80.13% accuracy for a Logistic Regression workflow, while this Day 39 script uses a newly trained Random Forest pipeline and numeric-only features. Therefore, the 66.03% accuracy at threshold 0.50 should not be interpreted as a direct deterioration from the earlier model. For a valid threshold comparison of the existing model, use the same trained model, preprocessing, features, and held-out test split as the original evaluation. The results are exploratory and should not be used repeatedly to tune against the test set.
Day 40 – Threshold Selection Analysis
On Day 40, the results generated on Day 39 were reused to identify the best tested threshold for each evaluation metric. This step did not retrain the model; it summarized the existing threshold results and created a comparison chart.
Results
Selection metric	Selected threshold	Score
Best accuracy	0.50	66.03%
Best precision	0.80	61.54%
Best recall	0.20	82.81%
Best F1-score	0.50	60.15%


Key Findings
- Threshold 0.50 was the best tested threshold for accuracy and F1-score in the Day 39 experiment.
- Threshold 0.80 had the highest precision, while threshold 0.20 had the highest recall.
- For this educational exercise, threshold 0.50 is the F1-based recommendation because it achieved the highest F1-score among the tested values.
- There is no universally best threshold: the appropriate choice depends on the problem and the relative cost of false positives and false negatives.
Files Created on Day 40
1. notebook/threshold_selection_analysis.py — reads the Day 39 metrics, identifies the best tested threshold for each metric, and creates a chart.
2. output/threshold_selection_summary.csv — records the selected threshold and corresponding scores for each metric.
3. output/threshold_selection_comparison.png — compares accuracy, precision, recall, and F1-score across the tested thresholds and marks the best-F1 threshold.
Evaluation note: These results are based on the exploratory Day 39 Random Forest run, which differs from the earlier Logistic Regression workflow. They should not be directly compared with earlier model scores. In a rigorous machine-learning workflow, choose the threshold using validation data and reserve the test set for final evaluation.
📝 Change Log
The following changes were made during data cleaning:
| Issue                            | Column      | Action Taken                      |
| -------------------------------- | ----------- | --------------------------------- |
| Missing values                   | Age         | Filled using median               |
| Missing values                   | Embarked    | Filled using mode                 |
| Missing values                   | Embark Town | Filled using embarkation mapping  |
| High missing values              | Deck        | Removed column                    |
| Duplicate records                | All columns | Removed exact duplicates          |
| Duplicate records after cleaning | All columns | Removed additional duplicate rows |
A detailed change log is available in:
output/change_log.csv
📊 Current Internship Progress
Day 40 / 45 completed
Progress: 88.9%
Completed Work
- Day 1: Internship setup and understanding Task 1
- Day 2: GitHub repository and project structure
- Day 3: Titanic dataset and column understanding
- Day 4: Raw dataset inspection
- Day 5: Missing value handling
- Day 6: Data cleaning change log
- Day 7: Duplicate record handling
- Day 8: Final duplicate verification
- Day 9: Data type and text consistency checks
- Day 10: Range and validity checks
- Day 11: Data consistency checks
- Day 12: Final dataset integrity validation
- Day 13: Final cleaning documentation
- Day 14: Exploratory data analysis
- Day 15: Survival analysis by gender and class
- Day 16: Survival analysis by age group
- Day 17: Survival analysis by embarkation port
- Day 18: Survival analysis by fare group
- Day 19: Survival analysis by gender and passenger class
- Day 20: Survival analysis by family size
- Day 21: Survival analysis by travel group size
- Day 22: Survival analysis by passenger status
- Day 23: Survival analysis by alone status
- Day 24: Passenger demographic distribution analysis
- Day 25: Correlation and relationship analysis
- Day 26: Multi-variable survival analysis
- Day 27: Outlier detection and analysis
- Day 28: Fare group and passenger class survival analysis
- Day 29: Feature engineering and derived variable analysis
Day 30: Key insights and findings from exploratory data analysis
- Day 31: Model data preparation for future survival prediction
- Day 31 output: output/survival_model_ready.csv
- Day 31 output: output/model_preparation_summary.csv
- Day 32: Train-test split preparation using an 80/20 split, random state 42, and stratification by survived
- Day 32 output: output/survival_train.csv
- Day 32 output: output/survival_test.csv
- Day 32 output: output/train_test_split_summary.csv
- Day 33: Logistic Regression model training and evaluation
- Day 33 accuracy: 80.13% on the 156-row test dataset
- Day 33 output: output/logistic_regression_metrics.csv
- Day 33 output: output/survival_test_predictions.csv
- Day 33 output: output/confusion_matrix.csv
- Day 34: Compared Logistic Regression and Decision Tree models on the same train/test split
- Day 34 result: Logistic Regression achieved 80.13% test accuracy; Decision Tree achieved 77.56%
- Day 34 output: output/model_comparison.csv
- Day 34 output: output/model_comparison_predictions.csv
- Day 35: Evaluated Logistic Regression at five classification thresholds and reviewed class-level metrics
- Day 35 result: Threshold 0.50 achieved 80.13% accuracy and a 76.69% F1-score for the survivor class on the test set
- Day 35 output: output/threshold_comparison.csv
- Day 35 output: output/classification_report.csv
- Day 35 output: output/evaluation_confusion_matrix.csv
- Day 35 output: output/survival_test_evaluation.csv
- Day 36: Analyzed model feature importance using permutation importance
- Day 36 finding: sex had the highest mean importance (0.1939), followed by pclass (0.0657)
- Day 36 output: output/feature_importance.csv
- Day 36 output: output/feature_importance.png
- Day 37: Analyzed Logistic Regression prediction errors on the existing test split
- Day 37 result: 125 correct and 31 incorrect predictions across 156 test passengers (80.13% accuracy)
- Day 37 error types: 18 false positives and 13 false negatives
- Day 37 output: output/prediction_results.csv
- Day 37 output: output/misclassified_passengers.csv
- Day 37 output: output/error_analysis_summary.csv
- Day 37 output: output/error_rates_by_group.csv
- Day 37 output: output/error_analysis_confusion_matrix.png
- Day 38: Compared model performance across passenger groups
- Day 38 result: Overall accuracy remained 80.13%; second-class group accuracy was 96.67% (30 passengers), and child group accuracy was 50.00% (8 passengers)
- Day 38 output: output/group_performance_report.csv
- Day 38 output: output/group_error_summary.csv
- Day 38 output: output/group_performance_comparison.png
- Day 39: Compared survival prediction thresholds from 0.20 to 0.80
- Day 39 result: Threshold 0.50 had the highest accuracy (66.03%) and F1-score (60.15%) in the preliminary Random Forest run; threshold 0.80 had the highest precision (61.54%), while threshold 0.20 had the highest recall (82.81%)
- Day 39 output: output/threshold_analysis.csv
- Day 39 output: output/threshold_analysis.png
- Day 40: Compared threshold-selection metrics and identified the best tested threshold for accuracy, precision, recall, and F1-score
- Day 40 result: Threshold 0.50 had the highest accuracy (66.03%) and F1-score (60.15%); threshold 0.80 had the highest precision (61.54%), while threshold 0.20 had the highest recall (82.81%) in the Day 39 experiment
- Day 40 output: output/threshold_selection_summary.csv
- Day 40 output: output/threshold_selection_comparison.png
✅ Final Outcome
The Titanic dataset was successfully cleaned, validated, and analyzed.
The final dataset contains:
- No missing values
- No duplicate rows
- Valid data ranges
- Consistent categorical values
- Correct data types
- Valid column structure
A baseline Logistic Regression model was trained and evaluated, achieving 80.13% test accuracy. On Day 34, Logistic Regression and Decision Tree were compared using the same split; Logistic Regression achieved 80.13% test accuracy, while Decision Tree achieved 77.56%. On Day 35, Logistic Regression was evaluated across five classification thresholds, with threshold 0.50 achieving 80.13% accuracy and a 76.69% survivor-class F1-score on the held-out test set. Model comparison, threshold metrics, classification report, confusion matrix, and predictions were saved for reproducibility. On Day 36, permutation importance identified sex and passenger class as the strongest predictive features in the exploratory analysis. Feature-importance values and a chart were saved for reproducibility. On Day 37, the model correctly predicted 125 of 156 test passengers (80.13% accuracy) and made 31 errors: 18 false positives and 13 false negatives. Prediction-level results, misclassified passengers, group-level error rates, a summary, and a confusion matrix chart were saved for further review. On Day 38, model performance was compared across passenger groups. The model retained 80.13% overall test accuracy; second-class passengers had 96.67% accuracy in this test split, while the child age group had 50.00% accuracy across only eight passengers. Group metrics and a comparison chart were saved for exploratory review. On Day 39, a separate Random Forest pipeline was evaluated across seven prediction thresholds. Threshold 0.50 achieved 66.03% accuracy and a 60.15% survivor-class F1-score in this run; threshold 0.80 had the highest precision (61.54%), and threshold 0.20 had the highest recall (82.81%). Because this experiment uses a different model setup from the earlier Logistic Regression evaluation, its metrics are documented separately and are not directly comparable. On Day 40, the Day 39 threshold results were summarized to identify the best tested threshold by metric. Threshold 0.50 was selected for the exercise's F1-based recommendation, with 66.03% accuracy and a 60.15% F1-score; threshold 0.80 led in precision (61.54%), and threshold 0.20 led in recall (82.81%). The summary CSV and comparison chart were saved. This threshold analysis remains exploratory and uses a different model setup from the earlier Logistic Regression workflow; threshold selection should ideally use validation data rather than repeatedly tuning on the test set.
Exploratory analysis was performed to understand survival patterns based on:
- Gender
- Passenger class
- Age group
- Embarkation port
- Fare group
- Gender and passenger class together
- Family size
- Travel group size
- Passenger status
- Alone status
- Fare group and passenger class
- Derived feature groups
Key survival insights from exploratory data analysis
Passenger demographic distribution was also analyzed across:
- Age groups
- Gender
- Passenger class
- Family size
- Travel status
Correlation and relationship analysis was performed across:
- Survival and passenger class
- Survival and fare
- Survival and age
- Survival and alone status
- SibSp and alone status
- Parch and alone status
- Passenger class and fare
- Family size and survival
Multi-variable survival analysis was performed using:
- Age group and gender
- Passenger class and gender
- Passenger class and age group
- Age group, gender, and passenger class
Outlier analysis was performed using the IQR method across:
- Age
- Fare
- SibSp
- Parch
- Family size
The identified outliers were reviewed and retained because they may represent genuine passenger observations.
Fare group and passenger class analysis was also performed to examine survival patterns across combined fare and class categories.
Feature engineering was performed to create:
- Family size
- Family size group
- Age group
- Fare group
- Travel status
The derived features were analyzed to identify additional survival patterns.
The model-ready data was also divided into training and testing sets using a reproducible, stratified 80/20 split.
The project demonstrates practical use of Python, Pandas, Matplotlib, data cleaning, data validation, exploratory data analysis, correlation analysis, relationship analysis, multi-variable analysis, outlier detection, feature engineering, grouped analysis, and Git/GitHub.
👨‍💻 Author
Vishnu Kumar
Data Analytics Intern
Veda Technology
GitHub:
https://github.com/vishnuvk-coder/Veda-Technology-Data-Analytics