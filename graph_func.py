import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as polynomial
import scipy

############ Test file for plotting original polynomial function. ############

####Function defs.



#Test data: x0 = 1, y0 = 5, m0 = 5; x1 = 3, y1 = 6, m1 = -1.
x0, y0, m0, x1, y1, m1 = 1, 5, 5, 3, 6, -1
xm1, xm2, xm3 = 1.5, 2, 2.5

#From this, delta x = 2.
delta_x = float(x1 - x0)
delta_x_squared = np.square(delta_x)
delta_x_cubed = np.power(delta_x, 3)

#Set up the y-based polynomials
a0, a1, a2, a3 = 1, 0, float(-3)/(delta_x_squared), float(2)/delta_x_cubed
first_polynomial_consts = [a3, a2, a1, a0]
second_polynomial_consts = [-a3, a2, a1, a0]
first_polynomial = scipy.poly1d(np.multiply(y0, first_polynomial_consts))
second_polynomial = scipy.poly1d(np.multiply(y1, second_polynomial_consts))
basic_a = scipy.poly1d(second_polynomial_consts)

#Get info
print('a0, a1, a2, a3: ', a0, a1, a2, a3)
print(first_polynomial(x0 - x0), first_polynomial(x1 - x0))
print(first_polynomial)
print(second_polynomial)
print(x0 - x1)
print(second_polynomial(x0 - x1), second_polynomial(x1 - x1))
print(float(2)/delta_x_cubed)

#Plot
plt.plot([x0, x1], [first_polynomial(x0 - x0), first_polynomial(x1 - x0)])
plt.plot([x0, xm1, xm2, xm3, x1], [second_polynomial(x0 - x1), second_polynomial(xm1 - x1), second_polynomial(xm2 - x1), second_polynomial(xm3 - x1), second_polynomial(x1 - x1)])
plt.ylabel('Derived polynomial functions')
plt.show()    