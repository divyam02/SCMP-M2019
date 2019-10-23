import numpy as np
from numpy.linalg import solve as solve
from numpy.linalg import norm as norm

def gen_hilbert_matrix(n):
	temp = np.ones(shape=(n, n))
	for i in range(n):
		for j in range(n):
			temp[i, j] = 1/(i+j+1) 
			# Change hilbert matrix entry because of zero indexing.

			temp[j, i] = np.copy(temp[i, j])

	return temp

n = 2
while True:
	x_true = np.ones(shape=(1, n)).T
	H = gen_hilbert_matrix(n)
	b = np.dot(H, x_true)
	x_approx = solve(H, b)
	# print(x_approx.shape)
	r = b - np.dot(H, x_approx)
	# print(r.shape)
	x_diff = x_approx - x_true
	# print(x_diff.shape)
	residual_error = norm(r.T, np.inf)
	absolute_error = norm(x_diff.T, np.inf)

	# print("residual_error", residual_error)
	# print("absolute_error", absolute_error)
	if n==100:
		break
	n+=1