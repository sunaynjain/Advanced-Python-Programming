import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

data = {
    "Age": [24, 27, 22, 32, 29, 25, 100],
    "Salary": [50000, 60000, 52000, 58000, 62000, 55000, 600000]
}

df = pd.DataFrame(data)

print("Descriptive Statistics:")
print(df.describe())

print("\nMean:", df["Age"].mean())
print("Median:", df["Age"].median())
print("Mode:", df["Age"].mode()[0])

plt.hist(df["Age"], bins=5, edgecolor="black")
plt.title("Age Distribution")
plt.show()

sns.boxplot(y=df["Age"])
plt.title("Box Plot of Age")
plt.show()

plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

df["Age_zscore"] = zscore(df["Age"])
df["Salary_zscore"] = zscore(df["Salary"])

print("\nData with Z-scores:")
print(df)

df_cleaned = df[
    (df["Age_zscore"].abs() <= 3) &
    (df["Salary_zscore"].abs() <= 3)
]

print("\nData after Removing Outliers:")
print(df_cleaned)
