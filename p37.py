import numpy as np
xarr = np.array([-1.0, 1.5, -2.0, 2.5, -3.0])
yarr = np.array([1.0, -1.5, 2.0, -2.5, 3.0])
cond = np.array([True, False, True, False, False])
outarr = np.where(cond, xarr, yarr)
print(outarr)
