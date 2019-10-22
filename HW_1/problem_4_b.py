import numpy as np
import matplotlib.pyplot as plt
from math import tan as tan

x1 = np.zeros(shape=(1, 17))
x2 = np.zeros(shape=(1, 17))

for i in range(17):
	h = 10**(-i)
	# print(h)
	x1[0, i] = (tan(1 + h) - tan(1 - h))/(2*h)
	x2[0, i] = np.log(abs(x1[0, i] - np.square(np.arccos(1))))

plt.figure(figsize=(10, 10))
plt.scatter(range(0, 17), x2[0], label="Magnitude of absolute error")
plt.xlabel("Values of h (Negative Log Scale)")
plt.ylabel("Magnitude of absolute error (Log Scale)")
plt.legend(loc='lower right')
plt.savefig("problem_4_b.png")

print("""
#####################################################################
#                       Problem 4 - part (b)                        #
#####################################################################

# Yes, there is a minimum value for the magnitude of error near
# -log(h) = 0.
# 
# Machine precision for floating point values on 64-bit machine is
# 2.220446049250313e-16 (approx.) and the square root is 
# 1.4901161193847656e-08 (approx.). h corresponding to lowest magnitude
# of absolute error is h = 1e-0.
""")