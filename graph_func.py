import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as polynomial
import scipy
import make_polynomial as mp
import sys

############ Test file for plotting original polynomial function. ############

#Test data: x0 = 1, y0 = 5, m0 = 5; x1 = 3, y1 = 6, m1 = -1.
x0, y0, m0, x1, y1, m1 = 1, 5, 5, 3, 6, -1
xm1, xm2, xm3 = 1.5, float(2), 2.5
x_array = np.linspace(x0, x1, 200)

#From this, delta x = 2.
delta_x = float(x1 - x0)

############ Set up component polynomial functions ############
consts = mp.Constants(delta_x)
first_polynomial = mp.scale_polynomial(y0, mp.make_cubic(consts.y0_consts()))
second_polynomial = mp.scale_polynomial(y1, mp.make_cubic(consts.y1_consts()))
third_polynomial = mp.scale_polynomial(m0, mp.make_cubic(consts.m0_consts()))
fourth_polynomial = mp.scale_polynomial(m1, mp.make_cubic(consts.m1_consts()))

#Declare the base function
f = first_polynomial(x_array - x0) + second_polynomial(x_array - x1) + third_polynomial(x_array - x0) + fourth_polynomial(x_array - x1)

#Todo: Fix "f_func". I don't know why yet but this is broken and it is the key to having actual interpolation.
f_func = first_polynomial + second_polynomial + third_polynomial + fourth_polynomial
d = f_func(x_array - x0)

#Integral function
#Todo: We can't just add up these polynomials because they are for different x inputs (regions or x as you may say)
#So this integral needs to be computed manually probably.
#Wait, is that true? If our bounds are huge, does the small difference matter? YES this is true. Our constants our based on
#their input so we can't just add the polys up and integrate over bigger bounds.
g = first_polynomial + second_polynomial + third_polynomial + fourth_polynomial
j = g.integ()
print(j)
f_magnitude = (j(1000000) - j(-1000000))

#just the values, we want the function.
p = f/f_magnitude
p_func = f_func/f_magnitude

#Print info
print('========== Polynomials: ==========')
print(first_polynomial)
print(second_polynomial)
print(third_polynomial)
print(fourth_polynomial)
print('========== P func: ==========')
print(p_func)
print('========== F magnitude: ==========')
print(f_magnitude)

#Plot
if(len(sys.argv) > 1):
    
    plt.plot(x_array, first_polynomial(x_array - x0))
    plt.plot(x_array, second_polynomial(x_array - x1))
    plt.plot(x_array, third_polynomial(x_array - x0))
    plt.plot(x_array, fourth_polynomial(x_array - x1))

    plt.plot(x_array, p)
    plt.plot(x_array, f)

    plt.ylabel('Derived polynomial functions')
    plt.show()    