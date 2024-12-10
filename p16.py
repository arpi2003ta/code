import functools
n=9
z = sum( map ( int , [c for c in str(functools.reduce( lambda x, y: x * y, range(1, n) ) ) ] ))
print(z)
