"""
NumPy Array Stacking Introduction
NumPy provides several methods for combining arrays by stacking them in different directions. Here are the key points about array stacking in NumPy:

Key Stacking Methods

Vertical Stacking (np.vstack)
    Stacks arrays along rows (first axis)
    Input arrays must have same shape along all but first axis
    Useful for adding new rows to data

Horizontal Stacking (np.hstack)
    Stacks arrays along columns (second axis)
    Arrays must have same shape along all but second axis
    Common for combining features in data analysis

Column Stacking (np.column_stack)
    Specifically for turning 1D arrays into columns
    Converts 1D arrays to 2D columns before stacking
    Popular in creating feature matrices

Depth Stacking (np.dstack)
    Stacks along third axis
    Creates 3D arrays from 1D/2D inputs
    Used in image processing and 3D data

Advanced Options

General Stack Function (np.stack)
    Most flexible stacking operation
    Allows specifying any axis
    Creates new axis for stacking

Concatenate Function (np.concatenate)
    Most versatile method
    Works along any existing axis
    No new axis is created
"""

import numpy as np

# Basic arrays for demonstration
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

# 1. Vertical Stacking (vstack)
print("1. Vertical Stacking:")
vertical_stack = np.vstack((arr1, arr2, arr3))
print(vertical_stack)
print("\nShape after vertical stacking:", vertical_stack.shape)

# 2. Horizontal Stacking (hstack)
print("\n2. Horizontal Stacking:")
horizontal_stack = np.hstack((arr1, arr2, arr3))
print(horizontal_stack)
print("\nShape after horizontal stacking:", horizontal_stack.shape)

# 3. Column Stacking (column_stack)
print("\n3. Column Stacking:")
column_stack = np.column_stack((arr1, arr2, arr3))
print(column_stack)
print("\nShape after column stacking:", column_stack.shape)

# 4. Depth Stacking (dstack)
print("\n4. Depth Stacking:")
depth_stack = np.dstack((arr1, arr2, arr3))
print(depth_stack)
print("\nShape after depth stacking:", depth_stack.shape)

# 5. Stack along specific axis (stack)
print("\n5. Stack along axis:")
axis_stack = np.stack((arr1, arr2, arr3), axis=0)  # Similar to vstack
print(axis_stack)
print("\nShape after axis stacking:", axis_stack.shape)

# 6. Practical Example with 2D arrays
print("\n6. Stacking 2D arrays:")
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("\nOriginal matrices:")
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)

print("\nVertical stacking 2D arrays:")
vertical_2d = np.vstack((matrix1, matrix2))
print(vertical_2d)

print("\nHorizontal stacking 2D arrays:")
horizontal_2d = np.hstack((matrix1, matrix2))
print(horizontal_2d)

# 7. Concatenate function (more flexible)
print("\n7. Using concatenate:")
concat_v = np.concatenate((matrix1, matrix2), axis=0)  # Vertical
concat_h = np.concatenate((matrix1, matrix2), axis=1)  # Horizontal

print("\nConcatenate vertical:\n", concat_v)
print("\nConcatenate horizontal:\n", concat_h)


"""
This code demonstrates different ways to stack arrays in NumPy:

Vertical Stacking (vstack)
    Stacks arrays vertically (along rows)
    Useful for combining arrays as new rows

Horizontal Stacking (hstack)
    Stacks arrays horizontally (along columns)
    Useful for adding new columns

Column Stacking (column_stack)
    Similar to hstack but treats 1D arrays as columns
    Converts 1D arrays into 2D columns

Depth Stacking (dstack)
    Stacks arrays along the third axis
    Creates 3D array from 1D or 2D inputs

Stack Function
    More general stacking operation
    Allows specifying axis explicitly

2D Array Stacking
    Shows how stacking works with matrices
    Demonstrates practical applications

Concatenate Function
    Most flexible stacking operation
    Can work along any axis

When you run this code, you'll see the different results of each stacking operation and their resulting shapes. This is particularly useful for data manipulation in data analysis and machine learning tasks.
"""