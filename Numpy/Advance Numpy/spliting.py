"""
NumPy Array Splitting Introduction
NumPy provides several methods for splitting arrays into multiple sub-arrays. Here are the key splitting methods:

Key Splitting Methods:

1. Array Split (np.array_split)
    - Splits array into specified number of sub-arrays
    - Can handle uneven splits
    - Most flexible splitting method

2. Horizontal Split (np.hsplit)
    - Splits array along horizontal axis
    - Splits columns into sub-arrays
    - Must be evenly divisible

3. Vertical Split (np.vsplit)
    - Splits array along vertical axis
    - Splits rows into sub-arrays
    - Must be evenly divisible

4. Deep Split (np.dsplit)
    - Splits array along depth (third axis)
    - Used for 3D arrays
    - Must be evenly divisible
"""

import numpy as np

# Basic array for demonstration
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# print(np.split(arr, 5))

# 1. Basic Array Split
print("1. Basic Array Split:")
split1 = np.array_split(arr, 3)  # Split into 3 parts
print(split1)

# 2. Uneven Split Example
print("\n2. Uneven Split:")
split2 = np.array_split(arr, 5)  # Split into 5 parts (uneven)
print(split2)

# 3. 2D Array Splitting
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("\n3. Original 2D Array:")
print(arr_2d)

# Vertical splitting
print("\n4. Vertical Split (vsplit):")
vsplit = np.vsplit(arr_2d, 3) # Split into 3 vertical parts
for array in vsplit:
    print(array)

# Create a 2D array suitable for horizontal splitting
arr_2d_h = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])

print("\n5. Horizontal Split (hsplit):")
hsplit = np.hsplit(arr_2d_h, 2)
for array in hsplit:
    print(array)

# 3D array example
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

print("\n6. 3D Array Split (dsplit):")
print("Original 3D array shape:", arr_3d.shape)
dsplit = np.dsplit(arr_3d, 2)
for array in dsplit:
    print("\nSplit array:")
    print(array)

# Advanced splitting with indices
print("\n7. Split at specific indices:")
indices_split = np.split(arr, [3, 7, 14])
print("Split at indices 3, 7, and 14:")
for array in indices_split:
    print(array)

"""
This code demonstrates various splitting operations in NumPy:

1. Basic Array Split
   - Splits array into equal or near-equal parts
   - Handles both even and uneven splits

2. 2D Array Splitting
   - Vertical splitting (vsplit)
   - Horizontal splitting (hsplit)
   - Shows how to work with multi-dimensional arrays

3. 3D Array Splitting
   - Demonstrates depth splitting (dsplit)
   - Useful for working with 3D data like images

4. Advanced Splitting
   - Splitting at specific indices
   - More control over split locations

Each splitting method is useful for different data manipulation scenarios
in data analysis and processing tasks.
"""