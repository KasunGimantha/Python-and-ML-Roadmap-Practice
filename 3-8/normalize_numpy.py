import numpy as np


def normalize_array(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm
    return matrix


array = np.arange(16)-2

matrix = np.arange(16)-2

matrix = array.reshape(4, 4)
print("Simple Matrix \n", matrix)
normalized_matrix = normalize_array(matrix)
print("\nSimple Matrix \n", normalized_matrix)
