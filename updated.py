import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as polynomial
import scipy
import make_polynomial as mp
import sys

#for now, use one.
DELTA_X = float(1)

#Test data. Should handle case for sorting...
startX = -4
bins = 10
y = [1, 2, -3, 4, 2, -3, 4, 2, 5, 6]
m = [2, 1, -1, 3, 4, 2, -3, 4, 2, -3]


def a(x, delta_x):
    x = float(x)
    if -delta_x < x < 0:
        return -((x+delta_x)**2)*(x-delta_x/2)*(2/delta_x**3)
    elif 0 <= x < delta_x:
        return ((x-delta_x)**2)*(x+delta_x/2)*(2/delta_x**3)
    else:
        return 0.

def b(x, delta_x):
    if -delta_x < x < 0:
        return -(-1/delta_x**2)*(x)*(x+delta_x)**2
    elif 0 <= x < delta_x:
        return (1/delta_x**2)*(x)*(x-delta_x)**2
    else:
        return 0.

def tangent(x, x1, y1, m):
    return m*(x - x1) + y1

plt.ylabel('Polynomial function')
xSpread = np.linspace(startX - 2*DELTA_X, startX + bins*DELTA_X + 2*DELTA_X, 300)
sigma = []
first = True
i = 0
xi = startX

#Since we rely on the assumption xi are evenly spaced apart...
while i < bins:
    j = 0
    for xSpreadVal in xSpread:
        if first:
            sigma.append(y[i]*a(xSpreadVal - xi, DELTA_X) + m[i]*b(xSpreadVal - xi, DELTA_X))
        else:
            sigma[j] = sigma[j] + y[i]*a(xSpreadVal - xi, DELTA_X) + m[i]*b(xSpreadVal - xi, DELTA_X)
        j = j + 1
    i = i + 1
    xi = xi + DELTA_X
    first = False

#plt.plot(xSpread, sigma)
#plt.show()   

plt.plot(xSpread, sigma, linestyle='dashed', color='red')
xbins = [startX]
i = 0
while i < bins:
    x = np.linspace(0.2*-DELTA_X + xbins[i], 0.2*DELTA_X + xbins[i], 100)
    plt.plot(x, tangent(x, xbins[i], y[i], m[i]), color='blue')
    if i != bins - 1:
        xbins.append(xbins[i] + DELTA_X)
    i = i + 1

plt.scatter(xbins, y)
plt.show()    