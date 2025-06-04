"""
Understanding isinf() in Python
The isinf() method is used to detect infinite values in numerical data. It's available in multiple Python libraries with slightly different implementations.

Key Implementations
    NumPy's isinf()
    Math module's isinf()
    Pandas' implementation via isfinite()
"""

import numpy as np
import math
import pandas as pd

# Create sample data with infinite values
arr = np.array([1, np.inf, -np.inf, 2, float('inf')])
print("Original array:", arr)

# 1. NumPy Implementation
print("\nNumPy isinf:")
print("Infinite values detected:", np.isinf(arr))
print("Number of infinite values:", np.isinf(arr).sum())
print("Positive infinite values:", np.isposinf(arr))
print("Negative infinite values:", np.isneginf(arr))

# 2. Math Module Implementation
print("\nMath module isinf:")
x = float('inf')
y = float('-inf')
print(f"Is {x} infinite?:", math.isinf(x))
print(f"Is {y} infinite?:", math.isinf(y))

# 3. Pandas Implementation
df = pd.DataFrame({
    'A': [1, np.inf, -np.inf, 4],
    'B': [np.inf, 5, 6, -np.inf]
})
print("\nPandas DataFrame:")
print(df)
print("\nInfinite values detected:")
print(np.isinf(df))

# Practical example: Handling infinite values
def clean_infinite(data):
    """Replace infinite values with NaN"""
    return np.where(np.isinf(data), np.nan, data)

cleaned_arr = clean_infinite(arr)
print("\nCleaned array (inf → NaN):", cleaned_arr)

# Additional replacement methods
print("\nReplacement Methods:")

# 1. Using np.nan_to_num
arr_finite = np.nan_to_num(arr, posinf=999, neginf=-999)
print("Replace with custom values:", arr_finite)

# 2. Using masked arrays
masked_arr = np.ma.masked_invalid(arr)
print("Masked array:", masked_arr)

# 3. Using pandas replace
df_clean = df.replace([np.inf, -np.inf], [999, -999])
print("\nPandas replace method:")
print(df_clean)

# 4. Using clip method to set boundaries
arr_clipped = np.clip(arr, -1000, 1000)  # Replace inf with boundary values
print("\nClipped array:", arr_clipped)

# 5. Using custom replacement function
def replace_infinite_values(data, pos_value=1e6, neg_value=-1e6):
    """Replace infinite values with custom values"""
    data = np.array(data)
    data[np.isposinf(data)] = pos_value
    data[np.isneginf(data)] = neg_value
    return data

arr_custom = replace_infinite_values(arr)
print("\nCustom replacement:", arr_custom)


"""
Key Features
NumPy's implementation:

    Works with arrays
    Can detect positive and negative infinity separately
    Vectorized operations for efficiency
Math module's implementation:

    Works with single values
    Part of Python standard library
    Simpler interface
Common Use Cases:

    Data validation
    Numerical computations
    Error handling
    Data preprocessing
"""