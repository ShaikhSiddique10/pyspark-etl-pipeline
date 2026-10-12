# ⚡ PySpark ETL Pipeline - CSV Data Processing

A beginner-friendly, Python-powered ETL pipeline that processes employee data from CSV files using PySpark. It cleans data, removes duplicates, handles missing values, filters records, calculates department-wise average salaries, and exports the cleaned data into a CSV output file.

---

## ✅ Features

Reads employee data from CSV files into Spark DataFrames  
Removes duplicate employee records based on employee ID  
Handles missing department values by replacing them with "Unknown"  
Filters employees based on salary conditions  
Sorts employee records from highest to lowest salary  
Calculates department-wise average salaries  
Exports cleaned and transformed data to a CSV output file  
Validates data processing results using record counts and output inspection

---

## 🛠 Tech Stack

Language: Python 3.11  
Data Processing: PySpark  
Data Format: CSV  
Libraries: PySpark, csv  
Concepts: ETL, Data Cleaning, Data Transformation, Data Aggregation, Data Validation

---

## ⚙️ Installation

Install Python 3.11 or a compatible Python version

Install Java JDK 17

Install PySpark

```bash
python -m pip install pyspark
```

Clone the repository

```bash
git clone https://github.com/ShaikhSiddique10/pyspark-etl-pipeline.git
cd pyspark-etl-pipeline
```

---

## 🚀 Usage

Start the ETL Pipeline

```bash
python src/etl_pipeline.py
```

Use the System

The pipeline reads employee records from `data/employees.csv` and performs the following operations:

Remove duplicate employee IDs  
Replace missing department values with "Unknown"  
Filter out employees earning less than ₹30,000  
Sort employees by salary in descending order  
Calculate department-wise average salaries  
Save the processed data to `output/cleaned_employees.csv`

---

## 📊 Results / Capabilities

Processes employee data using PySpark DataFrames  
Removes duplicate records from the input dataset  
Handles missing department values correctly  
Filters employees based on salary requirements  
Calculates average salary for each department  
Generates a cleaned CSV file containing 9 employee records  
Sorts the final output from highest to lowest salary

---

## 🔁 Example Flow

Input → Employee CSV file containing 11 records

Data Cleaning → Remove duplicate employee IDs and handle missing departments

Transformation → Filter salaries below ₹30,000 and sort records

Aggregation → Calculate department-wise average salaries

Output → Cleaned CSV file containing 9 employee records

---

## 🧠 Key Concepts Demonstrated

Extract, Transform, Load (ETL)  
PySpark DataFrames  
CSV Data Processing  
Data Cleaning and Duplicate Removal  
Missing Value Handling  
Filtering and Sorting  
GroupBy and Aggregation  
Department-wise Average Salary Calculation  
Data Export and Validation

---

## 🎯 Why This Project

This project demonstrates fundamental Data Engineering concepts through a practical ETL pipeline:

Shows how to process structured data using PySpark  
Implements common data cleaning and transformation operations  
Demonstrates aggregation using Spark SQL functions  
Processes CSV data and generates a cleaned output file  
Builds a foundation for more advanced data engineering projects

---

## 👤 Author Info

Siddique Shaikh

📧 [siddiqueshaikh009@gmail.com](mailto:siddiqueshaikh009@gmail.com)

🔗 [https://in.linkedin.com/in/siddique-shaikh-23a776265](https://in.linkedin.com/in/siddique-shaikh-23a776265)

💻 [https://github.com/ShaikhSiddique10](https://github.com/ShaikhSiddique10)
