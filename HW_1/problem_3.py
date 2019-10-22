import numpy as np
import matplotlib.pyplot as plt

values = list()
for i in range(161):
	values.append(1.920 + i*0.001)

# print(values)

x1 = np.zeros(shape=(1, len(values)))
x2 = np.zeros(shape=(1, len(values)))

for i, val in enumerate(values):
	x1[0, i] = (val-2)**9
	x2[0, i] = val**9 - 18*(val**8) + 144*(val**7) - 672*(val**6) + 2016*(val**5) - 4032*(val**4) + 5376*(val**3) - 4608*(val**2) + 2304*val - 512

x3 = np.ones(shape=(1, 10))
x4 = np.ones(shape=(1, 10))

for i in range(0, 10):
	if i!=0:
		x3[0, i] = x3[0, i]*(i+1)

	x4[0, i] = np.sqrt(2*np.pi * i)*((i/np.e)**i)


print("\n\nAbsolute errors from Problem 1:")
for i in range(list(x1.shape)[1]):
	print(x2[0, i]-x1[0, i], end=" ")

print("\n\nAbsolute errors from Problem 2:")
for i in range(list(x3.shape)[1]):
	print(x4[0, i]-x3[0, i], end=" ")

print("\n\nRelative errors from Problem 1:")
for i in range(list(x1.shape)[1]):
	print((x2[0, i]-x1[0, i])/x1[0, i], end=" ")

print("\n\nRelative errors from Problem 2:")
for i in range(list(x3.shape)[1]):
	print((x4[0, i]-x3[0, i])/x3[0, i], end=" ")

print("\n\n")

print("""
#####################################################################
#                       Problem 3 - part (a)                        #
#####################################################################

# From my understanding Relative Error would be a better meaure for 
# polynomial evaluation. We might have instances where our estimate and
# the true value are very small. In this case absolute error may be less
# than the machine precision; giving an inaccurate value due to represen-
# -tation. Now if the true value is also small, we can express relative 
# error as (x_estimate/x_true) - 1, which is numerically stable.


#####################################################################
#                       Problem 3 - part (b)                        #
#####################################################################

# It is clear from the calculated values that both relative and 
# absolute errors increase.
""")