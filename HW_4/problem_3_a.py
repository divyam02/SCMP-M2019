import numpy as np
from numpy.linalg import eigh as eigh
from numpy.linalg import norm as norm
from numpy.linalg import solve as solve

x = np.zeros(shape=(3, 1))
x[-1] = 1

A = np.asarray([[6, 2, 1], [2, 3, 1], [1, 1, 1]])

converge_steps = 0
for i in range(100):
	try:
		mu = np.dot(x.T, np.dot(A, x))/np.dot(x.T, x)
		y = solve(A-(mu*np.eye(3)), x)
		x = y/norm(y)		

		converge_steps+=1
	except:
		break

print('Calculated Eigenvalue:', mu)
print('Calculated Eigenvector:', x.T[0])
v, w = eigh(A)
print('Actual Eigenvalue:', v[0])
print('Actual Eigenvector:', w[:,0].T)

#########################################################################
#							Observations								#
#########################################################################
# Calculated Eigenvalue: 0.57893339
# Calculated Eigenvector: -0.0431682  -0.35073145  0.9354806 
# Actual Eigenvalue: 0.5789333856910526
# Actual Eigenvector: -0.0431682  -0.35073145  0.9354806 