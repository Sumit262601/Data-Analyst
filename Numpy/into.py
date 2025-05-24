'''
NumPy Introduction
NumPy (Numerical Python) is a fundamental Python library for numerical and scientific computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

NumPy is widely used in data science, machine learning, and scientific computing due to its efficiency and ease of use. It is the foundation for many other libraries in the Python ecosystem, such as SciPy, Pandas, and Matplotlib.

NumPy is designed for performance and efficiency, making it suitable for handling large datasets and complex mathematical operations. It provides a powerful N-dimensional array object, which allows for efficient storage and manipulation of data.
'''

import numpy as np

# Create a simple array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Create array with zeros and ones
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
print("\nZeros:\n", zeros)
print("\nOnes:\n", ones)

# Basic operations
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)
print("Add 2 to each element:", arr + 2)
print("Multiply each element by 3:", arr * 3)

# Reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print("Original array:", arr)
print("\nReshaped array (2x3):\n", reshaped)

# Array mathematics
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nArray addition:", arr1 + arr2)
print("Array multiplication:", arr1 * arr2)

# Statistical operations
data = np.array([14, 23, 32, 41, 50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard deviation:", np.std(data))