# Exercises: Level 1
# 1. Declare an empty list
emoty_list =[]

# 2. Declare a list with more than 5 items
fruits = ['apple', 'mango', 'orange', 'grapes', 'lemon']

# 3. Find the length of your list
print(len(fruits))

# 4. Get the first item, the middle item and the last item of the list
print(fruits[0])
print(fruits[len(fruits)//2])
print(fruits[len(fruits) - 1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = [
    "Raj",
    19,
    "Single",
    "India"
]
print(mixed_data_type)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"

]

# 7. Print the list using _print()_
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "Nvidia")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 13. Change one of the it_companies names to lowercase (IBM excluded!)
it_companies[3] = it_companies[3].lower()
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.
print("Microsoft" in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
middle = len(it_companies)//2

print(it_companies[middle])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(middle)
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
#    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#    back_end = ['Node','Express', 'MongoDB']
front_end = ["HTML","CSS", "JS", "React", "Rust"]
back_end = ["Node", "Express", "MongoDB"]
full_stack = front_end + back_end
print(full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = full_stack.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# Exercises: Level 2
# 1. The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# - Sort the list and find the min and max age
# - Add the min age and the max age again to the list
# - Find the median age (one middle item or two middle items divided by two)
# - Find the average age (sum of all items divided by their number )
# - Find the range of the ages (max minus min)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)

print(min(ages))
print(max(ages))

length = len(ages)
if length % 2 ==0:
    median = (ages[length//2]+ages[length//2-1])/2
else:
    median = ages[length//2]
print(median)

average = sum(ages)/len(ages)
print(average)

age_range = max(ages) - min(ages)
print(age_range)

print(abs(min(ages) - average))
print(abs(max(ages) - average))

# 2. Find the middle country(ies) in the [countries list]
countries = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark"
]

middle = len(countries)//2
print(countries[middle])

half = len(countries)//2
first_half = countries[:half+1]
second_half = countries[half+1:]
print(first_half)
print(second_half)

first, second, third, *scandic = countries
print(first)
print(second)
print(third)

print(scandic)
