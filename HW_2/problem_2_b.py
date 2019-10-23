import numpy as np
from numpy.linalg import norm
from numpy.linalg import solve
import matplotlib.pyplot as plt

acc = np.zeros(shape=(1, 10))
truth = np.ones(shape=(1, 2))
A = np.ones(shape=(2, 2))
b = np.ones(shape=(2, 1))
for i in range(10):
	epsilon = 10**(-2*(i+1))
	temp = np.zeros(shape=(1, 2))
	A[0, 1] = epsilon
	b[0, 0] = 1+epsilon
	b[1, 0] = 2
	# Using partial pivoting and iterative refinement:
	temp[0, 1] = (1 + epsilon + 2*epsilon)/(1 - epsilon)
	temp[0, 0] = 2 - temp[0, 1]

	r = b - np.dot(A, temp.T)
	d = solve(A, r)

	temp = temp + d.T

	acc[0, i] = norm(truth - temp)/norm(truth)

	print("truth:", truth)
	print("temp:", temp)

plt.figure(figsize=(10, 10))
plt.scatter(range(1, 11), acc[0], label='Accuracy')
plt.ylabel('L2 distance between true and estimated solution')
plt.xlabel('Values of K (Negative Log Scale)')
plt.savefig('Problem_2_b.png')


# Observations:
# There seems to be no error! It is likely the case 
# that whatever error is there is less than the 
# machine precision.
# 
