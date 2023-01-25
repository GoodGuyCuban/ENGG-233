import numpy as np
NUM_ARRAYS = 3

measurements_1 = np.array([3,6,9,-1,4])
measurements_2 = np.array([20,5,8,10,-2])
measurements_3 = np.array([-7,4,0,-3,5])

result = ((measurements_1+measurements_2+measurements_3)/NUM_ARRAYS).max()
print(measurements_1)
print(measurements_2)
print(measurements_3)
print((measurements_1+measurements_2+measurements_3)/NUM_ARRAYS)
print(result)