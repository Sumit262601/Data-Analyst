"""
NumPy Reshaping: Basic to Advanced Guide

Introduction:
Reshaping in NumPy refers to changing the shape (dimensions) of an array without changing its data. This is crucial for data preprocessing, machine learning, image processing, and scientific computing.

Key Concepts:
- The new shape must contain the same total number of elements as the original.
- Reshaping is used for data restructuring, feature engineering, and batch processing.
- Methods include: reshape(), resize(), ravel(), flatten(), transpose(), swapaxes(), squeeze(), expand_dims(), stack(), hstack(), vstack().
- Use the -1 parameter for automatic dimension inference.
- Be aware of memory layout (C-contiguous vs. F-contiguous).
- Reshaping usually returns a view, not a copy (unless not possible).

Common Methods:
- reshape(): Returns a new array with the specified shape.
- resize(): Changes the shape in-place (can alter total elements).
- ravel(): Flattens the array to 1D (returns a view if possible).
- flatten(): Flattens to 1D (always returns a copy).
- transpose(): Permutes array axes.
- swapaxes(): Swaps two axes.
- squeeze(): Removes single-dimensional entries.
- expand_dims(): Adds a new axis.
- stack(), hstack(), vstack(): Combine arrays along new or existing axes.

NOTE: Reshaping changes the view of data in memory, not the data itself (unless a copy is required).

"""

# Basic Reshaping Example
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2x3 matrix
matrix = arr.reshape(2, 3)
print("Reshaped Matrix:\n", matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Using -1 in Reshape (automatic dimension calculation)
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped_auto = arr2.reshape(4, -1)  # NumPy infers columns
print("Reshaped with -1:\n", reshaped_auto)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Flattening arrays
flat1 = arr2.ravel()    # Returns a flattened view
flat2 = arr2.flatten()  # Returns a flattened copy
print("Ravel:", flat1)
print("Flatten:", flat2)

# Transpose and swapaxes
arr3 = np.arange(8).reshape(2, 2, 2)
print("Original shape:", arr3.shape)
print("Transposed shape:", arr3.transpose(1, 0, 2).shape)
print("Swapaxes shape:", np.swapaxes(arr3, 0, 2).shape)

# Squeeze and expand_dims
arr4 = np.array([[[1, 2, 3]]])
print("Squeezed shape:", np.squeeze(arr4).shape)
print("Expanded dims shape:", np.expand_dims(arr, axis=0).shape)

# Stacking examples
a = np.array([1, 2])
b = np.array([3, 4])
print("Stack:\n", np.stack((a, b)))
print("HStack:\n", np.hstack((a, b)))
print("VStack:\n", np.vstack((a, b)))

"""
Interview Questions

Q: What's the difference between reshape() and resize()?
A: reshape() returns a new array with the desired shape (original unchanged, view if possible). resize() changes the shape in-place and can change the total number of elements (fills with zeros if needed).

Q: Can you reshape an array of 10 elements into a 3x4 matrix?
A: No, because 3x4=12 elements, which does not match the original 10.

Q: What does reshape(-1, 1) do?
A: Converts a 1D array into a column vector (NumPy infers the number of rows).

Advanced Example
"""

# Create a 3D array
arr5 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

# Reshape to different dimensions
reshaped_1 = arr5.reshape(2, 2, 3)  # 2x2x3
reshaped_2 = arr5.reshape(-1)       # Flatten to 1D
reshaped_3 = arr5.reshape(4, 3)     # 4x3 matrix

print("\nOriginal shape:", arr5.shape)
print(arr5)
print("\nReshaped to 2x2x3:", reshaped_1.shape)
print(reshaped_1)
print("\nFlattened shape:", reshaped_2.shape)
print(reshaped_2)
print("\nReshaped to 4x3:", reshaped_3.shape)
print(reshaped_3)

"""
Common Use Cases
- Feature engineering in machine learning
- Image processing (reshaping pixel matrices)
- Time series data restructuring
- Batch processing in deep learning

Best Practices
- Always verify shape compatibility before reshaping
- Use -1 for flexible dimensions
- Use ravel() for flattening if a view is acceptable
- Check array contiguity with .flags['C_CONTIGUOUS']
- Prefer built-in NumPy methods for performance

This guide covers essential reshaping operations for effective data manipulation in NumPy.
"""

# Additional Example with resize()
arr = np.array([1, 2, 3, 4])
arr.resize((2, 3))
print(arr)
# Output:
# [[1 2 3]
#  [4 1 2]]