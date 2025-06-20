import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28,34,22,30,29,40,25, 32],
    "Salary": [50000,60000,45000, 52000,49000, 70000,48000, 58000],
    "Performance_Score": [85,90,78,92,88,95,80, 89]
}

df = pd.DataFrame(data)
print(df,'\n')

# For adding any columns in the dataset
df["Bonus"] = df["Salary"] * 0.1
print('\n',df)


# use insert() method to add columns in specific index
# df.insert(loc[index], 'Column_name', 'some_data') 
df.insert(0, "Employee Id", [101, 102, 103, 104, 105, 106, 107, 108])
print('\n', df)
