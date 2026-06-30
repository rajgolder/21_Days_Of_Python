# 📘 Day 5 Revision Notes

# Lists

- A **list** is an **ordered**, **mutable (changeable)** collection.
- Lists allow **duplicate** elements.
- Lists can store **different data types**.
- Created using:
  - `[]`
  - `list()`

---

# Collection Types Comparison

| Type | Ordered | Mutable | Duplicates |
|------|---------|---------|------------|
| List | ✅ | ✅ | ✅ |
| Tuple | ✅ | ❌ | ✅ |
| Set | ❌ | ✅ | ❌ |
| Dictionary | ✅ (Py 3.7+) | ✅ | Keys ❌ |

---

# Creating Lists

- Empty list
- List with values
- Mixed data type list

Use `len()` to find the number of items.

---

# Accessing List Items

## Positive Indexing

- Starts from `0`

Example:
- First item → `0`
- Second item → `1`

---

## Negative Indexing

- Starts from the end

Example:
- Last item → `-1`
- Second last → `-2`

---

# Unpacking Lists

Assign list items directly to variables.

- Use `*` to collect remaining items.

Example pattern:

```
first, second, *rest
```

---

# List Slicing

General syntax:

```
list[start:end:step]
```

### Common Slices

- First few items
- Last few items
- Entire list
- Every second item
- Reverse list

---

# Modifying Lists

Lists are **mutable**.

You can:
- Change values
- Replace items
- Update elements using their index

---

# Checking Items

Use:

```
in
```

Returns:
- `True`
- `False`

---

# Adding Items

## `append()`

- Adds one item at the end.

---

## `insert(index, item)`

- Inserts item at a specific position.
- Existing items shift right.

---

# Removing Items

## `remove(item)`

- Removes the **first occurrence** of an item.

---

## `pop()`

- Removes and returns:
  - Last item (default)
  - Specified index

---

## `del`

- Deletes:
  - Single item
  - Range of items
  - Entire list

---

## `clear()`

- Removes all items.
- List becomes empty.

---

# Copying Lists

## `copy()`

Creates a separate copy.

**Important**

```
list2 = list1
```

does **not** create a new list.

Both variables reference the same list.

---

# Joining Lists

## `+`

Creates a new combined list.

---

## `extend()`

Adds another list to the existing list.

Difference:

- `+` → New list
- `extend()` → Modifies original list

---

# Useful List Methods

| Method | Purpose |
|---------|---------|
| `append()` | Add at end |
| `insert()` | Add at index |
| `remove()` | Remove by value |
| `pop()` | Remove by index |
| `clear()` | Empty list |
| `copy()` | Copy list |
| `extend()` | Merge lists |
| `count()` | Count occurrences |
| `index()` | Find first occurrence |
| `reverse()` | Reverse list |
| `sort()` | Sort original list |

---

# Sorting Lists

## `sort()`

- Modifies original list.
- Ascending by default.
- Use `reverse=True` for descending.

---

## `sorted()`

- Returns a **new sorted list**.
- Original list remains unchanged.

---

# Important Differences

## `append()` vs `insert()`

| append() | insert() |
|-----------|----------|
| Adds at end | Adds at specific index |

---

## `remove()` vs `pop()`

| remove() | pop() |
|-----------|-------|
| Removes by value | Removes by index |
| No return value | Returns removed item |

---

## `sort()` vs `sorted()`

| sort() | sorted() |
|---------|----------|
| Modifies original list | Returns new sorted list |
| No new list | Original unchanged |

---

## `+` vs `extend()`

| `+` | `extend()` |
|------|------------|
| Creates new list | Modifies existing list |

---

# Important Points to Remember

- Lists are mutable.
- Indexing starts at `0`.
- Negative indexing starts at `-1`.
- Lists can contain mixed data types.
- Lists allow duplicates.
- Slicing returns a new list.
- `append()` adds one item.
- `extend()` adds multiple items.
- `remove()` removes by value.
- `pop()` removes by index.
- `copy()` creates a separate list.
- `sort()` changes the original list.
- `sorted()` returns a new sorted list.

---

# Quick Revision Checklist ✅

- List creation
- Collection types
- Positive indexing
- Negative indexing
- Unpacking
- Slicing
- Modify items
- `in` operator
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `del`
- `clear()`
- `copy()`
- `+`
- `extend()`
- `count()`
- `index()`
- `reverse()`
- `sort()`
- `sorted()`
- `append()` vs `insert()`
- `remove()` vs `pop()`
- `sort()` vs `sorted()`
- `+` vs `extend()`