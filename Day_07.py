# Create an empty set
st = set()
print(st)

# Create a set with initial values
st = {'item1', 'item2', 'item3', 'item4'}
print(st)

# Create another set of fruits
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

# Find the number of items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# Check whether an item exists in a set
st = {'item1', 'item2', 'item3', 'item4'}
print('Does set contain item3?', 'item3' in st)

# Check membership in another set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Does set contain mango?', 'mango' in fruits)

# Add a new item to a set
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)

# Add a new fruit to the set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

# Update a set with multiple values
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
print(st)

# Update one set with values from another set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Remove a specific item from a set
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

# Remove and return an arbitrary item from a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
print(fruits)

# Clear all items from a set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

# Delete the set variable entirely
st = {'item1', 'item2', 'item3', 'item4'}
del st

# Convert a list to a set to remove duplicates
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
print(lst)
st = set(lst)
print(st)

# Combine two sets using union
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item15', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# Find common elements between sets using intersection
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st1.intersection(st2))

# Find common values between two number sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

# Check whether one set is a subset of another
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.issubset(st1))

# Check whether one set is a superset of another
print(st2.issuperset(st2))

# Find items present in one set but not the other
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.difference(st1))
print(st1.difference(st2))

# Find elements that are in one set or the other, but not both
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.symmetric_difference(st1))

# Find symmetric difference for number sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

# Check whether two sets share any common elements
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))

# Check whether two number sets are disjoint
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))