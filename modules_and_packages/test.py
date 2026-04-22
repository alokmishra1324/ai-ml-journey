# import math

# print(math.sqrt(16))

# from math import sqrt , pi

# print(sqrt(25))
# print(pi*8)

import numpy as np

arr = np.array([12,3,4,5,])
print(arr)


from math import *

print(sqrt(144))
print(pi)

# from package.maths import addition  ##custom package that we have created

# print(addition(23,45))

from package import maths

print(maths.addition(78 , 12))

print(maths.substract(90, 12))


from package.subpackages.multi import multiply

print(multiply(45,2))