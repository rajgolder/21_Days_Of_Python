#single line string
letter = "P"
print(letter)
print(len(letter))
greeting = "Hello World"
print(greeting)
print(len(greeting))
sentence = "Today is day 3 of 30 days of python challenge"
print(sentence)

#multi-line string
multi_line_string = '''I am a student and enjoy learning.
That is why I started the 30 days of python.'''
print(multi_line_string)
#another way of doing
multiline_string = """I am a student and I enjoy learning.
That is why I started the 30 days of python."""
print(multiline_string)

#string concatenation
first_name = "Rek"
last_name = "Nitro"
space = " "
full_name = first_name + space + last_name
print(full_name)
#checking length of a string using len()
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

#unpacking characters
language = "Python"
a, b, c, d, e, f = language #unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#accesiing characters in string by index
language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)  
second_last = language[-6]
print(second_last)

#slicing
language = "Python"
#starts at zero index and up to 3 but not include 3
first_three = language[0 : 3]
print(first_three)
last_three = language[3 : 6]
print(last_three)
#another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)