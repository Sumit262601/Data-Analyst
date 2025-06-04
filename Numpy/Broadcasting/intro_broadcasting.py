"""
NumPy Broadcasting Introduction

Broadcasting is a powerful mechanism in NumPy that allows arrays with different shapes 
to be used in arithmetic operations. It enables efficient array operations without 
explicitly replicating data.

Key Broadcasting Rules:
1. Arrays must have the same number of dimensions, or
2. One array can have fewer dimensions which will be "broadcast" to match
3. The size of each dimension must be:
   - Equal, or
   - One of the arrays has size 1 in that dimension, or
   - One array doesn't have that dimension at all

Common Broadcasting Scenarios:
- Scalar operations with arrays
- Operations between arrays of different shapes
- Vector operations with matrices
"""

import numpy as np

# 1. Basic Broadcasting with Scalar
print("1. Broadcasting with Scalar:")
arr = np.array([1, 2, 3, 4])
scalar = 2
result = arr * scalar
print(f"Array: {arr}")
print(f"Result after multiplying by {scalar}: {result}")

# 2. Broadcasting with Different Shaped Arrays
print("\n2. Broadcasting Different Shapes:")
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # Shape: (2, 3)

b = np.array([10, 20, 30])  # Shape: (3,)
result = a + b
print("Array a (2x3):")
print(a)
print("\nArray b (1x3):")
print(b)
print("\nResult after addition:")
print(result)

# 3. Broadcasting in Matrix Operations
print("\n3. Matrix Operations:")
matrix = np.array([[1, 2, 3],
                  [4, 5, 6]]) # Shape: (2, 3)

vector = np.array([1, 0, 1])  # Shape: (3,)
result = matrix * vector
print("Matrix:")
print(matrix)
print("\nVector:")
print(vector)
print("\nResult after multiplication:")
print(result)

# 4. More Complex Broadcasting Example
print("\n4. Complex Broadcasting:")
a = np.zeros((2, 3, 4))
print(a)
b = np.zeros((3, 4))
print(b)
c = np.zeros((4,))
print(c)
print(f"Shapes: a:{a.shape}, b:{b.shape}, c:{c.shape}")
print("All these operations are valid due to broadcasting:")
print("a + b -> shape:", (a + b).shape)
print("a + c -> shape:", (a + c).shape)

# 5. Broadcasting Limitations Example
print("\n5. Broadcasting Limitations:")
try:
    x = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
    y = np.array([1, 2, 3])         # Shape: (3,)
    result = x + y
except ValueError as e:
    print("Error demonstrating incompatible shapes:")
    print(e)

"""
Key Points to Remember:

1. Broadcasting Rules
   - Arrays must be compatible in all dimensions
   - Smaller arrays are "stretched" to match larger ones
   - No data copying occurs during broadcasting

2. Common Use Cases
   - Scalar operations with arrays
   - Vector operations with matrices
   - Operations between arrays of different ranks

3. Benefits
   - Memory efficient (no need to copy data)
   - Computationally efficient
   - Cleaner, more readable code

4. Limitations
   - Not all shape combinations can be broadcast
   - Need to understand rules to avoid errors
"""