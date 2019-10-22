import numpy as np
import matplotlib.pyplot as plt

x1 = np.ones(shape=(1, 10))
x2 = np.ones(shape=(1, 10))

for i in range(0, 10):
	if i!=0:
		x1[0, i] = x1[0, i]*(i+1)

	x2[0, i] = np.sqrt(2*np.pi * i)*((i/np.e)**i)


plt.figure(figsize=(20, 10))
plt.scatter(range(1, 11), x1[0], label='Direct')
plt.scatter(range(1, 11), x2[0], label='Approximation')

plt.ylabel('f(x)')
plt.xlabel('Input values')
plt.legend(loc='lower right')
plt.savefig('problem_2.png')

