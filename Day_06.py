# Create an empty tuple
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

# Create tuples with initial values
tpl = ('items1', 'item2', 'item3')
print(tpl)
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

# Find the length of a tuple
tpl = ('items1', 'item2', 'item3')
print(len(tpl))

# Access tuple items using positive indexing
tpl = ('items1', 'item2', 'item3')
frist_item = tpl[0]
print(frist_item)
second_item = tpl[1]
print(second_item)
last_index = len(tpl) - 1
last_item = tpl[last_index]
print(last_item)

# Access tuple items using negative indexing
tpl = ('items1', 'item2', 'item3')
first_item = tpl[-3]
print(frist_item)
second_item = tpl[-2]
print(second_item)

# Slice tuples to get a range of items
tpl = ('items1', 'item2', 'item3', 'item4', 'item5')
all_items = tpl[0:5]
print(all_items)
all_items = tpl[0:]
print(all_items)
middle_two_itms = tpl[1:3]
print(middle_two_itms)

# Slice tuples using negative indices
tpl = ('items1', 'item2', 'item3', 'item4', 'item5')
all_items = tpl[-5:]
print(all_items)
middle_two_itms = tpl[-3:-1]
print(middle_two_itms)

# Convert tuples to lists and back to tuples
tpl = ('items1', 'item2', 'item3', 'item4')
lst = list(tpl)
print(tpl)
print(lst)
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Check whether an item exists in a tuple
tpl = ('items1', 'item2', 'item3', 'item4')
print('item2' in tpl)
fruits = ('banana', 'orange', 'mango', 'lemon')
print('apple' in fruits)
print('orange' in fruits)

# Join two tuples together
tpl1 = ('items1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl + tpl2
print(tpl3)
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Delete a tuple from memory
tpl = ('items1', 'item2', 'item3', 'item4', 'item5')
del tpl