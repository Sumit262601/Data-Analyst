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

---

## All Major Methods and Features in NumPy

### Array Creation
- `np.array()`, `np.asarray()`
- `np.zeros()`, `np.ones()`, `np.full()`, `np.empty()`
- `np.arange()`, `np.linspace()`, `np.logspace()`
- `np.eye()`, `np.identity()`, `np.diag()`
- `np.fromfunction()`, `np.fromiter()`, `np.frombuffer()`

### Array Attributes
- `ndarray.shape`, `ndarray.ndim`, `ndarray.size`, `ndarray.dtype`, `ndarray.itemsize`, `ndarray.nbytes`, `ndarray.T` (transpose), `ndarray.strides`, `ndarray.flags`

### Array Manipulation
- Reshape: `reshape()`, `ravel()`, `flatten()`, `resize()`
- Transpose: `transpose()`, `swapaxes()`, `moveaxis()`
- Stacking: `vstack()`, `hstack()`, `dstack()`, `column_stack()`, `row_stack()`
- Splitting: `split()`, `hsplit()`, `vsplit()`, `dsplit()`
- Repeat & Tile: `repeat()`, `tile()`
- Broadcasting: automatic with compatible shapes

### Indexing, Slicing, and Iterating
- Basic, advanced, boolean, and fancy indexing
- `np.where()`, `np.nonzero()`, `np.argwhere()`
- `np.take()`, `np.put()`, `np.choose()`
- Iteration: `nditer()`, `ndenumerate()`, `ndindex()`

### Universal Functions (ufuncs)
- Arithmetic: `add()`, `subtract()`, `multiply()`, `divide()`, `power()`, `mod()`
- Trigonometric: `sin()`, `cos()`, `tan()`, `arcsin()`, `arccos()`, `arctan()`
- Exponential & Logarithmic: `exp()`, `log()`, `log10()`, `log2()`
- Rounding: `round()`, `floor()`, `ceil()`, `trunc()`
- Aggregation: `sum()`, `prod()`, `mean()`, `std()`, `var()`, `min()`, `max()`, `argmin()`, `argmax()`, `median()`, `percentile()`, `cumsum()`, `cumprod()`

### Linear Algebra
- `dot()`, `vdot()`, `inner()`, `outer()`, `matmul()`
- `linalg.inv()`, `linalg.pinv()`, `linalg.det()`, `linalg.matrix_rank()`
- `linalg.eig()`, `linalg.eigh()`, `linalg.eigvals()`
- `linalg.svd()`, `linalg.qr()`, `linalg.cholesky()`, `linalg.lstsq()`
- `linalg.solve()`, `linalg.norm()`, `linalg.trace()`

### Random Module
- `random.rand()`, `random.randn()`, `random.randint()`, `random.choice()`, `random.shuffle()`, `random.permutation()`
- `random.seed()`, `random.uniform()`, `random.normal()`, `random.binomial()`, `random.beta()`, `random.gamma()`, `random.poisson()`

### Statistics
- `mean()`, `median()`, `std()`, `var()`, `ptp()`, `percentile()`, `quantile()`, `corrcoef()`, `cov()`, `histogram()`, `bincount()`

### Set Operations
- `unique()`, `intersect1d()`, `union1d()`, `setdiff1d()`, `setxor1d()`, `in1d()`, `isin()`

### Sorting, Searching, and Counting
- `sort()`, `argsort()`, `lexsort()`, `searchsorted()`, `argmax()`, `argmin()`, `count_nonzero()`

### File I/O
- `loadtxt()`, `genfromtxt()`, `savetxt()`
- `save()`, `savez()`, `savez_compressed()`, `load()`
- `fromfile()`, `tofile()`

### Masked Arrays
- `np.ma.masked_array()`, `np.ma.masked_where()`, `np.ma.masked_equal()`, `np.ma.masked_greater()`, `np.ma.filled()`

### Structured Arrays & Record Arrays
- Custom dtypes, `np.recarray()`, field access

### Memory Management
- `np.copy()`, `np.view()`, `np.shares_memory()`, `np.may_share_memory()`

### Miscellaneous
- `np.clip()`, `np.round()`, `np.isnan()`, `np.isinf()`, `np.isfinite()`
- `np.vectorize()`, `np.apply_along_axis()`, `np.apply_over_axes()`
- `np.broadcast()`, `np.broadcast_to()`, `np.broadcast_arrays()`
- `np.meshgrid()`, `np.mgrid`, `np.ogrid`
- `np.diff()`, `np.gradient()`, `np.ediff1d()`
- `np.pad()`, `np.roll()`, `np.flip()`, `np.rot90()`
- `np.triu()`, `np.tril()`, `np.diagflat()`
- `np.select()`, `np.piecewise()`
- `np.array_split()`, `np.hsplit()`, `np.vsplit()`, `np.dsplit()`
- `np.cumsum()`, `np.cumprod()`
- `np.resize()`, `np.append()`, `np.insert()`, `np.delete()`

