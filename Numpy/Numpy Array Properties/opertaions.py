import numpy as np

# Common arrays used across examples
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("\n1. Shape Operations")
print("-" * 50)

# Shape tells us the structure of the array (rows, columns, dimensions)
print("1D array shape:", arr_1d.shape)     # (5,) - 5 elements
print("2D array shape:", arr_2d.shape)     # (2, 3) - 2 rows, 3 columns
print("3D array shape:", arr_3d.shape)     # (2, 2, 2) - 2 layers, 2 rows, 2 columns

print("\n2. Size Operations")
print("-" * 50)

# Size gives total number of elements in the array
print("1D array size:", arr_1d.size)       # 5 elements
print("2D array size:", arr_2d.size)       # 6 elements (2 × 3)
print("3D array size:", arr_3d.size)       # 8 elements (2 × 2 × 2)

print("\n3. Number of Dimensions (ndim)")
print("-" * 50)

# ndim tells us how many dimensions the array has
print("1D array dimensions:", arr_1d.ndim)  # 1 dimension (vector)
print("2D array dimensions:", arr_2d.ndim)  # 2 dimensions (matrix)
print("3D array dimensions:", arr_3d.ndim)  # 3 dimensions (tensor)

print("\n4. Data Type (dtype) Operations")
print("-" * 50)

# dtype shows the type of data stored in the array
print("Default data type:", arr_1d.dtype)

# Creating arrays with different data types
float_arr = np.array([1, 2, 3], dtype=np.float64)
bool_arr = np.array([True, False, True])
print("Float array dtype:", float_arr.dtype)
print("Boolean array dtype:", bool_arr.dtype)
print("Item size in bytes:", arr_2d.itemsize)
print("Total bytes used:", arr_2d.nbytes)

print("\n5. Type Conversion (astype)")
print("-" * 50)

# Converting between different data types
float_vals = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print("Original array:", float_vals)
print("To integer:", float_vals.astype(int))
print("To boolean:", float_vals.astype(bool))
print("To string:", float_vals.astype(str))

print("\n6. Mathematical Operations")
print("-" * 50)
math_arr = np.array([1, 2, 3, 4, 5])
# Basic arithmetic
print("Addition:", math_arr + 2)
print("Subtraction:", math_arr - 2)
print("Multiplication:", math_arr * 2)
print("Division:", math_arr / 2)

# Advanced mathematics
print("\nAdvanced Math:")
print("Square root:", np.sqrt(math_arr))
print("Exponentiation:", math_arr ** 2)
print("Natural log:", np.log(math_arr))

# Trigonometric functions
print("\nTrigonometry:")
print("Sine:", np.sin(math_arr))
print("Cosine:", np.cos(math_arr))
print("Tangent:", np.tan(math_arr))

# Rounding functions
print("\nRounding:")
print("Floor:", np.floor(math_arr))
print("Ceiling:", np.ceil(math_arr))
print("Round:", np.round(math_arr))
print("Absolute:", np.abs(math_arr))

print("\n7. Aggregation Functions")
print("-" * 50)
agg_arr = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
# Basic statistics
print("Sum:", np.sum(agg_arr))
print("Mean:", np.mean(agg_arr))
print("Median:", np.median(agg_arr))
print("Standard deviation:", np.std(agg_arr))
print("Variance:", np.var(agg_arr))

# Aggregation along axes
print("\nAxis-specific operations:")
print("Column sums (axis=0):", np.sum(agg_arr, axis=0))
print("Row sums (axis=1):", np.sum(agg_arr, axis=1))
print("Column means:", np.mean(agg_arr, axis=0))
print("Row means:", np.mean(agg_arr, axis=1))
print("Min value per column:", np.min(agg_arr, axis=0))
print("Max value per row:", np.max(agg_arr, axis=1))
