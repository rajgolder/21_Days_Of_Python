# Create an empty dictionary
empty_dict = {}

# Create a sample dictionary with key-value pairs
dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Create a dictionary for a person with multiple fields
person = {
    'first_name': 'Rek',
    'last_name': 'Nitro',
    'age': 200,
    'country': 'India',
    'is_married': False,
    'skills': ['Python', 'Github', 'AI'],
}

# Check the number of items in a dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(len(dct))

# Find the length of the person dictionary
print(len(person))

# Access dictionary items using their keys
print(dct['key1'])
print(dct['key4'])

# Access values from the person dictionary
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['country'])
print(person['is_married'])
print(person['skills'])
print(person['skills'][0])

# Use the get() method to access values safely
print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

# Add a new key-value pair to the dictionary
dct['key5'] = 'value5'
print(dct)

# Add a new field to the person dictionary
person['job_title'] = 'Student'
print(person)

# Modify an existing value in a dictionary
dct['key1'] = 'value-one'
print(dct)

# Change the first name in the person dictionary
person['first_name'] = 'Raj'
print(person)

# Check whether a key exists in the dictionary
print('key2' in dct)
print('key5' in dct)

# Remove items from a dictionary
dct.pop('key1')
print(dct)

# popitem() removes the last inserted key-value pair
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()
print(dct)

# del removes a specific key-value pair from the dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct['key2']
print(dct)

# Convert a dictionary into a list of its items
# This returns a list-like object of key-value pairs
print(dct.items())

# Clear all key-value pairs from a dictionary
# After clearing, the dictionary becomes empty
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.clear())

# Delete the dictionary object completely
del dct

# Copy a dictionary to create a duplicate
# The copy is independent of the original dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()

# Get the dictionary keys as a list
keys = dct.keys()
print(keys)

# Get the dictionary values as a list
values = dct.values()
print(values) 