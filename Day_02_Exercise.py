# Day 2: 21 Days of Python programming

# Define variables of different data types
first_name = "Rek"
last_name = "Nitro"
full_name = first_name + last_name
country = 'India'
age = 200
is_married = False
is_true = True
is_light_on = True

# Assign multiple variables in one line
x, y, z = 20, 40, 60

# Print the data type of each variable
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Print the length of the first and last names
print(len(first_name))
print(len(last_name))

# Compare the length of the first and last names
if len(first_name) > len(last_name):
    print('First name is longer')
elif len(first_name) < len(last_name):
    print('Last name is longer')
else:
    print('Both have the same length')

# Perform basic arithmetic operations
num_one = 22
num_two = 44
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_two / num_two
print(division)
reminder = num_two % num_one
print(reminder)
exponent = num_one ** num_two
print(exponent)
floor_division = num_one // num_two
print(floor_division)

# Calculate the area and circumference of a circle
pi = 3.12
radius = 20
area = pi * radius ** 2
print(area)
circum = 2 * pi * radius
print(circum)

# Take user input for the radius and calculate its area
radius = float(input('Enter radius: '))
area = 3.14 * radius ** 2
print(area)

# Take user input for personal details
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = input("Enter age: ")
print(first_name, last_name)
print(age)

# Display Python keywords
help("keywords")