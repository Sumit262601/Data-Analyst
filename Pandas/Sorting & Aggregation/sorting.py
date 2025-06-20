#sorting data
#SORTING DATA 1 COLUMN sort_values()
#df.sort_values(by="Column Name", True/False, inplace = True)

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28,34,22],
    "Salary": [10000,20000, 30000]
}

df = pd.DataFrame(data)

# =============== SORTTING FOR A SINGLE COLUMNS =========================
# df.sort_values(by="Age", ascending=True, inplace=True, ignore_index=True)
# print('Sorted Age by Ascending')
# print(df)

# =============== SORTTING FOR A MULTIPLE COLUMNS =========================
df.sort_values(by=["Age", "Salary"], ascending=[True, True], inplace=True, ignore_index=True)
print('Sorted Age by Ascending')
print(df)

