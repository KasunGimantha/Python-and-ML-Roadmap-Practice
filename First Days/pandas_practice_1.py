import pandas as pd

df = pd.read_csv("data.csv")


print(df.head(5))
print("\n")
print(df.columns)

by_salary = df[df['Salary'] > 50000]
print(by_salary)
