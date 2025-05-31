"""Flatten and Ravel in Python NumPy
Definition
    Flatten: Creates a new 1D array that contains a copy of the elements in the original array
    Ravel: Returns a 1D array containing the elements of the input array, typically returns a view of the original array when possible
    flatten() vs ravel():
        flatten() creates a new array, while ravel() returns a flattened view of the original array if possible

        flatten() always returns a copy, while ravel() may return a view (which is more memory efficient)

        flatten() is useful when you need a separate copy of the data, while ravel() is preferred for memory efficiency
Key Differences
    Memory Usage:

        flatten() creates a new array in memory
        ravel() returns a view when possible, more memory efficient
        
    Modification Effects:

        Changes to flattened array don't affect original
        Changes to raveled array may affect original
"""

# Example Usage
import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])



# Using flatten()
flat_arr = arr.flatten()
print("Flattened array:", flat_arr)  # [1 2 3 4 5 6]

flat_arr = np.append(flat_arr, [7, 8, 9])
print(flat_arr.reshape(3,3))

# Using ravel()
ravel_arr = arr.ravel()
print("Raveled array:", ravel_arr)   # [1 2 3 4 5 6]

# Demonstrating the difference
ravel_arr[0] = 99  # This may modify original array
flat_arr[0] = 88   # This won't modify original array
# print(ravel_arr)

print("Original array after modifications:", arr)
print("Flattened array:", flat_arr)
print("Raveled array:", ravel_arr)


# Advanced Usage

# Different order options
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Row-major (C-style) ordering
print("C-style flatten:", arr.flatten('C'))

# Column-major (Fortran-style) ordering
print("F-style flatten:", arr.flatten('F'))

# Memory layout optimization
print("Memory optimized:", arr.flatten('K'))

# 'A': preserve input order
print("Preserve input order:", arr.flatten('A'))

"""Interview Questions
Q: What's the main difference between flatten() and ravel()?

    A: flatten() creates a new array copy, while ravel() returns a view when possible
Q: When should you use flatten() over ravel()?

    A: Use flatten() when you need a copy and don't want modifications to affect the original array
Q: What are the order parameters in flatten/ravel?

    A:
        'C' (default): row-major order
        'F': column-major order
        'A': preserve input order
        'K': match memory layout

Best Practices
    Use ravel() when memory efficiency is important
    Use flatten() when you need a separate copy
    Consider memory layout ('C' vs 'F') for performance
    Check array contiguity before operations

Common Use Cases
    Data preprocessing in machine learning
    Converting multi-dimensional data to 1D
    Feature engineering
    Matrix operations

Performance Tips
    Use ravel() for better performance when possible
    Consider memory layout for large arrays
    Use appropriate order parameter based on original array layout
    Avoid unnecessary copies with flatten()
    
Remember: Always consider memory implications when choosing between flatten() and ravel(), especially for large datasets."""