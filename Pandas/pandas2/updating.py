import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28,34,22,30,29,40,25, 32],
    "Salary": [50000,60000,45000, 52000,49000, 70000,48000, 58000],
    "Performance_Score": [85,90,78,92,88,95,80, 89]
}

df = pd.DataFrame(data)
print(df)

# .loc[] -> use access a specific cell, rows, set of rows / columns, for modify the dataset
# df.loc[index_value, "Column_Name"] = new_values
df.loc[0, "Salary"] = 55000
print('\n',df)


# =================================== INCREASEING MANY VALUES ===================================
df['Salary'] = df['Salary'] * 1.05
print('\n',df)


