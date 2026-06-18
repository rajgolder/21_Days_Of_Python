# Example: creating and printing a single-line string
letter = "P"
print(letter)
print(len(letter))
greeting = "Hello World"
print(greeting)
print(len(greeting))
sentence = "Today is day 3 of 30 days of python challenge"
print(sentence)

# Example: creating and printing multi-line strings
multi_line_string = """I am a student and enjoy learning.
That is why I started the 30 days of python."""
print(multi_line_string)
# Another way to write a multi-line string
multiline_string = """I am a student and I enjoy learning.
That is why I started the 30 days of python."""
print(multiline_string)

# Example: combining strings using concatenation
first_name = "Rek"
last_name = "Nitro"
space = " "
full_name = first_name + space + last_name
print(full_name)
# Example: checking string length with len()
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Example: unpacking characters from a string
language = "Python"
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Example: accessing characters by index and using negative indexing
language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# We can also access characters from the end using negative indices
language = "Python"
last_letter = language[-1]
print(last_letter)
second_last = language[-6]
print(second_last)

# Example: slicing strings and skipping characters
language = "Python"
# Start at index 0 and stop before index 3
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
# Another way to slice from the end
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Example: skipping characters while slicing a string
language = "Python"
pto = language[0:6:2]  # Start at index 0, stop before index 6, move by 2 positions each time
print(pto)

# Example: using escape sequences in strings
print("I hope I can learn python.\nAnd you?")
print("Days\tTopics\tExercises")
print("Day1\t1\t3")
print("Day2\t3\t4")
print("Day3\t2\t5")
print("Day4\t3\t5")
print("THis is a back slash symbol (\\)")
print("In every programing language it starts with \"Hello World\"")

# Example: using built-in string methods
# capitalize(): converts the first character of the string to a capital letter
challenge = "thrity days of python"
print(challenge.capitalize())

# count(): returns the number of occurrences of a substring
print(challenge.count("y"))
print(challenge.count("y", 7, 14))
print(challenge.count("th"))

# endswith(): checks whether a string ends with a specified suffix
challenge = "thirty day of python"
print(challenge.endswith("on"))
print(challenge.endswith("tion"))

# expandtabs(): replaces tab characters with spaces
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): returns the index of the first occurrence of a substring
challenge = "thirty days of python"
print(challenge.find("y"))
print(challenge.find("th"))

# format(): formats a string into a clearer output
first_name = "Rek"
last_name = "Nitro"
job = "Student"
sentence = "I am {} {}. I am a {}.".format(
    first_name, last_name, job
)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = "The area of circle with radius {} is {}".format(str(radius), str(area))
print(result)

# index(): returns the index of a substring
challenge = "thirty day of python"
print(challenge.index("y"))
print(challenge.index("th"))

# isalnum(): checks whether the string is alphanumeric
challenge = "thirty days of python"
print(challenge.isalnum())

challenge = "thirtydaysofpython"
print(challenge.isalnum())

challenge = "30 days of python"
print(challenge.isalnum())

challenge = "30daysofpython"
print(challenge.isalnum())

# isalpha(): checks if all characters are alphabetic
challenge = "thirty days of python"
print(challenge.isalpha())
num = "1234"
print(num.isalpha())

# isdigit(): checks whether all characters are digits
challenge = "Thirty"
print(challenge.isdigit())
challenge = "30"
print(challenge.isdigit())

# isdecimal(): checks whether the string contains decimal characters
num = "10"
print(num.isdecimal())  # True
num = "10.5"
print(num.isdecimal())  # False


# isidentifier(): checks whether a string is a valid variable name
challenge = "30DaysOfPython"
print(challenge.isidentifier())
challenge = "thirty_days_of_python"
print(challenge.isidentifier())


# islower(): checks if all alphabetic characters are lowercase
challenge = "thirty days of python"
print(challenge.islower())
challenge = "Thirty days of python"
print(challenge.islower())

# isupper(): checks if all alphabetic characters are uppercase
challenge = "thirty days of python"
print(challenge.isupper())
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())


# isnumeric(): checks whether the string is numeric
num = "10"
print(num.isnumeric())
print("ten".isnumeric())

# join(): joins elements of a list into a single string
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = "#, ".join(web_tech)
print(result)

# strip(): removes both leading and trailing characters
challenge = " thirty days of python "
print(challenge.strip("y"))

# replace(): replaces a substring inside a string
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))

# split(): splits a string into a list of words
challenge = "thirty days of python"
print(challenge.split())

# title(): returns a title-cased version of the string
challenge = "thirty days of python"
print(challenge.title())

# swapcase(): swaps the case of each character
challenge = "thirty days of python"
print(challenge.swapcase())
challenge = "Thirty Days Of Python"
print(challenge.swapcase())

# startswith(): checks if a string starts with a specified prefix
challenge = "thirty days of python"
print(challenge.startswith("thirty"))
challenge = "30 days of python"
print(challenge.startswith("thirty"))
