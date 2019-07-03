import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

x = np.linspace(-5, 5, 5)
many_x = np.linspace(-5, 5, 200)
y = np.power(x, 3)
spline = CubicSpline(x, y)

plt.plot(many_x, spline(many_x))
plt.ylabel('some numbers')

plt.show()
