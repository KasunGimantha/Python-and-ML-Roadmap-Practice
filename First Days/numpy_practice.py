#input:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("first", arr[0])
print("last", arr[:-1])
print("middle", arr[3])
print("only first 3 elements", arr[:3])

arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
row_index = 1
print("only second row", arr2[row_index])

print("only last column", arr2[:, -1])

#output:
first 1
last [1 2 3 4]
middle 4      
only first 3 elements [1 2 3]
only second row [5 6 7 8]
only last column [ 4  8 12]