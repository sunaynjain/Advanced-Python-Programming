import pandas as pd
import numpy as np

numbers = np.random.randint(1, 100, 10)

series = pd.Series(numbers)

print("Pandas Series:")
print(series)

data = {
    "Name": ["Amit", "Rahul", "Neha", "Priya"],
    "Age": [20, 21, 22, 23]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nName Column:")
print(df["Name"])

print("\nFirst Row:")
print(df.iloc[0])
