# NumPy Essential Guide

## Introduction
NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a vast collection of mathematical functions to operate on these arrays efficiently.

## Core Concepts

### 1. Arrays
Arrays are the core building block of NumPy - they are grid of values, all of the same type.

Examples:
```python
import numpy as np

# 1D Array
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D Array (Matrix)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
```

### 2. Array Operations
Basic mathematical operations are performed element-wise.

Examples:
```python
# Addition
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2  # [5, 7, 9]

# Multiplication
mult_arr = arr1 * 2  # [2, 4, 6]

# Matrix multiplication
mat_mult = np.dot(arr1, arr2)  # 32
```

### 3. Array Indexing and Slicing
Accessing array elements using indices and slices.

Examples:
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Single element
element = arr[0, 0]  # 1

# Row
row = arr[1, :]  # [4, 5, 6]

# Column
col = arr[:, 1]  # [2, 5, 8]
```

## Common Interview Questions & Answers

1. **Q: What is the difference between a Python list and NumPy array?**
   - A: NumPy arrays are homogeneous (same data type), more memory efficient, and support vectorized operations. Lists are heterogeneous and more flexible but slower for numerical computations.

2. **Q: Explain broadcasting in NumPy.**
   - A: Broadcasting is the ability of NumPy to perform operations on arrays of different shapes. The smaller array is "broadcast" to match the shape of the larger array.

3. **Q: How to find the memory size of a NumPy array?**
   - A: Use `array.nbytes` to get the total bytes consumed by the array's elements.

4. **Q: What is the difference between np.zeros() and np.empty()?**
   - A: `np.zeros()` creates an array filled with zeros, while `np.empty()` creates an array with uninitialized memory (faster but contains random values).

## Practice Questions (Try These!)

1. Create a function that finds the second largest element in a 2D array without using sort.

2. Write code to replace all odd numbers in an array with -1 without using loops.

3. Given two arrays, find common elements considering duplicates.

4. Create a function to rotate a matrix 90 degrees clockwise without using additional memory.

5. Write a function to find the peaks (elements greater than their neighbors) in a 1D array.

## Advanced Topics for Practice

### Array Manipulation
```python
# Reshape arrays
# Stack arrays
# Split arrays
# Roll and shift arrays
```

### Linear Algebra
```python
# Matrix operations
# Eigenvalues and eigenvectors
# Matrix decomposition
```

### Statistical Functions
```python
# Mean, median, mode
# Standard deviation
# Correlation and covariance
```

## Performance Tips
1. Use vectorized operations instead of loops
2. Understand memory layout (row-major vs column-major)
3. Use appropriate data types
4. Avoid unnecessary copies
5. Use built-in NumPy functions when possible

## Common Pitfalls
1. Mixing data types unexpectedly
2. Not understanding broadcasting rules
3. Memory issues with large arrays
4. Incorrect axis specifications
5. View vs Copy confusion

## Debugging Tips
1. Use `array.shape` to verify dimensions
2. Print `array.dtype` to check data types
3. Use `np.info()` for function documentation
4. Check memory usage with `array.nbytes`
5. Use `np.shares_memory()` to check array views