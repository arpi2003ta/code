x = [1, 2, 3, 4, 5, 6]
y = list(map(lambda n: n**3, filter(lambda n: n % 2 != 0, x)))
print(y)
