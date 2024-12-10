Marks =80
print(Marks)
def fun1() :
    global Marks
    print(Marks)
    Marks = 'Marks changed'

fun1()
print(Marks)