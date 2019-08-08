import scipy
import numpy as np

#constants array like: [a0, a1, a2, a3]
def make_cubic(constants_array):
    a3 = constants_array[3]
    a2 = constants_array[2]
    a1 = constants_array[1]
    a0 = constants_array[0]
    cubic_consts = [a3, a2, a1, a0]
    cubic = scipy.poly1d(cubic_consts)
    return cubic

def scale_polynomial(scalar, polynomial):
    return np.polymul(scalar, polynomial)

class Constants:

    delta_x = None
    delta_x_squared = None#np.square(delta_x)
    delta_x_cubed = None#np.power(delta_x, 3)

    def __init__(self, delta_x): 
            self.delta_x = delta_x
            self.delta_x_squared = np.square(delta_x)
            self.delta_x_cubed = np.power(delta_x, 3)
    
    def y0_consts(self):
        return [1, 0, float(-3)/(self.delta_x_squared), float(2)/self.delta_x_cubed]

    def y1_consts(self):
        return [1, 0, float(-3)/(self.delta_x_squared), -float(2)/self.delta_x_cubed]
    
    def m0_consts(self):
        return [0, 1, float(-2)/self.delta_x, float(1)/self.delta_x_squared]

    def m1_consts(self):
        return [0, float(1), float(2)/self.delta_x, float(1)/self.delta_x_squared]    