---

## Common Interview Questions & Answers

1. **Q: What is the difference between a Python list and NumPy array?**
   - A: NumPy arrays are homogeneous (same data type), more memory efficient, and support vectorized operations. Lists are heterogeneous and more flexible but slower for numerical computations.

2. **Q: Explain broadcasting in NumPy.**
   - A: Broadcasting is the ability of NumPy to perform operations on arrays of different shapes. The smaller array is "broadcast" to match the shape of the larger array.

3. **Q: How to find the memory size of a NumPy array?**
   - A: Use `array.nbytes` to get the total bytes consumed by the array's elements.

4. **Q: What is the difference between np.zeros() and np.empty()?**
   - A: `np.zeros()` creates an array filled with zeros, while `np.empty()` creates an array with uninitialized memory (faster but contains random values).

---

## Practice Questions (Try These!)

1. Create a function that finds the second largest element in a 2D array without using sort.

2. Write code to replace all odd numbers in an array with -1 without using loops.

3. Given two arrays, find common elements considering duplicates.

4. Create a function to rotate a matrix 90 degrees clockwise without using additional memory.

5. Write a function to find the peaks (elements greater than their neighbors) in a 1D array.

---

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

---

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

# NumPy Complete Topics Index

## 1. Array Basics
- Creating Arrays
  - np.array()
  - np.zeros()
  - np.ones()
  - np.empty()
  - np.arange()
  - np.linspace()
  
## 2. Array Operations
- Basic Operations
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Universal Functions (ufunc)
  - np.sum()
  - np.mean()
  - np.max()
  - np.min()

## 3. Array Indexing & Slicing
- Basic Indexing
- Boolean Indexing
- Fancy Indexing
- Array Slicing
- Index Tricks

## 4. Array Shape Manipulation
- Reshaping Arrays
- Stacking Arrays
  - np.vstack()
  - np.hstack()
  - np.concatenate()
- Splitting Arrays
  - np.split()
  - np.vsplit()
  - np.hsplit()

## 5. Linear Algebra
- Matrix Operations
  - Matrix Multiplication
  - Transpose
  - Inverse
- Eigenvalues & Eigenvectors
- Matrix Decomposition
  - LU Decomposition
  - QR Decomposition
  - SVD

## 6. Statistics
- Descriptive Statistics
  - Mean
  - Median
  - Standard Deviation
  - Variance
- Correlation & Covariance
- Histograms
- Random Number Generation

## 7. File Operations
- Loading Data
  - np.loadtxt()
  - np.genfromtxt()
- Saving Data
  - np.save()
  - np.savez()
  - np.savetxt()

## 8. Advanced Topics
- Broadcasting
- Structured Arrays
- Memory Management
- Performance Optimization
- Vectorization

## 9. Integration with Other Libraries
- Pandas Integration
- Matplotlib Integration
- SciPy Integration

## 10. Data Processing
- Data Cleaning
- Missing Values
- Data Transformation
- Data Normalization

## 11. Mathematical Functions
- Trigonometric Functions
- Exponential & Logarithmic
- Rounding Functions
- Complex Numbers

## 12. Array Iteration
- np.nditer()
- Broadcasting Iterator
- Buffer Iterator

## 13. Set Operations
- np.unique()
- np.intersect1d()
- np.union1d()
- np.setdiff1d()

## 14. Sorting & Searching
- np.sort()
- np.argsort()
- np.searchsorted()
- np.argmax()/argmin()

## 15. Binary Operations
- Bitwise Operations
- Comparison Operations
- Logical Operations

## Quick Reference Links
1. [Official NumPy Documentation](https://numpy.org/doc/)
2. [NumPy User Guide](https://numpy.org/doc/stable/user/)
3. [NumPy Reference](https://numpy.org/doc/stable/reference/)

## Code Examples Repository Structure
```
numpy/
├── basics/
│   ├── array_creation.py
│   ├── array_operations.py
│   └── indexing_slicing.py
├── advanced/
│   ├── broadcasting.py
│   ├── vectorization.py
│   └── memory_management.py
├── math/
│   ├── linear_algebra.py
│   ├── statistics.py
│   └── mathematical_functions.py
└── data_processing/
    ├── file_operations.py
    ├── data_cleaning.py
    └── data_transformation.py
```

Each topic contains:
1. Theory explanation
2. Basic examples
3. Advanced use cases
4. Common pitfalls
5. Best practices
6. Performance considerations