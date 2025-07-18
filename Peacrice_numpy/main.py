import numpy as np

array_1 = np.array([1,2,3,4,5,6,7,8,9])
# print(array_1)

# Create a 3x3 NumPy array with all elements as True.
true_array = np.ones((3,3), dtype=bool)
print(true_array)

# Create an array of 10 random floats between 0 and 1.
random_array = np.random.rand(10)
print(random_array)

# Change the shape of a 1D array with 12 elements into a 3x4 matrix.
matrix = array_1.reshape(3,3)
print(matrix)

# Create an array of 5 elements all set to the same value (e.g., 7).
full_array = np.full(5, 7)
print(full_array)


# # Example: 3x3 matrix of random integers from 10 to 49
matrix = np.random.randint(10, 50, size=(3, 3))
print(matrix)