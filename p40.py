import pandas as pd
marks = {'Ajay': 96, 'Usha': 90, 'Deep': 94, 'Ria': 89}
obj1 = pd.Series(marks)
print(obj1)
student = ['Usha', 'Vijay', 'Ria', 'Ajay']
obj2 = pd.Series(marks, index = student)
print(obj2)
print(pd.isnull(obj2))
