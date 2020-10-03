import matplotlib.pyplot as plt
import numpy
import random

X = []
Y = []
for i in range(10):
    X.append(random.uniform(0, 3))
    Y.append(random.uniform(0, 3))

plt.plot(X, Y, 'ro')
plt.axis([-2, 10, -2, 8])
plt.show()