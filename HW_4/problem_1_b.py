import numpy as np
from numpy.linalg import eig as eig
from numpy.linalg import norm as norm
from numpy.linalg import solve

x = np.zeros(shape=(3, 1))
x[-1] = 1

A = np.asarray([[2, 3, 2], [10, 3, 4], [3, 6, 1]])

for i in range(100):
	y = solve(A, x)
	x = y/norm(y)
	
print('Calculated Eigenvalue:', 1/norm(y))
print('Calculated Eigenvector:', x.T[0])
v, w = eig(A)
print('Actual Eigenvalue:', np.abs(v[1]))
print('Actual Eigenvector:', w[:,1])