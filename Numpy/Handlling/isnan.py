"""
Understanding isnan (Is Not a Number) in Python
Overview
(isnan) is a function used to identify "Not a Number" (NaN) values in numerical data. It's particularly important in data analysis and numerical computations.

Key Concepts
Definition

   NaN represents undefined or unrepresentable values
   Common in floating-point arithmetic
   Results from operations like 0/0 or sqrt(-1)
Available Methods

   numpy.isnan(): NumPy's implementation
   math.isnan(): Python's built-in math module
   pd.isna(): Pandas' implementation (also catches None values)
"""


import numpy as np
import math
import pandas as pd

"""
Using isnan in different Python contexts:

1. NumPy Implementation
   - Vectorized operation
   - Works with arrays
   - Most efficient for large datasets

2. Math Module Implementation
   - Works with single values
   - Part of Python standard library
   - Throws TypeError for non-float values

3. Pandas Implementation
   - Works with Series and DataFrames
   - Handles both NaN and None
   - Preferred for data analysis
"""

# Key characteristics of NaN:
# 1. NaN != NaN
# 2. Any operation with NaN results in NaN
# 3. Cannot be compared using standard operators

# Common use cases:
# 1. Data cleaning
# 2. Missing value detection
# 3. Error handling in numerical computations
# 4. Quality assurance in data processing

"""
Important Notes
Properties of NaN

NaN is not equal to itself (NaN != NaN)
Any arithmetic operation with NaN results in NaN
Cannot be compared using standard comparison operators
Best Practices

Always use appropriate isnan function based on data type
Consider using pandas for data analysis tasks
Handle NaN values early in data processing pipeline
Common Applications

Data cleaning and preprocessing
Missing value detection
Scientific computing
Financial calculations
Performance Considerations

NumPy's implementation is fastest for large arrays
Math module is suitable for single value checks
Pandas' implementation adds overhead but provides more functionality
"""

# Examples of using isnan in different contexts

# 1. NumPy Implementation
arr = np.array([1, 2, np.nan, 4, 5])
print("NumPy array with NaN:", arr)
print("NaN detected:", np.isnan(arr))
print("Number of NaN values:", np.isnan(arr).sum())

# 2. Math Module Implementation
x = float('nan')  # Creating a NaN value
print("\nMath module example:")
print("Is x NaN?:", math.isnan(x))

# 3. Pandas Implementation
df = pd.DataFrame({
    'A': [1, np.nan, 3, None],
    'B': [4, 5, np.nan, 7]
})
print("\nPandas DataFrame:")
print(df)
print("\nDetecting NaN values:")
print(pd.isna(df))

# Example of NaN behavior
x = np.nan
y = np.nan
print("\nNaN behavior:")
print("NaN == NaN:", x == y)  # False
print("NaN is NaN:", x is y)  # False

# Common operations with NaN
print("\nOperations with NaN:")
print("NaN + 1:", np.nan + 1)  # NaN
print("NaN * 10:", np.nan * 10)  # NaN
print("sum of array with NaN:", np.sum([1, 2, np.nan, 4, np.nan]))  # NaN