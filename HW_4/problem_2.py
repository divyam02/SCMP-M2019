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
#########################################################################
#							Observations								#
#########################################################################
# Calculated Eigenvalue: 2.133074475348525
# Calculated Eigenvector: -0.49742503  0.8195891   0.28432735
# Actual Eigenvalue: 2.1330744753485256
# Actual Eigenvector: -0.49742503  0.8195891   0.28432735
# 
# We calculate 1/|lambda| and the negative eigenvector is not considered.