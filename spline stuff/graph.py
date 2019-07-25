import matplotlib.pyplot as plt
import numpy as np
import scipy

x = np.linspace(-5, 5, 5)
y = np.power(x, 3)

i = 0
last_y = y[0]
last_x = x[0]
print(y)

slopes = []
for point in y:
 #   print point
  #  print x[i]
    this_x = x[i]
    this_y = y[i]
    if i != len(y):
        #Do something
        old_x = x[i - 1]
        old_y = y[i - 1]
        slopes.append((this_y - old_y)/ np.absolute(this_x - old_x))
        print(str((this_y - old_y)/ np.absolute(this_x - old_x)) + " dif: " + str(this_y - old_y) + " y's: " + str(this_y) + " " + str(old_y))#)
    else:
      #  print y[i]
        next_x = x[1 + i]
        next_y = y[1 + i]
        slopes.append((next_y - this_y)/ np.absolute(this_x - next_x))
        print(str((next_y - this_y)/ np.absolute(this_x - next_x)) + " dif: " + str(next_y - this_y) + " y's: " + str(next_y) + " " + str(this_y))
    i = i + 1

#plt.plot(x,y)
#plt.ylabel('some numbers')

#plt.show()
