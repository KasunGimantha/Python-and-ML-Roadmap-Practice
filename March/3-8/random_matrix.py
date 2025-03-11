import numpy as np

random_matrix = np.random.randint(100, size=(5, 5)) #create random matrix
print(random_matrix) #

filter_arr = random_matrix > 50 #filtering


random_matrix[filter_arr] = 0 #assigning 0 to filtered indexes
print(random_matrix) #printing final array
