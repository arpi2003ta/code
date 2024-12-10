# Initialize the list with integers from 1 to 18
numbers = list(range(1, 19))

# (i) Display the squares of each element of the list
squares = list(map(lambda x: x**2, numbers))
print("Squares of each element:", squares)

# (ii) Display only the elements which are divisible by 5
divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print("Elements divisible by 5:", divisible_by_5)

# (iii) Display the sum of all the elements of the list
sum_of_elements = sum(numbers)
print("Sum of all elements:", sum_of_elements)
