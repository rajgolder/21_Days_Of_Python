#arithmetic operation in python
#integers

print("Addition:", 1 + 2)
print("Subtraction:", 2 - 1)
print("Multiplication:", 2 * 3)
#division in python given floating number
print("Division:", 4 / 2)
print("Divesion:", 7 / 2)
#gives without the floating number or without the remainder
print("Division without the reminder:", 7 // 2)
print("Modulus:", 7 % 2) #gives the reminder
print("Exponential:", 3 ** 2) # it means 3 to the power of 2

#floating numbers
print("Floating nuber, PI:", 3.14)
print("Floating numbe, gravity:", 9.81)

#complex number
print("Complex number:", 1 + 1j)
print("Multiplying complex number:", (1+1j) * (1-1j))

#declaring the variable at the top first
a = 3
b = 2
#arithmetic operation and assigning the result to a variable
add = a + b
diff = a - b
product = a * b
reminder = a % b
division = a / b
floor_division = a // b
exponential = a ** b

print("a + b =", add)
print("a - b =", diff)
print("a * b =", product)
print("a / b =", division)
print("a % b =", reminder)
print("a // b =", floor_division)
print("a ** b =", exponential)

#declaring values and organizing them together
num_one = 3
num_two = 4

#operation
add = num_one + num_two
diff = num_one - num_two
prodict = num_one * num_two
div = num_one / num_two
reminder = num_one % num_two

#print
print("Total:", add)
print("Difference:", diff)
print("Product:", product)
print("Division:", div)
print("Reminder:", reminder)

#calculating the area of a cicle
radius = 10
area_of_circle = 3.14 * radius ** 2
print("Area of circle:", area_of_circle)

#calculating the area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of rectangle:", area_of_rectangle)

#calculating the weight of an object
mass = 75
gravity = 9.81
weigth = mass * gravity
print("Weight:", weigth, "N")

print(3 > 2) #true, because 3 is greater than 2
print(3 >= 2) #true, because 3 is greater than 2
print(3 < 2) #false, because 3 is greater than 2
print(2 < 3) #true, because 2 is less than 3
print(2 <= 3) #true, because 2 is less than 3
print(3 == 2) #false, because 3 is not equal to 2
print(3 != 2) #true, because 3 is not equal to 2

#boolen comparison
print("True == True:", True == True)
print("True == False:", True == False)
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)

#another way of comparison
print("1 is 1", 1 is 1)
print("1 is not 2", 1 is not 2)
print("R in Rek", "R" in "Rek")
print("E in Rek", "E" in "Rek")
print("coding" in "coding for all")
print("a in an", "a" in "an")
print("4 is 2 ** 2", 4 is 2 ** 2)

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False