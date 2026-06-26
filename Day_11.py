# Example: function that prints a full name
def generate_full_name():
    first_name = "Rek"
    last_name = "Nitro"
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


# Call the function to display the result
generate_full_name()

# Example: function that prints the sum of two numbers
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


# Call the function to display the result
add_two_numbers()

# Example: function that returns a full name
def generate_full_name():
    first_name = "Rek"
    last_name = "Nitro"
    space = ' '
    full_name = first_name + space + last_name
    return full_name


# Print the returned value from the function
print(generate_full_name())

# Example: function that returns the sum of two numbers
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


# Print the returned total
print(add_two_numbers())

# Example: function with one parameter and a return value
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message


# Call the function with an argument
print(greetings("Rek"))

# Example: function that adds 10 to a given number
def add_ten(num):
    ten = 10
    return num + ten


# Get input from the user and pass it to the function
print(add_ten(int(input("Enter a number: "))))

# Example: function that returns the square of a number
def square_number(x):
    return x * x


# Print the squared value
print(square_number(2))

# Example: function that calculates the area of a circle
def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area


# Print the calculated area
print(area_of_circle(5))

# Example: function that adds numbers from 0 to n
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


# Print results for different values of n
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Example: function with two parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


# Call the function with two arguments
print("Full name:", generate_full_name("Rek", "Nitro"))

# Example: function that adds two numbers using parameters
def sum_two_numbers(num_one, num_two):
    sum_value = num_one + num_two
    return sum_value


# Print the sum of two numbers
print("Sum of two numbers: ", sum_two_numbers(1, 9))

# Example: function that calculates weight based on mass and gravity
def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + " N"
    return weight


# Print the result in Newtons
print("Weight of an object in Newtons:", weight_of_object(100, 9.81))

# Example: function that prints a full name using keyword arguments
def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


# Pass arguments by name
print_fullname(last_name="Nitro", first_name="Rek")

# Example: function that returns the sum of two numbers using keyword arguments
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


# Pass values using keyword arguments
print(add_two_numbers(num2=3, num1=2))

# Example: function that returns the given first name
def print_name(first_name):
    return first_name


# Print the returned name
print(print_name("Rek"))

# Example: function that returns a full name using keyword arguments
def print_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


# Print the returned full name
print(print_full_name(first_name="Rek", last_name="Nitro"))

# Example: function that adds two values using positional arguments
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


# Call the function with positional arguments
print(add_two_numbers(2, 3))

# Example: function that checks whether a number is even
def is_even(n):
    if n % 2 == 0:
        return True
    return False


# Print the result for even and odd numbers
print(is_even(10))
print(is_even(7))

# Example: function that returns all even numbers up to n
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


# Print the list of even numbers
print(find_even_numbers(10))

# Example: function with a default parameter value
def greetings(name="Peter"):
    message = name + ", welcome to Python for Everyone!"
    return message


# Call the function with and without an argument
print(greetings())
print(greetings("Rek"))

# Example: function with default values for both parameters
def generate_full_name(first_name="Rek", last_name="Nitro"):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


# Print the default and custom full names
print(generate_full_name())
print(generate_full_name("David", "Smith"))

# Example: function that accepts any number of positional arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


# Print the sum of multiple numbers
print(sum_all_nums(2, 3, 5))

# Example: function that accepts a team name and any number of extra values
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


# Call the function with a team name and multiple extra values
generate_groups("Team-1", "Rek", "David", "Brook")

# Example: function that accepts named arguments
def greet(name, location):
    print("Hi there", name, "how is the weather in", location)


# Pass values using keyword arguments
greet(name="Rek", location="India")

# Example: unpacking a dictionary into keyword arguments
my_dict = {"name": "Rek", "location": "India"}
greet(**my_dict)

# Example: function that accepts arbitrary keyword arguments
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)


# Call the function without any keyword arguments
print(arbitrary_named_args())

# Example: function passed as an argument to another function
def square_number(n):
    return n ** n


def do_something(f, x):
    return f(x)


# Call the function using another function as an argument
print(do_something(square_number, 3))