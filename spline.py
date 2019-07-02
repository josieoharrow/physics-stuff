import matplotlib.pyplot as plt
import numpy as np
import scipy

x = np.linspace(-5, 5, 5)
y = np.power(x, 3)
spline = scipy.interpolate.CubicSpline(x, y)

plt.plot(spline)
plt.ylabel('some numbers')

plt.show()
