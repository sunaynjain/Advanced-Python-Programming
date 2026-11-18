import numpy as np
import pandas as pd

salaries = np.array([45000, 55000, 65000, 75000, 90000])

print("Average Salary:", np.mean(salaries))
print("Maximum Salary:", np.max(salaries))
print("Minimum Salary:", np.min(salaries))

data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan"],
    "Salary": salaries
}

df = pd.DataFrame(data)

print("\nAll Employee Details:")
print(df)

print("\nEmployees Earning More Than 60000:")
print(df[df["Salary"] > 60000])
