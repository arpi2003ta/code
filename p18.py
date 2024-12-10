from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, nums) # Multiplies all elements
print(result) # Output: 24