# Example 1: Check whether a number is positive
a = 3
if a > 0:
    print("A is a positive number")

# Example 2: Check whether a number is negative or positive
a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")

# Example 3: Check whether a number is positive, negative, or zero
a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

# Example 4: Use a short conditional expression
a = 2
print("A is positive") if a > 0 else print("A is negative")

# Example 5: Check if a number is positive, even, zero, or negative
a = 4
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

# Example 6: Check whether a number is even, odd, zero, or negative
a = 7
if a > 0 and a % 2 == 0:
    print("A is a even and positive number")
elif a > 0 and a % 2 != 0:
    print("A is a odd and positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")

# Example 7: Check user access using logical operators
user = "Rek"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted")
else:
    print("Access denied")