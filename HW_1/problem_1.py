import matplotlib.pyplot as plt
import numpy as np


values = list()
for i in range(161):
	values.append(1.920 + i*0.001)

# print(values)

x1 = np.zeros(shape=(1, len(values)))
x2 = np.zeros(shape=(1, len(values)))

for i, val in enumerate(values):
	x1[0, i] = (val-2)**9
	x2[0, i] = val**9 - 18*(val**8) + 144*(val**7) - 672*(val**6) + 2016*(val**5) - 4032*(val**4) + 5376*(val**3) - 4608*(val**2) + 2304*val - 512

plt.figure(figsize=(10, 10))
plt.plot(values, x1[0], label='Direct')
plt.plot(values, x2[0], label='Expansion')

plt.ylabel('f(x)')
plt.xlabel('Input values')
plt.legend(loc='lower right')
plt.savefig('problem_1.png')

