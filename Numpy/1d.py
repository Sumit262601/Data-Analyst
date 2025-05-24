"""
One-Dimensional Arrays in NumPy
A one-dimensional array (1D array) in NumPy is the simplest form of an array that represents a sequence of elements arranged in a single line. It's similar to a Python list but offers more efficient operations and functionality.
"""

import numpy as np

# Creating 1D arrays
arr1 = np.array([1, 2, 3, 4, 5])               # From list
arr2 = np.arange(0, 10, 2)                     # Using arange (start, stop, step)
arr3 = np.linspace(0, 1, 5)                    # Create array with evenly spaced numbers

print("Basic array:", arr1)
print("Using arange:", arr2)
print("Using linspace:", arr3)

# Array operations
print("\nBasic Operations:")
print("Addition:", arr1 + 2)                    # Add 2 to each element
print("Multiplication:", arr1 * 3)              # Multiply each element by 3
print("Square:", arr1 ** 2)                     # Square each element

# Array indexing and slicing
print("\nIndexing and Slicing:")
print("First element:", arr1[0])                # Access first element
print("Last element:", arr1[-1])                # Access last element
print("Slice (1:4):", arr1[1:4])                # Slice array

# Array attributes
print("\nArray Information:")
print("Shape:", arr1.shape)                         # Array dimensions
print("Size:", arr1.size)                           # Number of elements
print("Data type:", arr1.dtype)                     # Data type of elements
print("Reshape (5,1):", arr1.reshape(5, 1))         # Reshape to 2D (5 rows, 1 column)
print("Flattened:", arr1.reshape(5, 1).flatten())   # Flatten to 1D


# Statistical operations
print("Variance:", np.var(arr1))                    # Variance
print("Median:", np.median(arr1))                   # Median
print("Cumulative Sum:", np.cumsum(arr1))           # Cumulative sum
print("Cumulative Product:", np.cumprod(arr1))      # Cumulative product
print("Dot Product:", np.dot(arr1, arr1))           # Dot product with itself

# Mathematical functions
print("\nMathematical Functions:")
print("Square:", np.square(arr1))                   # Square of each element
print("Exponential:", np.exp(arr1))                 # Exponential of each element
print("Logarithm:", np.log(arr1))                   # Natural logarithm of each element
print("Logarithm base 10:", np.log10(arr1))         # Logarithm base 10 of each element
print("Absolute:", np.abs(arr1))                    # Absolute value of each element
print("Sin:", np.sin(arr1))                         # Sine of each element
print("Cosine:", np.cos(arr1))                      # Cosine of each element
print("Tangent:", np.tan(arr1))                     # Tangent of each element
print("Floor:", np.floor(arr1))                     # Floor value of each element
print("Ceil:", np.ceil(arr1))                       # Ceiling value of each element
print("Rounding:", np.round(arr1))                  # Round each element
print("Sum:", np.sum(arr1))                         # Sum of all elements
print("Product:", np.prod(arr1))                    # Product of all elements
print("Max:", np.max(arr1))                         # Maximum value
print("Min:", np.min(arr1))                         # Minimum value
print("Sum:", np.sum(arr1))                         # Sum of elements
print("Mean:", np.mean(arr1))                       # Average
print("Standard Deviation:", np.std(arr1))          # Standard deviation
print("Square Root:", np.sqrt(arr1))                # Square root of each element

# Sorting and searching
print("\nSorting and Searching:")
arr4 = np.array([5, 2, 9, 1, 5, 6])
print("Unsorted array:", arr4)
print("Sorted array:", np.sort(arr4))
print("Search (5):", np.where(arr4 == 5))

# Broadcasting
print("\nBroadcasting:")
arr5 = np.array([1, 2, 3])
arr6 = np.array([10, 20, 30])
print("Array 1:", arr5)
print("Array 2:", arr6)

# Broadcasting example
print("Broadcasting (Array 1 + 10):", arr5 + 10)
print("Broadcasting (Array 1 + Array 2):", arr5 + arr6)

"""
Key points about 1D arrays:

Creation:
Using np.array() with a list
Using np.arange() for sequential numbers
Using np.linspace() for evenly spaced numbers

Operations:
Element-wise arithmetic operations
Mathematical functions
Broadcasting with scalars

Indexing:
Zero-based indexing
Negative indexing (from end)
Slicing with start:stop:step

Attributes:
shape: Returns dimensions
size: Number of elements
dtype: Data type of elements

Common Functions:
Statistical operations (mean, sum, std)
Mathematical operations (min, max, sqrt)
Sorting and searching
1D arrays are fundamental building blocks for more complex array operations in NumPy and are widely used in data analysis and scientific computing.
"""