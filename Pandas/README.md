# Pandas Project: Basic to Advanced Guide

## Introduction

**Pandas** is a powerful, open-source Python library for data analysis and manipulation. It provides flexible data structures like Series (1D) and DataFrame (2D) for handling structured data efficiently.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Operations](#basic-operations)
3. [Intermediate Operations](#intermediate-operations)
4. [Advanced Operations](#advanced-operations)
5. [Interview Questions & Answers](#interview-questions--answers)
6. [References](#references)

---

## Getting Started

### Installation

```bash
pip install pandas
```

### Importing Pandas

```python
import pandas as pd
```

---

## Basic Operations

### Creating Series and DataFrames

```python
import pandas as pd

# Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 22, 35]
}
df = pd.DataFrame(data)
```

### Reading and Writing Data

```python
# Read CSV
df = pd.read_csv('data.csv')

# Write to CSV
df.to_csv('output.csv', index=False)
```

### Selecting Data

```python
# Select column
df['Name']

# Select row by index
df.iloc[0]

# Filter rows
df[df['Age'] > 25]
```

---

## Intermediate Operations

### Handling Missing Data

```python
# Fill missing values
df.fillna(0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
```

### Data Aggregation

```python
# Group by column and calculate mean
df.groupby('Name')['Age'].mean()
```

### Merging and Joining

```python
# Merge two DataFrames
merged = pd.merge(df1, df2, on='key')
```

### Sorting

```python
df.sort_values('Age', ascending=False)
```

---

## Advanced Operations

### Pivot Tables

```python
pivot = df.pivot_table(values='Age', index='Name', columns='City', aggfunc='mean')
```

### Applying Functions

```python
# Apply a function to a column
df['Age'] = df['Age'].apply(lambda x: x + 1)
```

### Time Series

```python
# Convert column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set as index
df.set_index('Date', inplace=True)
```

### Custom Aggregations

```python
df.groupby('City').agg({'Age': ['mean', 'max'], 'Salary': 'sum'})
```

---

## Interview Questions & Answers

### Q1: What is a DataFrame in Pandas?
**A:** A DataFrame is a 2-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns).

---

### Q2: How do you handle missing data in Pandas?
**A:** Use `df.fillna()` to fill missing values, or `df.dropna()` to remove rows/columns with missing values.

---

### Q3: How can you merge two DataFrames?
**A:** Use `pd.merge(df1, df2, on='key')` for SQL-style joins, or `df1.join(df2)` for joining on index.

---

### Q4: Explain the difference between `loc` and `iloc`.
**A:** `loc` selects data by label, while `iloc` selects data by integer position.

---

### Q5: How do you group data and calculate summary statistics?
**A:** Use `df.groupby('column').agg({'col1': 'mean', 'col2': 'sum'})` to group and aggregate data.

---

### Q6: What is a pivot table in Pandas?
**A:** A pivot table summarizes data by grouping and aggregating values, similar to Excel pivot tables, using `pd.pivot_table()`.

---

### Q7: How do you handle large datasets efficiently in Pandas?
**A:** Use chunking (`pd.read_csv(..., chunksize=...)`), optimize data types, and use vectorized operations.

---

## References

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Tutorials - Real Python](https://realpython.com/learning-paths/pandas/)
- [Kaggle Pandas Course](https://www.kaggle.com/learn/pandas)

---

*This README provides a structured overview of Pandas from basics to advanced, with practical code examples and interview Q&A for professional preparation.*