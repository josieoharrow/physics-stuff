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
#x0, y0, m0, x1, y1, m1 = 1, 2, 5, 3, 6, 3

xm1, xm2, xm3 = 1.5, float(2), 2.5
x_array = np.linspace(x0, x1, 200)

#From this, delta x = 2.
delta_x = float(x1 - x0)
before_x_array = np.linspace(x0 - delta_x, x0, 200)
after_x_array = np.linspace(x1, x1 + delta_x, 200)

############ Set up component polynomial functions ############
consts = mp.Constants(delta_x)
first_polynomial = mp.scale_polynomial(y0, mp.make_cubic(consts.y0_consts()))
second_polynomial = mp.scale_polynomial(y1, mp.make_cubic(consts.y1_consts()))
third_polynomial = mp.scale_polynomial(m0, mp.make_cubic(consts.m0_consts()))
fourth_polynomial = mp.scale_polynomial(m1, mp.make_cubic(consts.m1_consts()))

#Declare the base function
f = first_polynomial(x_array - x0) + second_polynomial(x_array - x1) + third_polynomial(x_array - x0) + fourth_polynomial(x_array - x1)

#Integral functions and fancier stuff. Largely not implemented yet.
#Todo: We can't just add up these polynomials because they are for different x inputs (regions or x as you may say)
#So this integral needs to be computed manually probably.
#Wait, is that true? If our bounds are huge, does the small difference matter? YES this is true. Our constants our based on
#their input so we can't just add the polys up and integrate over bigger bounds.
f_func = first_polynomial + second_polynomial + third_polynomial + fourth_polynomial
d = f_func(x_array - x0)
g = first_polynomial + second_polynomial + third_polynomial + fourth_polynomial
j = g.integ()
f_magnitude = (j(1000000) - j(-1000000))

#just the values, we want the function.
p = f/f_magnitude
p_func = f_func/f_magnitude

############ Before data func ############
a = mp.scale_polynomial(0, mp.make_cubic(consts.y0_consts()))
b = mp.scale_polynomial(y0, mp.make_cubic(consts.y1_consts()))
c = mp.scale_polynomial(0, mp.make_cubic(consts.m0_consts()))
d = mp.scale_polynomial(m0, mp.make_cubic(consts.m1_consts()))
f_before = a(before_x_array - 0) + b(before_x_array - x0) + c(before_x_array - 0) + d(before_x_array - x0)
f_before = b(before_x_array - x0) + d(before_x_array - x0)

############ After data func ############
e = mp.scale_polynomial(y1, mp.make_cubic(consts.y0_consts()))
k = mp.scale_polynomial(0, mp.make_cubic(consts.y1_consts()))
l = mp.scale_polynomial(m1, mp.make_cubic(consts.m0_consts()))
m = mp.scale_polynomial(0, mp.make_cubic(consts.m1_consts()))

f_after = e(after_x_array - x1) + l(after_x_array - x1)

############ Print info ############

print('========== Polynomials: ==========')
print(first_polynomial)
print(second_polynomial)
print(third_polynomial)
print(fourth_polynomial)
print('========== P func: ==========')
print(p_func)
print('========== F magnitude: ==========')
print(f_magnitude)

############ Plot ############

if(len(sys.argv) > 1):

    plt.plot(x_array, first_polynomial(x_array - x0))
    plt.plot(x_array, second_polynomial(x_array - x1))
    plt.plot(x_array, third_polynomial(x_array - x0))
    plt.plot(x_array, fourth_polynomial(x_array - x1))

    plt.plot(x_array, f)
    plt.plot(before_x_array, f_before)
    plt.plot(after_x_array, f_after)

    plt.ylabel('Derived polynomial functions')
    plt.show()    