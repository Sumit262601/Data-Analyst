"""
Python Vectorization Introduction

Vectorization is the process of converting loop-based operations into vector operations.
It significantly improves performance by:
1. Eliminating loops
2. Using optimized array operations
3. Reducing overhead of Python interpreter

Benefits of Vectorization:
- Faster execution
- Cleaner code
- Better memory efficiency
- Parallel processing capabilities
"""

import numpy as np
import time

# 1. Compare Loop vs Vectorized Operations
print("1. Loop vs Vectorized Operations")

# Create large arrays for testing
size = 1000000
arr1 = np.random.rand(size)
arr2 = np.random.rand(size)

# Using loop
def loop_addition(a, b):
    result = np.zeros_like(a)
    for i in range(len(a)):
        result[i] = a[i] + b[i]
    return result

# Using vectorization
def vector_addition(a, b):
    return a + b

# Time comparison
print("\nTime Comparison for Addition:")
# Loop timing
start = time.time()
loop_result = loop_addition(arr1, arr2)
loop_time = time.time() - start
print(f"Loop time: {loop_time:.6f} seconds")

# Vectorized timing
start = time.time()
vector_result = vector_addition(arr1, arr2)
vector_time = time.time() - start
print(f"Vectorized time: {vector_time:.6f} seconds")
print(f"Speedup: {loop_time/vector_time:.2f}x")

# 2. Mathematical Operations
print("\n2. Mathematical Operations")
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
print("Square:", arr**2)
print("Square root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))

# 3. Conditional Operations
print("\n3. Conditional Operations")
# Traditional way with loop
def loop_conditional(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        if arr[i] > 3:
            result[i] = 1
    return result

# Vectorized way
def vector_conditional(arr):
    return np.where(arr > 3, 1, 0)

print("Conditional results:")
print("Original array:", arr)
print("Vector conditional:", vector_conditional(arr))
print("Loop conditional:", loop_conditional(arr))

# 4. Complex Operations
print("\n4. Complex Operations")
# Generate sample data
x = np.linspace(0, 10, 1000)
y = np.sin(x) + np.random.normal(0, 0.1, x.shape)

# Compute moving average
window_size = 50
def moving_average(data, window):
    return np.convolve(data, np.ones(window)/window, mode='valid')  

smooth_y = moving_average(y, window_size)
print(f"Original data shape: {y.shape}")
print(f"Smoothed data shape: {smooth_y.shape}")

"""
Key Vectorization Best Practices:

1. Use NumPy's Universal Functions (ufuncs)
   - Built-in operations are optimized
   - Support broadcasting
   - Thread-safe and memory efficient

2. Avoid Loops When Possible
   - Replace Python loops with vector operations
   - Use array operations instead of element-wise operations

3. Use Appropriate Data Types
   - Choose correct dtype for arrays
   - Avoid unnecessary type conversions

4. Common Vectorized Operations
   - Mathematical operations (add, multiply, power, etc.)
   - Statistical operations (mean, std, var)
   - Linear algebra operations
   - Boolean operations and masking
"""