st = set()
print(st)

st = {'item1', 'item2', 'item3', 'item4'}
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)


fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

st = {'item1', 'item2', 'item3', 'item4'}
print('Does set contain item3?', 'item3' in st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Does set contain mango?', 'mango' in fruits)


st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)


st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)


st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
print(fruits)


st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

st = {'item1', 'item2', 'item3', 'item4'}
del st


lst = ['item1', 'item2', 'item3', 'item4', 'item1']
print(lst)
st = set(lst)
print(st)


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item15', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st1.intersection(st2))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.issubset(st1))
print(st2.issuperset(st2))


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.difference(st1))
print(st1.difference(st2))


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.symmetric_difference(st1))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))