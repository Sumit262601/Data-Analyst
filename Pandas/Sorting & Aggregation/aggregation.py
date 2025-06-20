"""df ["Column Name"].mean()
df ["Column Name"].sum()
df["Column Name"].min()
df ["Column Name"].max()"""

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28,34,22],
    "Salary": [10000,20000,30000]
}
df = pd.DataFrame(data)

avg_salary = df ['Salary']. mean()
max_salary = df ['Salary']. max()
min_salary = df ['Salary']. min()
sum_salary = df ['Salary']. sum()
print(avg_salary)
print(max_salary)
print(min_salary)
print(sum_salary)