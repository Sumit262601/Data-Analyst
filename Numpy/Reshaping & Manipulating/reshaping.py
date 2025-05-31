"""
Reshaping in Python NumPy - Comprehensive Guide

Definition: -
Reshaping in Python (specifically with NumPy) is the process of reorganizing array elements into a new shape while keeping the total number of elements constant. It allows you to transform the dimensional structure of an array without changing its data.

Key Concepts: -
    The new shape must be compatible with the original shape
    Total elements must remain the same
    Used for data restructuring in machine learning and data analysis
    Reshaping can be done using methods like reshape(), resize(), and ravel()
    The choice of method depends on the specific requirements (e.g., in-place vs. new array)
    Always ensure that the total number of elements remains constant during reshaping
    Be mindful of the data layout (C-contiguous vs. F-contiguous) when reshaping
    Consider using the -1 parameter for automatic dimension calculation
    
Common Methods: -
- reshape(): Returns a new array with the specified shape
- resize(): Modifies the array in-place to the new shape
- ravel(): Flattens the array into a 1D array
- flatten(): Returns a copy of the array collapsed into 1D
- transpose(): Permutes the dimensions of the array
- swapaxes(): Interchanges two axes of the array
- squeeze(): Removes single-dimensional entries from the shape of an array
- expand_dims(): Adds a new axis to the array, increasing its dimensionality
- stack(): Joins a sequence of arrays along a new axis
- hstack(): Stacks arrays in sequence horizontally (column-wise)
- vstack(): Stacks arrays in sequence vertically (row-wise)


NOTE: Reshaping does not change the data, only the view of the data in memory. It is focused they cannot be copy any array data, only the view of the data in memory.


"""

"""Common Reshaping Operations
1. Basic Reshaping Example"""

import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2x3 matrix
matrix = arr.reshape(2, 3)
print("Reshaped Matrix:\n", matrix)
# Result:
# [[1, 2, 3],
#  [4, 5, 6]]

# 2. Using -1 in Reshape

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# NumPy automatically calculates the size for -1
reshaping = arr.reshape(-1, 1)  # Reshapes to 4x2 reshaping
print("Reshaped with -1:\n", reshaping)

# Result:
# [[1, 2],
#  [3, 4],
#  [5, 6],
#  [7, 8]]


"""
Interview Questions
Q: What's the difference between reshape() and resize()?

A: reshape() returns a new array with modified shape while maintaining the same data
resize() modifies the array in-place and can change the total number of elements
Q: Can you reshape an array of 10 elements into a 3x4 matrix?

A: No, because 3x4=12 elements, which doesn't match the original 10 elements
Q: What does reshape(-1, 1) do?

A: It converts an array into a column vector, where -1 automatically calculates the number of rows
Advanced Example
"""

# Create a 3D array
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Reshape to different dimensions
reshaped_1 = arr.reshape(2, 2, 3)  # 2x2x3
reshaped_2 = arr.reshape(-1)        # Flattens to 1D
reshaped_3 = arr.reshape(4, 3)      # 4x3 matrix


print("\nOriginal shape:", arr.shape)
print(arr)

print("\nReshaped to 2x2x3:", reshaped_1.shape)
print(reshaped_1)

print("\nFlattened shape:", reshaped_2.shape)
print(reshaped_2)

print("\nReshaped to 4x3:", reshaped_3.shape)
print(reshaped_3)

"""
Common Use Cases
    Feature engineering in machine learning
    Image processing (reshaping pixel matrices)
    Time series data restructuring
    Batch processing in deep learning

Best Practices
    Always verify shape compatibility before reshaping
    Use -1 when one dimension is flexible
    Consider using ravel() for flattening arrays
    Check array contiguity with is_contiguous()

This knowledge is essential for data preprocessing, machine learning, and array manipulations in Python.
"""