# Demonstrate basic while loops and how they control repetition.
count = 0
while count < 5:
    count = count + 1
print(count)

# This while loop prints the current counter value before increasing it.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Use break to exit the loop early when a condition is met.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Use continue to skip the current iteration and move to the next one.
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# Loop through a list and print each element.
numbers = [0, 1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)

# Loop through each character in a string.
language = "Python"
for letter in language:
    print(letter)

# Use range and len to access characters by index.
for i in range(len(language)):
    print(language[i])

# Loop through a tuple and print each value.
numbers = (0, 1, 2, 3, 4, 5, 6)
for number in numbers:
    print(number)

# Create a dictionary and iterate over its keys and values.
person = {
    'first_name': "Rek",
    'last_name': "Nitro",
    'age': 200,
    'country': "India",
    'skills': ["Python", "VS Code", "Github", "AI"]
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

# Loop through a set of company names.
it_companies = {"Facebook", "Google", "Micreosoft", "Apple", "Amazon"}
for company in it_companies:
    print(company)

# Break out of the loop when the value reaches 3.
numbers = (0, 1, 2, 3, 4, 5, 6)
for number in numbers:
    print(number)
    if number == 3:
        break

# Skip the current iteration when the value is 3 and print a message for others.
numbers = (0, 1, 2, 3, 4, 5, 6)
for number in numbers:
    print(number)
    if number == 3:
        continue
    if number != 5:
        print("Next number should be", number + 1)
    else:
        print("Loop's end")
print("Outside of loop")

# Create a list and a set from a range of numbers.
lst = list(range(1, 11))
print(lst)
st = set(range(1, 11))
print(st)

# Create a list and set using a step value of 2.
lst = list(range(0, 11, 2))
print(lst)
st = set(range(0, 11, 2))
print(st)

# Create a descending list using a negative step value.
lst = list(range(11, 0, -2))
print(lst)

# Print numbers from 0 to 10 using range.
for number in range(11):
    print(number)

# Nested loop to print each skill in the person's skills list.
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# A for loop with an else block that runs after the loop completes normally.
for number in range(11):
    print(number)
else:
    print("The loop stops at", number)

# pass acts as a placeholder for code that will be added later.
for number in range(6):
    pass