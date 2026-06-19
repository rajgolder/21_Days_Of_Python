# List of fruits
fruits = ["banana", "orange", "mango", "lemon"]
# List of vegetables
vegetables = ["tomato", "potato", "cabbage", "onion", "carrot"]
# List of animal products
animal_products = ["milk", "meat", "butter", "yogurt"]
# List of web technologies
web_tech = ["HTML", "CSS", "React", "Redux", "Node", "MongDB"]
# List of countries
countries = ["Finland", "India", "Denmark", "Sweden"]

# Print each list and its length
print("Fruits:", fruits)
print("Number of fruits:", len(fruits))
print("Vegetables", vegetables)
print("Number of vegetables", len(vegetables))
print("Animal products:", animal_products)
print("Number of animal products:", len(animal_products))
print("Web technologies:", web_tech)
print("Number of web technologies:", len(web_tech))
print("Countries:", countries)
print("Number of countries:", len(countries))

# Accessing items by index
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
# Accessing the last item using its index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

# Accessing items using negative indexing
fruits = ["banana", "orange", "mango", "lemon"]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)
print(second_last)

# Slicing a list to get a subset of items
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]
print(all_fruits)
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
print(orange_and_mango)
print(orange_mango_lemon)

# Modifying items in a list
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)
fruits[1] = "apple"
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)

# Checking whether an item exists in a list
fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)

# Adding items to the end of a list
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

# Inserting items at a specific position
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")
print(fruits)
fruits.insert(3, "lime")
print(fruits)

# Removing an item by value
fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("banana")
print(fruits)
fruits.remove("lemon")
print(fruits)

# Deleting an item by index
fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)

# Clearing all items from a list
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)

# Copying a list so the original remains unchanged
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining lists using the + operator
positive_numbers = [1, 2, 3, 4, 5, 6]
zero = [0]
negative_numbers = [-6, -5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["tomato", "potato", "cabbage", "onion", "carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Extending one list with another list
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers:", num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers:", negative_numbers)

# Counting occurrences of an item
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))
ages = (22, 19, 24, 25, 26, 24, 25, 24)
print(ages.count(24))

# Finding the index of an item
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))
ages = (22, 19, 24, 25, 26, 24, 25, 24)
print(ages.index(24))

# Reversing the order of items
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# Sorting items in ascending and descending order
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)