def fun(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return fun(n//2) + fun(n%2)
print(fun(17))