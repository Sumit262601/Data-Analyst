import pandas as pd

data = {
    "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28,34,22,30,None,40,25, 32],
    "Salary": [50000,None,None, 52000,49000, 70000,None, 58000],
    "Performance_Score": [85,None,78,92,None,95,80, 89]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())


