import matplotlib.pyplot as plt
import numpy as np
import random

from scipy.interpolate import CubicSpline

x = np.linspace(-5, 5, 5)
many_x = np.linspace(-5, 5, 200)
y = [random.random(), random.random(), random.random(), random.random(), random.random()]
spline = CubicSpline(x, y)

plt.plot(many_x, spline(many_x), label='fit')
plt.plot(many_x, spline(many_x, 2), label='fit')
plt.plot(many_x, spline(many_x, 1), label='fit')
plt.plot(x, y, label='data')
plt.ylabel('some numbers')

plt.show()
