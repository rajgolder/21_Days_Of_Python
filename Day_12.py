# Demonstrating various ways to import and use modules in Python

# Importing an entire module and accessing its attributes
import mymodule
print(mymodule.generate_full_name("Rek", "Nitro"))

# Importing specific functions and variables from a module
from mymodule import generate_full_name, sum_two_num, person, gravity
print(generate_full_name("Rek", "Nitro"))
print(sum_two_num(3,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['first_name'])

# Importing with aliases for brevity
from mymodule import generate_full_name as fullname, sum_two_num as total, person as p, gravity as g
print(fullname("Rek", "Nitro"))
print(total(4,8))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['first_name'])

# Importing all functions from a module (use with caution)
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# Importing the standard math module
import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2, 3)) 
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

# Importing a specific function with an alias
from math import pi as  PI
print(PI)

# Importing the string module for useful constants
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation) 

# Importing the random module for generating random numbers
import random
print(random.random())
print(random.randint(1, 10))