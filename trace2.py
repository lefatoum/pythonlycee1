import matplotlib.pyplot as plt
import numpy
import math

X = numpy.arange(-1, 5, 0.1)

Y = []
Ys = []
for x in X:
    Y.append(x**2)
    Ys.append(math.sin(x)+1)

plt.plot(X, Y)
plt.plot(X, Ys)


plt.title('mon titre')
plt.grid(True)
plt.xlabel('x label')
plt.ylabel('y label')

plt.legend(["courbe 1", "courbe 2"])


plt.axis([0, 5, 0, 3])

plt.show()