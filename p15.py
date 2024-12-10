def my_func(x): 
    ab={} 
    keys = x.keys() 
    for j in keys: 
        if j!=0: 
            ab[j-1]=(j)*x[j] 
    return ab 
print(my_func({1:-3, 3:2, 5:-1, 6:2})) 
print(my_func({0:-4, 2:12, 3:-2, 4:3, 8:2}))
