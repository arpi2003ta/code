import numpy as np

# Creating arr1: A 4x3 array of integers
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Creating arr2: A 1D array with 4 integers
arr2 = np.array([1, 2, 3, 4])

# Display the shapes of arr1 and arr2
print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)

# Broadcasting rules to check if arr3 = arr1 - arr2 is possible
arr2_reshape=arr2.reshape(4,1)
print(arr2_reshape)

result=arr1-arr2_reshape
print(result)
