import numpy as np
from numpy.linalg import qr as qr
from numpy.linalg import norm as norm
from numpy.linalg import solve as solve

A1 = np.asarray([[2, 3, 2], [10, 3, 4], [3, 6, 1]])
A2 =  np.asarray([[6, 2, 1], [2, 3, 1], [1, 1, 1]])

def modified_QR_iter(A):
	sig = A[-1][-1]
	Q, R = qr(A-(sig*np.eye(3)))
	A = np.dot(R, Q) + sig*np.eye(3)
	return A, Q, R

temp = np.copy(A1)
for i in range(50):
	temp, Q, R = modified_QR_iter(temp)

print('Original Matrix:')
print(A1)
print('Obtained Eigenvalues:', np.diagonal(temp))

temp = np.copy(A2)
for i in range(50):
	temp, Q, R = modified_QR_iter(temp)

print('Original Matrix:')
print(A2)
print('Obtained Eigenvalues', np.diagonal(temp))


#########################################################################
#							Observations								#
#########################################################################
# Eigenvalues obtained as compared to other methods appear to be 
# consistent. These are:
# 11, -3, -2 for matrix A1 and
# 7.2879, 2.1330, 0.5789 for matrix A2
# 
# 
# 
