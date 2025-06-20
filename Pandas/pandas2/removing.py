import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28,34,22,30,29,40,25, 32],
    "Salary": [50000,60000,45000, 52000,49000, 70000,48000, 58000],
    "Performance_Score": [85,90,78,92,88,95,80, 89]
}

df = pd.DataFrame(data)
print(df)

# FOR REMOVING A SINGLE COLUMNS IN DATASET
# df.drop(columns=["Column_Nmae"], inplace=True) inplace to remove data in original dataset grather than False condition to show new dataframe they does't change in original dataset

print('\nModify DataSet ============================')
df.drop(columns=["Performance_Score"], inplace=True) 
print(df)