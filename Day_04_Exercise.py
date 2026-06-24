# String concatenation example
s1 = "Twenty"
s2 = "One"
s3 = "Days"
s4 = "of"
s5 = "Python"
result = s1 + '-' + s2 + ' ' + s3 + ' ' + s4 + ' ' + s5
print(result)

# Another string creation example
result2 = "Coding" + ' ' + "For" + ' ' + "All"
print(result2)

# Working with the company string
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

# String transformation methods
print("Capitalize:", company.capitalize())
print("Title:", company.title())
print("Swapcase:", company.swapcase())

# Slicing a string
print(company[7:])

# Checking substring and finding positions
print("Coding" in company)
print("Index:", company.index("Coding"))
print("Find:", company.find("Coding"))

# Replacing text in a string
print(company.replace("Coding", "Python"))

# Replacing a word in another text
text = "Python For Everyone"
print(text.replace("Everyone", "All"))

# Splitting a string into parts
print(company.split())

companies = "Facebook, Google, Microsoft, Apple, Amazon"
print(companies.split(","))

# Accessing characters by index
print(company[0])
print(len(company) - 1)
print(company[10])

# Creating an acronym from words
text2 = "Python For Everyone"
acronym = ''.join(word[0] for word in text2.split())
print(acronym)

text3 = "Coding For All"
acronym2 = ''.join(word[0] for word in text3.split())
print(acronym2)

# Finding the index of characters in the string
print(company.index("C"))
print(company.index("F"))

# Finding the last occurrence of a character
text4 = "Coding For All"
print(text4.rfind("l"))

# Searching for a word in a sentence
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
print(sentence.rindex("because"))

# Extracting a substring between two occurrences
start = sentence.find("because")
end = sentence.rfind("because") + len("because")
print(sentence[start:end])

# Checking string prefixes and suffixes
print(company.startswith("Coding"))
print(company.endswith("Coding"))

# Removing extra spaces from both ends
spaced = "  Coding For All     "
print(spaced.strip())

# Validating identifier names
print("21DaysOfPython".isidentifier())
print("Twenty_One_Days_Of_Python".isidentifier())

# Joining list items into a single string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

# Using escape sequences in strings
print("I am enjoying this challenge.\nI just wonder what is next.")

# Tab-separated output example
print("Name\tAge\tCountry")
print("Rek\t200\tIndia")

# Calculating the area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")

# Arithmetic operations with formatted output
x = 8
y = 6
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y:.2f}")
print(f"{x} % {y} = {x%y}")
print(f"{x} // {y} = {x//y}")
print(f"{x} ** {y} = {x**y}")