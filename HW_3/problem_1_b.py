import numpy as np
from numpy.linalg import norm
from numpy.linalg import solve
from numpy.linalg import qr
import matplotlib.pyplot as plt

def gen_hilbert_matrix(n):
	"""
	# Generate Hilbert matrix with entries
	"""
	temp = np.ones(shape=(n, n))
	for i in range(n):
		for j in range(n):
			temp[i, j] = 1/(i+j+1) 
			# Change hilbert matrix entry because of zero indexing.

			temp[j, i] = np.copy(temp[i, j])

	return temp

def house_holder_method(H):
	Q, R = qr(H)
	return Q

def classical_gram_schmidt(H, n):
	"""
	# Return orthogonal matrix with orthonormal column space
	of the Hilbert matrix H using the classical method.
	# Solved assuming rows were columns so returning the
	transpose.
	"""
	temp = np.zeros(shape=H.shape)
	for k in range(n):
		temp[k] = H[k]
		for j in range(k):
			r = np.dot(temp[j], H[k].T)
			temp[k] = temp[k] - r*temp[j]
		r = norm(temp[k])
		temp[k] = temp[k]/r

	# print(temp)
	# print(np.dot(temp, temp.T))
	return temp.T

def modified_gram_schmidt(H, n):
	"""
	# Return orthogonal matrix with orthonormal column space
	of the Hilbert matrix H using the modified method
	# Solved assuming rows were columns so returning the
	transpose.
	"""
	temp = np.zeros(shape=H.shape)
	for k in range(n):
		r = norm(H[k])
		temp[k] = H[k]/r
		for j in range(k+1, n):
			r = np.dot(temp[k], H[j].T)
			H[j] = H[j] - r*temp[k]

	# print(temp)
	# print(np.dot(temp, temp.T))
	return temp.T

x1 = np.zeros(shape=(1, 11))
x2 = np.zeros(shape=(1, 11))
x3 = np.zeros(shape=(1, 11))
x4 = np.zeros(shape=(1, 11))

for i in range(2, 13):
	identity_matrix = np.identity(i)
	H = gen_hilbert_matrix(i)
	Q = classical_gram_schmidt(np.copy(H), i)
	# Classical
	x1[0, i-2] = -1*(np.log(norm(identity_matrix - np.dot(Q.T, Q)))/np.log(10))
	# Classical applied twice
	Q = classical_gram_schmidt(Q.T, i)
	x3[0, i-2] = -1*(np.log(norm(identity_matrix - np.dot(Q.T, Q)))/np.log(10))
	# Modified
	Q = modified_gram_schmidt(np.copy(H), i)
	x2[0, i-2] = -1*(np.log(norm(identity_matrix - np.dot(Q.T, Q)))/np.log(10))
	# House-Holder
	Q = house_holder_method(np.copy(H))
	x4[0, i-2] = -1*(np.log(norm(identity_matrix - np.dot(Q.T, Q)))/np.log(10))

plt.figure(figsize=(20, 10))
plt.plot(range(2, 13), x1[0], label='Classical Gram-Schmidt')
plt.plot(range(2, 13), x2[0], label='Modified Gram-Schmidt')
plt.plot(range(2, 13), x3[0], label='Classical Gram-Schmidt applied twice')
plt.plot(range(2, 13), x4[0], label='House-Holder')

plt.ylabel('Digits of Accuracy')
plt.xlabel('Value of n')
plt.legend(loc='upper right')
plt.savefig('problem_1_b.png')

# Observations:
# House-Holder's Method performs well even for large
# n, as compared to the other methods
# 
