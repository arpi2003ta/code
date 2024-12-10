import numpy as np
# Array
arr = np.array([[1, 2], [3, 4]])
print(arr * arr) # Element-wise multiplication
# Matrix
mat = np.matrix([[1, 2], [3, 4]])
print(mat * mat) # Matrix multiplication

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3]) # Output: [4 5]

import numpy as np
arr = np.array([1, 2, 3, 4])
print(np.sqrt(arr)) # Output: [1. 1.41421356 1.73205081 2.]