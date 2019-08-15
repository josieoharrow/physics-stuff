import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as polynomial
import scipy
import make_polynomial as mp
import sys

############ Test file for plotting original polynomial function. ############

#Test data
#x0, y0, m0, x1, y1, m1 = 1, 5, 5, 3, 6, -1
x0, y0, m0, x1, y1, m1 = 1, 5, 5, 3, 6, 3
x_bins = [-4, -2, 0, 2, 4]
y_vals = [1, 2, -3, 4, 2]
m_vals = [2, 1, -1, 3, 4]
#x0, y0, m0, x1, y1, m1 = 1, 2, 5, 3, 6, 3

#From this, delta x = 2.
delta_x = 2#float(x1 - x0)

def a(x):
    x = float(x)
    if -delta_x < x <= 0:
        return 1 - 3*x**2/delta_x**2 - 2*x**3/delta_x**3
    elif 0 < x < delta_x:
        return 1 - 3*x**2/delta_x**2 + 2*x**3/delta_x**3
    else:
        return 0.
a = np.vectorize(a)

def integral_a(x):
    x = float(x)
    if -delta_x < x <= 0:
        return x - x**3/delta_x**2 - x**4/2*delta_x**3
    elif 0 < x < delta_x:
        return x - x**3/delta_x**2 + x**4/2*delta_x**3
    else:
        return 0.
integral_a = np.vectorize(integral_a)

def b(x):
    x = float(x)
    if -delta_x < x <= 0:
        return x + 2*x**2/delta_x + x**3/delta_x**2
    elif 0 < x < delta_x:
        return x - 2*x**2/delta_x + x**3/delta_x**2
    else:
        return 0.
b = np.vectorize(b)

def integral_b(x):
    x = float(x)
    if -delta_x < x <= 0:
        return x**2/2 + 2*x**3/3*delta_x + x**4/4*delta_x**2
    elif 0 < x < delta_x:
        return x**2/2 - 2*x**3/3*delta_x + x**4/4*delta_x**2
    else:
        return 0.
integral_b = np.vectorize(integral_b)

############ Print info ############

############ Plot ############

if(len(sys.argv) > 1):

    plt.ylabel('Derived polynomial functions')
    x = np.linspace(-2*delta_x, 2*delta_x, 1000)
    i = 0
    for xi in x_bins:
        print(xi)
        x = np.linspace(xi - delta_x, xi + delta_x, 200)
        #plt.plot(x, y_vals[i]*a(x - xi))
        #plt.plot(x, b(x - xi))
        plt.plot(x, y_vals[i]*a(x - xi) + m_vals[i]*b(x - xi))
        i = i + 1

    #plt.figure()
    x = np.linspace(2*-delta_x, 2*delta_x, 100)
    #plt.plot(x, a(x))
    #plt.plot(x, b(x))
    plt.plot(x, integral_b(x))
    plt.plot(x, integral_a(x)/15)
    #plt.plot(x, integral_a(x) + integral_b(x))
    plt.show()    