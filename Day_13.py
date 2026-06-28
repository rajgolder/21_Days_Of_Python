language = "Python"

# Convert the string to a list of characters using the built-in list() function.
lst = list(language)
print(type(lst))
print(lst)

# Create the same list of characters using a list comprehension.
lst = [i for i in language]
print(type(lst))
print(lst)

# Generate a list of numbers from 0 to 10 using range().
numbers = [i for i in range(11)]
print(numbers)

# Generate a list of squares from 0^2 to 10^2.
squares = [i * i for i in range(11)]
print(squares)

# Generate a list of tuples containing a number and its square.
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Filter even numbers from 0 to 20.
even_num = [i for i in range(21) if i % 2 == 0]
print(even_num)

# Filter odd numbers from 0 to 20.
odd_num = [i for i in range(21) if i % 2 != 0]
print(odd_num)

# Select positive even numbers from a predefined list.
numbers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
positive = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive)

# Flatten a 2D list into a single list using a nested comprehension.
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_list)
flattened_list = [number for row in list_of_list for number in row]
print(flattened_list)

# Define a normal function that adds two numbers.
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))

# Define the same addition operation as a lambda function.
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))

# Call an anonymous lambda function directly.
print((lambda a, b: a + b)(2, 3))

# Lambda expressions for square and cube operations.
square = lambda x: x ** 2
print(square(3))
cube = lambda x: x ** 3
print(cube(3))

# Lambda with multiple parameters.
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(2, 4, 6))

# Higher-order function returning a lambda to compute x raised to the power n.
def power(x):
    return lambda n: x ** n

cube = power(2)(3)
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)