a = [[1, 2], [3, 4], [5, 6], [7, 8]]
b = [[c[i] for c in a] for i in range(2)]
print(b)
