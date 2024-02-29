import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])

# Convert 1D array to a row vector (2D array)
row_vector = arr[np.newaxis, :]
print("Row vector shape:", row_vector.shape)  # Output: (1, 5)

# Convert 1D array to a column vector (2D array)
column_vector = arr[:, np.newaxis]
print("Column vector shape:", column_vector)  # Output: (5, 1)
