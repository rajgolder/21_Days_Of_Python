# Question 1: Assign an integer value to a variable
age = 200

# Question 2: Assign a floating-point value to a variable
height = 5.8
# Question 3: Create a complex number
complex_number = 2 + 6j

# Question 4: Calculate the area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is", area)

# Question 5: Find the perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

# Question 6: Calculate the area and perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width:"))
area = length * width
perimeter = 2 * (length + width)
print("Area is", area)
print("Perimeter is", perimeter)

# Question 7: Compute the area and circumference of a circle
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print("Area =", area)
print("Circumference =", circumference)

# Question 8: Understand the line equation y = 2x - 2
# The slope is 2 and the y-intercept is -2
slope1 = 2
y_intercept = -2
# When y = 0, the x-intercept is 1
x_intercept = 1

# Question 9: Find the slope and distance between two points
(x1, y1) = (2, 2)
(x2, y2) = (6, 10)
slope2 = (10 - 2) / (6 - 2)
print(slope2)
distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5

# Question 10: Compare the slopes of two lines
print(slope1 == slope2)

# Question 11: Generate a random number and evaluate a quadratic expression
import random
# The expression y = x^2 + 6x + 9 can be factored as (x + 3)^2
x = random.randint(-10, 10)
print('x is', x)
y = x ** 2 + 6 * x + 9
print('y is', y)

# Question 12: Compare the lengths of two strings
len_p = len('python')
len_d = len('dragon')
print(len_p < len_d)

# Question 13: Check whether 'on' exists in both strings
print('on' in 'python' and 'on' in 'dragon')

# Question 14: Check whether the word 'jargon' appears in a sentence
sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)

# Question 15: Check whether 'on' does not appear in both strings
print('on' not in 'python' and 'on' not in 'dragon')

# Question 16: Convert the length of a string to different data types
length = len("python")
length_float = float(length)
length_string = str(length)
print(length_float)
print(length_string)

# Question 17: Check whether a number is even
num = int(input("Enter a number: "))
print(num % 2 == 0)

# Question 18: Compare integer division with a float conversion
print(7 // 3 == int(2.7))

# Question 19: Compare the types of two values
print(type('10') == type(10))

# Question 20: Compare a rounded float with an integer
print(int(float('9.8')) == 10)

# Question 21: Calculate weekly earnings
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earning = hours * rate
print("Your weekly earning is", earning)

# Question 22: Compute the remaining seconds until the age of 100
current_age = float(input("Enter your current age in years: "))
remaining_years = 100 - current_age
remaining_seconds = remaining_years * 365 * 24 * 60 * 60
print("Remaining seconds to live:", remaining_seconds)

# Question 23: Print a simple pattern using a loop
for i in range(1, 6):
    print(i, 1, i, i ** 2, i ** 3)