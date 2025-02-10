""" Create an array of 100 random values
    and normalize them between 0 and 1. """

import numpy as np
arr = np.random.randint(1000, size=100)
n_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
n_arr = np.round(n_arr, 2)
print("Original array:\n", arr)
print("Normalized array:\n", n_arr)

