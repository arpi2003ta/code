import numpy as np
arr = np.array([1, 7, 5, -4, 8, -3])
print(arr[1:6:2])

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [1, 3, 4]
print(arr[indices])

m = np.matrix('2 1 8; 0 5 6; 7 9 3')
print(np.sort(m))

import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3]})
print(df.index)

df = pd.DataFrame({'A': [1, None, 3]})
print(df.fillna(0))  # Replaces NaN with 0
