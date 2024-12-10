d = {4: 'India', 9: 'USA', 17: 'Japan', 24: 'Australia'}
print([d[i] for i in d.keys() if i%2 == 0])

nested_list = [[10,15], 24, [True], [5, ['Tom', 'Harry'], 10]]
print(nested_list[3][1][1])