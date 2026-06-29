# Demonstrate a simple higher-order function that accepts another function as an argument

def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lst):
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # prints 15


# Define three basic math functions to return function objects based on a string input

def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


# Use the returned function and call it with a value
result = higher_order_function('square')
print(result(3))  # prints 9
result = higher_order_function('cube')
print(result(3))  # prints 27
result = higher_order_function('absolute')
print(result(-3))  # prints 3


# Closure example: add_ten returns a function that remembers the outer scope variable 'ten'
def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))   # prints 15
print(closure_result(10))  # prints 20


# Decorator example without syntactic sugar: manually wrap a function

def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())  # prints 'WELCOME TO PYTHON'


# Decorator example with @ syntax, which is a cleaner way to apply the wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator

def greeting():
    return 'Welcome to Python'


print(greeting())  # prints 'WELCOME TO PYTHON'


# Demonstrate stacked decorators and the order of execution
# The decorator closest to the function is applied first, then the next one.

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@uppercase_decorator

def greeting():
    return 'Welcome to Python'


print(greeting())  # prints ['WELCOME', 'TO', 'PYTHON']


# Decorator that accepts parameters via an inner wrapper function

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters

def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to learn.".format(first_name, last_name))


print_full_name("Rek", "Nitro", 'India')
# prints the name line and then 'I live in India'


# Using map() with a named function to transform list elements

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2


numbers_squared = map(square, numbers)
print(list(numbers_squared))  # prints [1, 4, 9, 16, 25]


# Using map() with a lambda function for the same transformation

numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # prints [1, 4, 9, 16, 25]


# Convert string values to integers using map()

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # prints [1, 2, 3, 4, 5]


# Map strings to uppercase using a named function and then a lambda

names = ["Rek", "Kirito", "Ash"]

def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  # prints ['REK', 'KIRITO', 'ASH']


names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # prints ['REK', 'KIRITO', 'ASH']


# Filter even numbers from a list

numbers = [1, 2, 3, 4, 5]

def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # prints [2, 4]


# Filter odd numbers from a list

numbers = [1, 2, 3, 4, 5]

def is_odd(num):
    if num % 2 != 0:
        return True
    return False


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # prints [1, 3, 5]


# Filter names longer than 3 characters

names = ["Rek", "Kirito", "Ash"]

def is_name_long(name):
    if len(name) > 3:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))  # prints ['Kirito']


# Reduce strings to a single numeric sum by converting each value to int

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']

def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)  # prints 15
