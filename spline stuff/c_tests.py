from scipy.interpolate import BSpline
import matplotlib.pyplot as plt
import numpy as np
import random
k = 3

x = np.linspace(-5, 5, 8)
many_x = np.linspace(-5, 5, 200)

increasing_y = np.array([-3, 0, 1, 3, 7, 19, 22, 34])
decreasing_y = -np.sort(-increasing_y)

print(-np.sort(-increasing_y))

one_c = np.array([1, 1, 1, 1])
increasing_c = np.array([-1, 0, 1, 2])
decreasing_c = np.array([2, 1, 0, -1])

increasing_one_bs = BSpline(increasing_y, one_c, k)
decreasing_one_bs = BSpline(decreasing_y, one_c, k)

increasing_bs = BSpline(y, increasing_c, k)
decreasing_bs = BSpline(y, decreasing_c, k)

plt.plot(x, increasing_one_bs(x), label='increasing Ones Fit')
plt.plot(x, decreasing_one_bs(x), label='decreasing Ones Fit')

plt.plot(x, increasing_bs(x), label='Increasing Fit')
plt.plot(x, decreasing_bs(x), label='Decreasing Fit')

plt.plot(x, increasing_y, label='Increasing data')
plt.plot(x, decreasing_y, label='Decreasing data')

plt.grid(True)
plt.legend(loc='best')
plt.ylabel('some numbers')

plt.show()
