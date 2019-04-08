import numpy as np

# UoI Lasso functional graphs are often missing the (zero-valued) diagonal elements
# Expand the matrix to be square by inserting zeros along the diagonal
def fix_adjacency_matrix(arr):
	major_dim = np.argmax(arr.shape)
	major_size = np.max(arr.shape)
	minor_size = np.min(arr.shape)

	fixed_arr = np.zeros((major_size, major_size))

	for i in range(major_size):
		# Select the rows (columns) corresponding to the ith column (row) and 
		# insert a 0 at the ith index
		vec = np.take(arr, i, axis = major_dim)

		# Insert zeros
		vec = np.insert(vec, i, 0)
		fixed_arr[i, :] = vec

	return fixed_arr