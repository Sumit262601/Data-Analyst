#creation identity matrices
#eye(size) creates an identity matrix of the given size
# Example: Creating a 3x3 identity matrix
# Importing the numpy library


import numpy as np

identity_matrix = np.eye()
print("Identity Matrix:", identity_matrix)

# Output:
# Identity Matrix: [[1. 0. 0. 0.]
#                   [0. 1. 0. 0.]
#                   [0. 0. 1. 0.]
#                   [0. 0. 0. 1.]]



# The np.eye() function creates a square matrix with ones on the diagonal and zeros elsewhere.
# The size of the matrix is specified by the argument passed to the function.
# The identity matrix is a special type of square matrix that has ones on the diagonal and zeros elsewhere.
# The identity matrix is useful in various mathematical operations, including matrix multiplication and solving systems of equations.
