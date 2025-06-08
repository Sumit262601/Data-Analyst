"""
Introduction to Pandas
Pandas is a powerful Python library for data manipulation and analysis. It provides high-performance, easy-to-use data structures and tools for working with structured data.

Key Features
    DataFrame: 2-dimensional labeled data structure
    Series: 1-dimensional labeled array
    **Efficient data manipulation and analysis
    **Handles missing data
    **Merging and joining datasets
    **Powerful data alignment capabilities
"""

# Basic Pandas operations
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 35, 32],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Basic operations
print("\nBasic DataFrame:")
print(df)

# Selecting columns
print("\nSelecting Age column:")
print(df['Age'])

# Filtering data
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# Adding new column
df['Status'] = ['Active', 'Inactive', 'Active', 'Active']

# Basic statistics
print("\nAge statistics:")
print(df['Age'].describe())

# Grouping data
print("\nCount by Status:")
print(df.groupby('Status').size())

"""
Common Operations
Reading Data:

    pd.read_csv()
    pd.read_excel()
    pd.read_sql()
Data Selection:

    df['column']
    df.loc[]
    df.iloc[]
Data Cleaning:

    df.dropna()
    df.fillna()
    df.drop_duplicates()
Data Analysis:

    df.describe()
    df.mean()
    df.groupby()
"""

