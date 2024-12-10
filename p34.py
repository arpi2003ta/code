import pandas as pd
marks = {
    'Name': ['Alice', 'Bob'],
    'Maths.': [85, 90],
    'English': [78, 88]
}

frame1 = pd.DataFrame(marks)
print(frame1)
print("Maths." in frame1.columns)
print("XI" in frame1.index)