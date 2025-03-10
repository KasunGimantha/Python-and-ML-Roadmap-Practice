import numpy as np

# declaring a 3X3 array
my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])


# modification 1
my_array[1, 0:2] = [35, 54]
print(my_array)

# modification 2
my_array[2, 1] = 90
print(my_array)
