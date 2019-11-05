import numpy as np
from numpy.linalg import eigh as eigh
from numpy.linalg import norm as norm
from numpy.linalg import solve as solve

x = np.zeros(shape=(3, 1))
x[-1] = 1

A = np.asarray([[6, 2, 1], [2, 3, 1], [1, 1, 1]])

mu = 2

for i in range(100):
	y = solve(A-(mu*np.eye(3)), x)
	x = y/norm(y)

print('Calculated Eigenvalue:', 1/norm(y)+mu)
print('Calculated Eigenvector:', x.T[0])
v, w = eigh(A)
print('Actual Eigenvalue:', v[1])
print('Actual Eigenvector:', w[:,1])
