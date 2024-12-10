import numpy as np
names = np.array(['HITK', 'JU', 'IIEST', 'HITK'])
arr = np.matrix([[ 0, -1, 2], [-3, -4, -6], [8, -9, -1], [7, 5, 0]])
print(arr[names == 'HITK'])