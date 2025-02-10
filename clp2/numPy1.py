# Generate a 5x5 matrix of random integers and compute row-wise sums.
import numpy as np
arr = np.random.randint(100, size=(5, 5))
sums = np.sum(arr, axis=1)
print(arr)
print("Row-wise sums:", sums)
