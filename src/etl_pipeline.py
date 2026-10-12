import csv
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("EmployeeETL").getOrCreate()

# Step 1: Read CSV data
df = spark.read.option("header", True).option("inferSchema", True).csv("data/employees.csv")

# Step 2: Remove duplicate employee IDs
df_cleaned = df.dropDuplicates(["employee_id"])

# Step 3: Replace missing departments
df_cleaned = df_cleaned.fillna({"department": "Unknown"})

df_cleaned = df_cleaned.filter(df_cleaned.salary >= 30000)

df_cleaned = df_cleaned.orderBy(df_cleaned.salary.desc())

with open("output/cleaned_employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(df_cleaned.columns)
    writer.writerows(df_cleaned.collect())

print("Cleaned CSV file saved successfully!")

department_salary = df_cleaned.groupBy("department").agg(
    avg("salary").alias("average_salary")
)

print("Department-wise Average Salary:")
department_salary.show()

# Display the result
print("Employee count:", df_cleaned.count())
df_cleaned.show()

spark.stop()
