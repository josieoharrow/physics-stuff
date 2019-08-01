import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as polynomial
import scipy

############ Test file for plotting original polynomial function. ############

#Test data: x0 = 1, y0 = 5, m0 = 5; x1 = 3, y1 = 6, m1 = -1.
x0, y0, m0, x1, y1, m1 = 1, 5, 5, 3, 6, -1
xm1, xm2, xm3 = 1.5, float(2), 2.5
x_array = np.linspace(x0, x1, 200)

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

#Set up the m-based polynomials
b0, b1, b2, b3 = 0, 1, float(-2)/delta_x, float(1)/delta_x_squared
third_polynomial_consts = [b3, b2, b1, b0]
third_polynomial = scipy.poly1d(np.multiply(m0, third_polynomial_consts))
#The consts. are different enough I just use new constants
c0, c1, c2, c3 = 0, float(-1) - float(m1), float(-1)/delta_x, float(m1)/delta_x_squared
fourth_polynomial_consts = [c3, c2, c1, c0]
fourth_polynomial = scipy.poly1d(np.multiply(m1, fourth_polynomial_consts))

#Declare the base function
f = first_polynomial(x_array - x0) + second_polynomial(x_array - x1) + third_polynomial(x_array - x0) + fourth_polynomial(x_array - x1)

#Integral functions
integ_1 = first_polynomial.integ()
integ_2 = second_polynomial.integ()
integ_3 = third_polynomial.integ()
integ_4 = fourth_polynomial.integ()
i = integ_1 + integ_2 + integ_3 + integ_4
g = first_polynomial + second_polynomial + third_polynomial + fourth_polynomial
b = g*g#.integ()
c = b.integ()
f_magnitude = (c(1) - c(0))
p = f/f_magnitude

#Print info
print('a0, a1, a2, a3: ', a0, a1, a2, a3)
print(first_polynomial)
print(second_polynomial)
print(third_polynomial)
print(fourth_polynomial)
print(integ_1)
print(c(1) - c(0))
print(b(x1) - b(x0))
print(i(x1) - i(x0))

#Plot
plt.plot(x_array, first_polynomial(x_array - x0))
plt.plot(x_array, second_polynomial(x_array - x1))
plt.plot(x_array, third_polynomial(x_array - x0))
plt.plot(x_array, fourth_polynomial(x_array - x1))
plt.plot(x_array, p)#(x_array - x1))

plt.plot(x_array, f)

plt.ylabel('Derived polynomial functions')
plt.show()    