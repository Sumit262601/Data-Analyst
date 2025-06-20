import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun', 'Narun', 'Marun'],
    "Age": [28,34,22,34,28],
    "Salary": [50000, 60000, 45000, 52000, 480000]
}

# ===================== GROUPING FOR A SINGLE COLUMN ==================
df = pd.DataFrame(data)
# grouped = df.groupby("Age") ["Salary"].sum()
# print(grouped)

# ===================== GROUPING FOR A MULTIPLE COLUMN ==================
grouped = df.groupby(["Age", "Name"]) ["Salary"].sum()
print(grouped)

"""
dr.groupby("Age")
age = 22 > [45000]
age = 28 [500000, 480000]
age = 34 [60000, 52000]

[Salary].sum()
age = 22 > [45000] =
age = 28 [50000,480000] = 530000
age = 34 [60000, 52000] = 11200


1- sum()
2- mean()
3- count()
4- min()
5- max()
6- std() |

"""