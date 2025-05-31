"""
NumPy Insert Operations

Definition
    numpy.insert() is a function that inserts values along a given axis before specified indices in a NumPy array. It returns a new array with inserted values.

Syntax
    numpy.insert(arr, obj, values, axis=None)
    
Parameters
    arr: Input array where values will be inserted.
    obj: Indices before which values are inserted. Can be an integer, slice, or array of integers.
    values: Values to be inserted into the array.
    axis: Axis along which to insert values. If None, the input array is flattened.
"""

import numpy as np

# 1. Basic 1D array insertion
arr = np.array([1, 2, 3, 4, 5])
result = np.insert(arr, 2, 10)  # Insert 10 at index 2
print("1D Insert:", result)  # [1 2 10 3 4 5]

# 2. Multiple value insertion
arr = np.array([1, 2, 3, 4])
result = np.insert(arr, 1, [10, 20])
print("Multiple values:", result)  # [1 10 20 2 3 4]

# 3. 2D array insertion along axis
arr_2d = np.array([[1, 2], [3, 4]])
# Insert along row (axis=0)
row_insert = np.insert(arr_2d, 1, [5, 6], axis=0)
print("\n2D Row Insert:\n", row_insert)

# Insert along column (axis=1)
col_insert = np.insert(arr_2d, 1, [5, 6], axis=1)
print("\n2D Column Insert:\n", col_insert)

# 4. Advanced: Insert at multiple positions
arr = np.array([1, 2, 3, 4])
result = np.insert(arr, [1, 3, 4], [10, 20, 30])
print("\nMultiple positions:", result)

"""Key Features
Axis-based Insertion

axis=None: Flattens array before insertion
axis=0: Insert along rows
axis=1: Insert along columns
Multiple Insertion Points

Can insert at multiple indices simultaneously
Supports array of indices
Broadcasting

Automatically broadcasts values if dimensions match
Interview Questions
Q: What happens when axis=None in np.insert()?

A: The array is flattened before insertion
Q: Can you insert multiple values at different positions?

A: Yes, using arrays for both positions and values
Q: What's the difference between insert and append?

A: Insert adds elements at specified positions, append adds at the end
Best Practices
Always verify array dimensions before insertion
Use appropriate axis parameter for multi-dimensional arrays
Consider memory efficiency for large arrays
Check output shape after insertion
Common Use Cases
Data augmentation
Feature engineering
Time series data modification
Matrix manipulation
Performance Tips
Pre-allocate arrays when possible
Use batch insertions instead of multiple single insertions
Consider alternative methods for large-scale operations
Use appropriate data types to save memory
Remember: insert() always returns a new array, the original array remains unchanged."""