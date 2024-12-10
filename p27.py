numbers = [3, 6, 9, 12, 15, 17, 18, 21]
result = [x for x in numbers if x % numbers[0] != 0]
print(result)
