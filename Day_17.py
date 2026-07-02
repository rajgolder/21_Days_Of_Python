try:
    # This will raise a TypeError because you cannot add int and str
    print(10 + '5')
except:
    # Catch any exception and print a generic error message
    print("Something went wrong")

try:
    # Prompt user for name and birth year (note: input returns a string)
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    # This will raise a TypeError because year_born is a string
    age = 2026 - year_born
    print(f'You are {name}, and your age is {age}.')
except:
    # Generic fallback for any exception
    print('Something went wrong')

try:
    # Another example demonstrating multiple specific except clauses
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2026 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    # Handle type-related errors (e.g., subtracting string from int)
    print("Type error occured")
except ValueError:
    # Handle value conversion errors
    print("Value error occured")
except ZeroDivisionError:
    # Not applicable here, but shown for demonstration
    print("zero division error occured")

try:
    # Convert input to int before arithmetic to avoid TypeError
    name = input("Enter your name: ")
    year_born = input("Year you born: ")
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    # Handle unexpected type errors
    print("Type error occur")
except ValueError:
    # Handle if the input cannot be converted to int
    print("Value error occur")
except ZeroDivisionError:
    # Included for completeness; not expected here
    print("zero division error occur")
else:
    # Runs if no exception was raised in the try block
    print("I usually run with the try block")
finally:
    # Always runs whether or not an exception occurred
    print("I alway run.")

try:
    # Example using a general Exception catch that prints the exception
    name = input("Enter your name: ")
    year_born = input("Year you born: ")
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    # Print the actual exception message for debugging
    print(e)

def sum_of_five_nums(a, b, c, d, e):
    # Return the sum of five numbers
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# The following call would raise a TypeError because no arguments are provided
print(sum_of_five_nums())

def sum_of_five_nums(a, b, c, d, e):
    # Same function: demonstrate argument unpacking with a list
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# Unpack the list into five positional arguments
print(sum_of_five_nums(*lst))

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(list(numbers))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# Demonstrate iterable unpacking: first three values and the rest
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
# Unpack first, middle (as list), and last element from a list
one, *middle, last = numbers
print(one, middle, last)

def unpacking_person_info(name, country, age):
    return f'{name} lives in {country}. He is {age} year old.'
dct = {'name':'Rek', 'country':'India', 'age':200}
# Demonstrate keyword-argument unpacking from a dict
print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

def packing_person_info(**kwargs):
    # Iterate over keyword args and print key/value pairs
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Rek", country="India", age=200))

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
# Use iterable unpacking to concatenate lists with an additional leading element
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
# Merge two lists of countries using unpacking
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        # Show index where a matching element is found
        print(f'The country {i} has been found at index {index}')

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
# Pair up fruits and vegetables into a list of dicts using zip
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
