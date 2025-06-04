""" 
NumPy nan_to_num Function Explanation
The line np.nan_to_num(arr, [2], nan=num, posinf=2, neginf=4)
is used to replace NaN (Not a Number) values in a NumPy array with a specified number (num). 
replaces NaN values in the array with num,
and replaces positive infinity with 2 and negative infinity with 4.

This function is useful for cleaning data by replacing NaN and infinite values with specified numbers.

"""

import numpy as np

# Create sample array with NaN values
arr = np.array([1, 2, np.nan, 4, 5, np.nan])

print("Original Array:", arr)

# Basic replacement of NaN with 10
print("Replace NaN with 10:", np.nan_to_num(arr, nan=10))

# Replace NaN and handle infinities
arr_with_inf = np.array([1, np.nan, np.inf, -np.inf, 5])
print("\nArray with inf:", arr_with_inf)
print("Replaced values:", np.nan_to_num(arr_with_inf, 
    nan=0,       # Replace NaN with 0
    posinf=1e10, # Replace +inf with 1e10
    neginf=-1e10 # Replace -inf with -1e10
))

# In-place modification
arr_copy = arr.copy()
np.nan_to_num(arr_copy, copy=False, nan=-1)  # Modifies array directly
print("\nIn-place modification:", arr_copy)

"""
Key Parameters for np.nan_to_num:
x: Input array
nan: Value to replace NaN (default: 0)
posinf: Value to replace positive infinity (default: large finite number)
neginf: Value to replace negative infinity (default: large negative finite number)
copy: Whether to create a copy (default: True)

The original code had an incorrect parameter [2] which should be removed as it's not a valid parameter for nan_to_num.
"""
