import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as polynomial
import scipy

############ Test file for plotting original polynomial function. ############

#Test data: x0 = 1, y0 = 5, m0 = 5; x1 = 3, y1 = 6, m1 = -1.
x0, y0, m0, x1, y1, m1 = 1, 5, 5, 3, 6, -1

#From this, delta x = 2.
delta_x = float(x1 - x0)
delta_x_squared = np.square(delta_x)
delta_x_cubed = np.power(delta_x, 3)

#Set up the first polynomial
a0, a1, a2, a3 = 1, 0, float(-3)/(delta_x_squared), float(2)/delta_x_cubed
first_polynomial = scipy.poly1d([y0*a3, y0*a2, y0*a1, y0*a0])

#Get info
print('a0, a1, a2, a3: ', a0, a1, a2, a3)
print(first_polynomial(x0 - x0), first_polynomial(delta_x))
print(float(2)/delta_x_cubed)

#Plot
plt.plot([x0, x1], [first_polynomial(x0 - x0), first_polynomial(delta_x)])
plt.ylabel('Derived polynomial functions')
plt.show()