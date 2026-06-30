# This file shows common Python mistakes and their fixes.
# The goal is to understand why an error happens and how to correct it.

# Example 1: Python 3 requires parentheses in print().
# Wrong: print without parentheses is invalid in Python 3.
print 'hello world'

# Correct: use parentheses with print().
print('hello world')

# Example 2: Variables must be defined before using them.
# Wrong: age is used before it is assigned, so Python raises NameError.
print(age)

# Correct: assign a value first, then print it.
age = 20
print(age)

# Example 3: List index must be within the valid range.
# Wrong: numbers has indices 0 to 4, so index 5 is out of range.
numbers = [1, 2, 3, 4, 5,]
print(numbers[5])

# Correct: use a valid index, such as 4 for the last element.
numbers = [1, 2, 3, 4, 5,]
print(numbers[4])

# Example 4: Importing the same module multiple times is unnecessary.
# This is allowed, but it does not create a new import.
import math
import math

# Example 5: Use the correct constant from the math module.
# Wrong: math.PI does not exist in Python's math module.
import math
math.PI

# Correct: use math.pi for the constant value of pi.
import math
math.pi

# Example 6: Dictionary keys must be spelled correctly.
# Wrong: 'county' is not a key in the dictionary.
users = {'name':'Rek', 'age':20, 'country':'India'}
print(users['name'])
print(users['county'])

# Correct: use the correct key 'country'.
print(users['country'])

# Example 7: Do not mix different data types in arithmetic.
# Wrong: '3' is a string, so 4 + '3' causes a TypeError.
print(4 + '3')

# Correct: convert the string to an integer before adding.
print(4 + int('3'))

# Example 8: Import the correct function name from the math module.
# Wrong: 'power' is not available in the math module.
from math import power

# Correct: use 'pow' for power calculation.
from math import pow

# Example 9: Convert only valid numeric strings.
# Wrong: '12a' cannot be converted to an integer.
int('12a')

# Example 10: Avoid division by zero.
# Wrong: dividing by zero raises ZeroDivisionError.
1/0