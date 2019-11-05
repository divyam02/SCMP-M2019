import numpy as np
from numpy.linalg import eigh as eigh
from numpy.linalg import norm as norm
from numpy.linalg import solve as solve

A = np.asarray([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
converge_steps = 0
for i in range(100):
	x = np.random.randn(3, 1)
	for i in range(100):
		try:
			mu = np.dot(x.T, np.dot(A, x))/np.dot(x.T, x)
			y = solve(A-(mu*np.eye(3)), x)
			x = y/norm(y)		

			converge_steps+=1
		except:
			# print(converge_steps)
			break

# print('Calculated Eigenvalue:', mu)
# print('Calculated Eigenvector:', x.T[0])
# v, w = eigh(A)
# print('Actual Eigenvalue:', v[1])
# print('Actual Eigenvector:', w[:,1].T)
print('Average convergence rate of Eigenvalue with arbitrary starting vectors:', converge_steps/100)

#########################################################################
#							Observations								#
#########################################################################	
# Average convergence rate of Eigenvalue with arbitrary starting vectors: 90.51