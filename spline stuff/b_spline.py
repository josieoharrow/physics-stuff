from scipy.interpolate import BSpline
import matplotlib.pyplot as plt
import numpy as np
import random
k = 3

x = np.linspace(-5, 5, 8)
many_x = np.linspace(-5, 5, 200)

x_bins = [-5, -2.5, 0, 2.5, 5]

y = np.sort([random.gauss(-10, 0.5), random.gauss(-1, 0.5), random.gauss(0, 0.5), random.gauss(1, 0.5), random.gauss(3, 0.5), random.gauss(4, 0.5), random.gauss(5, 0.5), random.gauss(10, 0.5)])

c = np.array([-1, 2, 0, -1])
a = np.array([-5, -5, -5, -5])
one_c = np.array([1, 1, 1, 1])
tiny_c = np.array([0.1, 0.1, 0.1, 0.1])

increasing_c = np.array([-1, 0, 1, 2])
decreasing_c = np.array([2, 1, 0, -1])

bspline = BSpline(y, c, k)
one_bs = BSpline(y, one_c, k)
a_bs = BSpline(y, a, k)
tiny_bs = BSpline(y, tiny_c, k)
increasing_bs = BSpline(y, increasing_c, k)
decreasing_bs = BSpline(y, decreasing_c, k)

#This fit is totally bad. Commenting out for now just so I can look more closely at the others.
#plt.plot(x, bspline(x), label='Bad Fit')

plt.plot(x, one_bs(x), label='Ones Fit')
plt.plot(x, a_bs(x), label='Negative Five Fit')
plt.plot(x, increasing_bs(x), label='Increasing C Fit')
plt.plot(x, decreasing_bs(x), label='Decreasing Fit')
plt.plot(x, tiny_bs(x), label='Sensitive Fit')
plt.plot(x, y, label='data')
plt.grid(True)
plt.legend(loc='best')
plt.ylabel('some numbers')

plt.show()
