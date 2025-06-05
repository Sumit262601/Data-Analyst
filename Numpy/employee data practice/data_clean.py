import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('employee data practice/employee_data.csv')
print("Initial dataset preview:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values
# Fill missing salaries with the mean
df['Salary (INR)'].fillna(df['Salary (INR)'].mean(), inplace=True)

# Fill missing performance ratings with the median
df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace=True)

# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill remaining NaN values in numerical columns with their mean
df.fillna(df.select_dtypes(include=[np.float32]).mean(), inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Replace negative salaries with the mean salary
df['Salary (INR)'] = np.where(df['Salary (INR)'] <0, df['Salary (INR)'].mean(), df['Salary (INR)'])

# Handle outliers using the 3-sigma rule
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]


# Save the cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nData cleaning completed successfully. File saved as 'cleaned_employee_data.csv'")
