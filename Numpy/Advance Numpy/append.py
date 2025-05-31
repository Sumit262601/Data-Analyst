"""NumPy Append Operations Guide
Definition
    numpy.append() is a function that appends values to the end of an array. It returns a new array with the appended values.

Syntax
    numpy.append(arr, values, axis=None)

Parameters
    arr: Input array to which values will be appended.
    values: Values to be appended to the array.
    axis: Axis along which to append values. If None, the input array is flattened.

Returns
    A new array with the appended values.
"""

# Basic Examples

import numpy as np

# 1. Basic 1D array append
arr = np.array([1, 2, 3])
result = np.append(arr, 4)
print("1D Append:", result)  # [1 2 3 4]

# 2. Multiple value append
arr = np.array([1, 2, 3])
result = np.append(arr, [4, 5, 6])
print("Multiple values:", result)  # [1 2 3 4 5 6]

# 3. 2D array append along axis
arr_2d = np.array([[1, 2], [3, 4]])
# Append along row (axis=0)
row_append = np.append(arr_2d, [[5, 6]], axis=0)
print("\n2D Row Append:\n", row_append)

# Append along column (axis=1)
col_append = np.append(arr_2d, [[5], [6]], axis=1)
print("\n2D Column Append:\n", col_append)


"""Key Features
Axis-based Appending

    axis=None: Flattens arrays before appending
    axis=0: Append along rows
    axis=1: Append along columns

Shape Requirements
    When using axis, shapes must match except in the dimension corresponding to axis

Interview Questions
Q: What's the difference between append() and concatenate()?

    A: append() is a simplified version of concatenate(), mainly for adding elements to end of 1D arrays
Q: Can you append multiple arrays at once?

    A: No, use concatenate() for multiple arrays. append() only works with two arrays
Q: What happens when axis=None?

    A: Arrays are flattened before appending

Best Practices
    Use appropriate axis parameter for multi-dimensional arrays
    Verify array shapes before appending
    Consider using concatenate() for complex operations
    Check output shape after appending
"""


# Advanced usage with different shapes
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

# Append with axis specification
result = np.append(arr1, arr2, axis=0)
print("\nAdvanced append:\n", result)

# Append with reshaping
arr3 = np.array([7, 8])
result = np.append(arr1, arr3.reshape(1, 2), axis=0)
print("\nAppend with reshape:\n", result)

"""
Common Use Cases
    Growing datasets dynamically
    Adding new features to datasets
    Combining data arrays
    Time series data expansion

Performance Tips
    Pre-allocate arrays when possible
    Use concatenate() for multiple arrays
    Avoid repeated appends in loops
    Consider memory efficiency for large arrays

Remember: append() always returns a new array, the original array remains unchanged.
"""



