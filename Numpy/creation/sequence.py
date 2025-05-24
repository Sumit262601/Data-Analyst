# Sequence creation
# 8. Using the `np.eye()` function
# 7. Using the `np.ones()` function
# 4. Using the `np.full()` function
# 6. Using the `np.zeros()` function
# 5. Using the `np.empty()` function
# 1. Using the `np.arange()` function
# 2. Using the `np.linspace()` function
# 3. Using the `np.logspace()` function
# 9. Using the `np.fromfunction()` function
# 10. Using the `np.fromiter()` function
# 11. Using the `np.fromstring()` function
# 12. Using the `np.frombuffer()` function
# 13. Using the `np.fromfile()` function
# 14. Using the `np.frompyfunc()` function

import numpy as np

# 1. np.arange() - Creates an array with evenly spaced values within a given interval
print("\n1. arange() examples:")
print(np.arange(5))                     # [0 1 2 3 4]
print(np.arange(2, 10, 2))              # [2 4 6 8]
print(np.arange(0, 2, 0.3))             # [0.  0.3 0.6 0.9 1.2 1.5 1.8]

# 2. np.linspace() - Creates an array with evenly spaced numbers over a specified interval
print("\n2. linspace() examples:")
print(np.linspace(0, 1, 5))         # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, 4))        # [0. 3.33 6.67 10.]

# 3. np.logspace() - Creates an array with evenly spaced numbers on a log scale
print("\n3. logspace() examples:")
print(np.logspace(0, 2, 3))         # [1. 10. 100.]
print(np.logspace(0, 5, 4))         # [1. 100. 10000. 100000.]

# 4. np.full() - Creates a constant array
print("\n4. full() examples:")
print(np.full(5, 7))                # [7 7 7 7 7]
print(np.full((2, 2), 9))           # [[9 9]
                                    #  [9 9]]

# 5. np.empty() - Creates an uninitialized array
print("\n5. empty() examples:")
print(np.empty(3))                 # [random values]
print(np.empty((2, 2)))            # [[random values]]

# 6. np.zeros() - Creates an array filled with zeros
print("\n6. zeros() examples:")
print(np.zeros(5))                  # [0. 0. 0. 0. 0.]
print(np.zeros((2, 3)))            # [[0. 0. 0.]
                                   #  [0. 0. 0.]]

# 7. np.ones() - Creates an array filled with ones
print("\n7. ones() examples:")
print(np.ones(4))                   # [1. 1. 1. 1.]
print(np.ones((2, 2)))             # [[1. 1.]
                                   #  [1. 1.]]

# 8. np.eye() - Creates an identity matrix
print("\n8. eye() examples:")
print(np.eye(3))                    # [[1. 0. 0.]
                                   #  [0. 1. 0.]
                                   #  [0. 0. 1.]]
print(np.eye(2, 3))                # [[1. 0. 0.]
                                   #  [0. 1. 0.]]

# 9. np.fromfunction() - Creates an array by executing a function over each coordinate
print("\n9. fromfunction() examples:")
def f(x, y): return x + y
print(np.fromfunction(f, (3, 3)))   # Array where each element is sum of its indices

# 10. np.fromiter() - Create an array from an iterable object
print("\n10. fromiter() examples:")
iterable = range(5)
print(np.fromiter(iterable, dtype=float))  # [0. 1. 2. 3. 4.]

# 11. np.fromstring() - Create array from string
print("\n11. fromstring() examples:")
print(np.fromstring('1 2 3 4 5', dtype=int, sep=' '))  # [1 2 3 4 5]

# 12. np.frombuffer() - Create array from buffer object
print("\n12. frombuffer() examples:")
s = b'Hello World'
print(np.frombuffer(s, dtype='S1'))  # [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']

# 13. np.fromfile() - Create array from file
# Note: This requires a file to exist
# Example: np.fromfile('data.txt', dtype=float)

# 14. np.frompyfunc() - Create a NumPy universal function from a Python function
print("\n14. frompyfunc() examples:")
def cube(x): return x * x * x
cube_ufunc = np.frompyfunc(cube, 1, 1)
print(cube_ufunc([1, 2, 3, 4]))    # [1 8 27 64]