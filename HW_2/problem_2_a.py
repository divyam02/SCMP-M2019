import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

acc = np.zeros(shape=(1, 10))
truth = np.ones(shape=(1, 2))

for i in range(10):
	epsilon = 10**(-2*(i+1))
	temp = np.zeros(shape=(1, 2))
	temp[0, 1] = (2 - (1+epsilon)/epsilon)/(1 - 1/epsilon)
	temp[0, 0] = (1+epsilon - temp[0, 1])/epsilon

	acc[0, i] = norm(truth - temp)

	print("truth:", truth)
	print("temp:", temp)
plt.figure(figsize=(10, 10))
plt.scatter(range(1, 11), acc[0], label='Accuracy')
plt.ylabel('L2 distance between true and estimated solution')
plt.xlabel('Values of K (Negative Log Scale)')
plt.savefig('Problem_2_a.png')


# Observations:
# It is apparent that error quickly increases (as measured by L2 distance)
# for smaller values of epsilon(~1e-16), converging to [0 1].
