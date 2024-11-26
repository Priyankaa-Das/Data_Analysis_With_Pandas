# Data Analysis with Pandas 📊🐼

## Overview

This project demonstrates essential data analysis tasks using the powerful *Pandas* library in Python. It leverages a sample dataset (data.csv) containing employee details to perform insightful analyses, including calculations, data filtering, and data visualization with charts. 🛠✨

## Features 🚀

### 1. *Load and Explore Data*
- Display the first and last few rows of the dataset.
- Generate descriptive statistics for all numerical columns.

### 2. *Data Cleaning*
- Identify missing values in each column.

### 3. *Data Analysis*
- Compute key metrics: average, maximum, and minimum for selected columns (e.g., Age, Salary).
- Count unique values in specific columns.
- Filter data based on custom conditions (e.g., employees in the Engineering department).
- Add a new column categorizing employees as *Senior* or *Junior* based on their age.

### 4. *Data Sorting*
- Sort data by columns like age in ascending or descending order.

### 5. *Data Visualization*
- Create a *Pie Chart* showing employee distribution across departments.
- Generate a *Bar Chart* to count employees in each department.

---

## Requirements 🛠

- *Python* 3.7+
- *Pandas*
- *Matplotlib*

---

## Installation 📥


1. Install required Python libraries:
   bash
   pip install pandas matplotlib
   

3. Place your data.csv file in the same directory as dataanalysis.py.

---

## Usage 💻

1. Run the script:
   bash
   python dataanalysis.py
   

2. Outputs:
   - Analytical summaries printed in the console.
   - Visual insights displayed via pie and bar charts.

3. *Customize your dataset*:
   - Replace the sample data.csv with your own dataset.
   - Ensure the structure (columns) is consistent.

---

## Example Data 📂

A sample data.csv file:

| Name     | Age | Salary  | Department   | Gender |
|----------|-----|---------|--------------|--------|
| Alice    | 30  | 70000   | Engineering  | Male   |
| Bob      | 25  | 50000   | Sales        | Male   |
| Charlie  | 35  | 80000   | Engineering  | Male   |
| Diana    | 28  | 45000   | Marketing    | Female |
| Eve      | 40  | 100000  | Sales        | Female |
| Frank    | 22  | 55000   | Marketing    | Male   |

---

## Outputs and Insights 📈

### Console Output:
- *Statistics*: Average, max, and min for numerical columns (e.g., Age, Salary).
- *Unique Counts*: Department-wise and other column summaries.
- *Filtered Data*: E.g., employees in specific departments or satisfying conditions.

### Visualizations:
1. *Pie Chart*: Distribution of employees across departments.
2. *Bar Chart*: Employee counts per department.

---

## Contributing 🤝

Contributions are welcome!



---

Enjoy exploring and analyzing data with Pandas! 🐼📊
