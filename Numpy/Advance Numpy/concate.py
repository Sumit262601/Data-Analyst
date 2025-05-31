"""NumPy Concatenation Operations Guide

Definition:
    numpy.concatenate() joins arrays along a specified axis.
    
Syntax:
    numpy.concatenate((arr1, arr2, ...), axis=0)

Parameters:
    arr1, arr2, ...: Arrays to concatenate. Must have the same shape except in the dimension corresponding to axis.
    axis: Axis along which to concatenate. Default is 0 (vertical concatenation).
    
Returns:
    A new array formed by joining the input arrays along the specified axis.

"""

import numpy as np

# 1. Basic 1D Array Concatenation
print("1. Basic 1D Concatenation")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate((arr1, arr2))
print(f"Concatenated 1D arrays: {result}\n")

# 2. 2D Array Concatenation
print("2. 2D Array Concatenation")
# Along rows (axis=0)
arr1_2d = np.array([[1, 2], [3, 4]])
arr2_2d = np.array([[5, 6], [7, 8]])

# Vertical concatenation (axis=0)
vertical_concat = np.concatenate((arr1_2d, arr2_2d), axis=0)
print("Vertical concatenation (axis=0):")
print(vertical_concat, "\n")

# Horizontal concatenation (axis=1)
horizontal_concat = np.concatenate((arr1_2d, arr2_2d), axis=1)
print("Horizontal concatenation (axis=1):")
print(horizontal_concat, "\n")

# 3. Multiple Array Concatenation
print("3. Multiple Array Concatenation")
arr3_2d = np.array([[9, 10], [11, 12]])
multi_concat = np.concatenate((arr1_2d, arr2_2d, arr3_2d))
print("Concatenating multiple arrays:")
print(multi_concat, "\n")

# 4. Alternative Methods
print("4. Alternative Methods")
# Using vstack (vertical stack)
vstack_result = np.vstack((arr1_2d, arr2_2d))
print("Using vstack:")
print(vstack_result, "\n")

# Using hstack (horizontal stack)
hstack_result = np.hstack((arr1_2d, arr2_2d))
print("Using hstack:")
print(hstack_result, "\n")

# 5. Advanced Example
print("5. Advanced Example")
# Concatenating arrays of different shapes
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5], [6]])
arr3 = np.array([[7], [8]])

# Reshape and concatenate
result = np.concatenate((arr1, arr2, arr3), axis=1)
print("Advanced concatenation:")
print(result)

"""
Key Points:
1. concatenate() requires same dimensions except for the concatenation axis
2. axis parameter determines the direction of concatenation
3. vstack and hstack are convenient alternatives for vertical and horizontal stacking
4. Arrays must have the same shape along all dimensions except the concatenation axis
5. Multiple arrays can be concatenated in a single operation

Common Use Cases:
- Combining datasets
- Merging feature matrices
- Building time series data
- Creating batch data for machine learning

Best Practices:
1. Verify array shapes before concatenation
2. Use appropriate axis parameter
3. Consider memory efficiency for large arrays
4. Use specialized functions (vstack, hstack) when appropriate
"""