"""
What is Fancy Indexing in Python?
Fancy indexing is a NumPy feature that allows you to index arrays using arrays of indices.
It enables selecting, modifying, and manipulating arrays in sophisticated ways using integer
arrays/lists as indices. This is particularly useful for complex data manipulation tasks.
"""

import numpy as np

# 1. Basic Fancy Indexing
print("\n--- Basic Fancy Indexing ---")
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print("Original array:", arr)
print("Selected elements:", arr[indices])  # Output: [10 30 50]
print("Using negative indices:", arr[[-1, -3]])  # Output: [50 30]

# 2. 2D Array Fancy Indexing
print("\n--- 2D Array Fancy Indexing ---")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Original matrix:\n", matrix)

# Selecting rows
row_indices = [0, 2]
print("\nSelected rows:\n", matrix[row_indices])

# Selecting specific elements
rows = [0, 1, 2]
cols = [0, 1, 0]
print("\nSelected elements using (rows, cols):", matrix[rows, cols])

# 3. Boolean Masking
print("\n--- Boolean Masking ---")
data = np.array([1, 2, 3, 4, 5, 6])
# Simple condition
mask = data > 3
print("Elements > 3:", data[mask])

# Complex conditions
complex_mask = (data > 2) & (data < 5)
print("Elements between 2 and 5:", data[complex_mask])

# 4. Modifying Values Using Fancy Indexing
print("\n--- Modifying Values ---")
arr = np.array([1, 2, 3, 4, 5])
print("Before modification:", arr)
arr[[0, 2, 4]] = 100
print("After modification:", arr)

# 5. Advanced Examples
print("\n--- Advanced Examples ---")
# Multiple dimensional boolean masking
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Values greater than 5 in matrix:", matrix[matrix > 5])

# Combining boolean masking with fancy indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mask = arr > 5
indices = [0, 1, 2]
print("Combined masking and indexing:", arr[mask][indices])

if __name__ == "__main__":
    # Run examples
    pass

"""
Common Interview Questions and Best Practices:

Q: What's the difference between fancy indexing and slicing?
A: Fancy indexing uses arrays of indices for non-sequential access, while slicing 
   uses start:stop:step for sequential access.

Q: Can fancy indexing be used with regular Python lists?
A: No, fancy indexing is a NumPy-specific feature. Regular Python lists don't support it.

Q: What happens if you use duplicate indices in fancy indexing?
A: The operation is performed multiple times on the same indices, which might lead 
   to unexpected results when modifying values.

Best Practices:
1. Always verify index bounds to avoid IndexError
2. Use boolean masking for filtering operations
3. Be cautious with duplicate indices in assignment operations
4. Consider memory usage when working with large arrays
5. Combine with regular indexing and slicing when appropriate
"""