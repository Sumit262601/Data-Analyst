"""NumPy Delete Operations Guide

Definition:
    numpy.delete() removes specified elements from an array along a specified axis.
    
Syntax:
    numpy.delete(arr, obj, axis=None)

Parameters:
    arr: Input array
    obj: Indices or slice to remove
    axis: Axis along which to delete. Default None means flatten the array first.
"""

import numpy as np

# 1. Basic 1D Array Deletion
print("1. Basic 1D Array Deletion")
arr1d = np.array([1, 2, 3, 4, 5])

# Delete single element
result1 = np.delete(arr1d, 2)  # Delete index 2
print(f"Delete single element: {result1}")

# Delete multiple elements
result2 = np.delete(arr1d, [0, 4])  # Delete first and last elements
print(f"Delete multiple elements: {result2}\n")

# 2. 2D Array Deletion
print("2. 2D Array Deletion")
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Original 2D array:")
print(arr2d, "\n")

# Delete row (axis=0)
row_delete = np.delete(arr2d, 1, axis=0)  # Delete second row
print("After deleting row 1:")
print(row_delete, "\n")

# Delete column (axis=1)
col_delete = np.delete(arr2d, 1, axis=1)  # Delete second column
print("After deleting column 1:")
print(col_delete, "\n")

# 3. Advanced Deletion
print("3. Advanced Deletion")
# Delete using condition
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
condition = arr % 2 == 0  # Delete even numbers
indices = np.where(condition)[0]
result3 = np.delete(arr, indices)
print(f"Delete even numbers: {result3}\n")

# 4. Slice Deletion
print("4. Slice Deletion")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Delete a range of elements
result4 = np.delete(arr, slice(2, 5))  # Delete elements from index 2 to 4
print(f"Delete slice: {result4}\n")

# 5. Complex Example
print("5. Complex Example")
# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]],
                  [[9, 10], [11, 12]]])
print("Original 3D array:")
print(arr3d, "\n")

# Delete along specific axis
result5 = np.delete(arr3d, 1, axis=1)
print("After deleting along axis 1:")
print(result5)

"""
Key Points:
1. delete() returns a new array with elements removed
2. Original array remains unchanged
3. Can delete along any axis in multi-dimensional arrays
4. Can delete using indices, slices, or conditions
5. Axis parameter determines the direction of deletion

Common Use Cases:
- Data cleaning
- Feature selection
- Array manipulation
- Removing outliers

Best Practices:
1. Always specify axis for multi-dimensional arrays
2. Be careful with index ordering
3. Consider memory efficiency for large arrays
4. Verify array shape after deletion
"""