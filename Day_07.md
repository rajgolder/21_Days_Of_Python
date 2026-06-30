# 📘 Day 7: Sets (Revision Notes)

## What is a Set?
- Unordered collection of **unique** elements.
- Does **not** allow duplicate values.
- Unindexed (cannot access items using indexes).
- Mutable (items can be added or removed).
- Written using **curly braces `{}`**.
- Empty set is created using **`set()`**, not `{}` (`{}` creates a dictionary).

---

# Creating Sets
- Empty set → `set()`
- Set with values → `{item1, item2, item3}`

---

# Set Characteristics

✅ Unordered

✅ Unique elements only

✅ Mutable (can add/remove items)

❌ No indexing

❌ No duplicate values

---

# Length
- Use `len()` to find the number of unique elements.

---

# Accessing Items
- Sets are **not indexed**.
- Access elements by looping through the set.

---

# Membership Test
- Use the `in` operator.
- Returns `True` or `False`.

---

# Adding Items

| Method | Purpose |
|---------|---------|
| `add()` | Add a single item |
| `update()` | Add multiple items |

---

# Removing Items

| Method | Purpose |
|---------|---------|
| `remove()` | Removes item (raises error if not found) |
| `discard()` | Removes item (no error if not found) |
| `pop()` | Removes a random item |
| `clear()` | Removes all items |
| `del` | Deletes the entire set |

---

# Converting Between List and Set

### List → Set
- Removes duplicate values automatically.

### Set → List
- Use when indexing or ordering is needed.

---

# Set Operations

## Union
- Combines all unique elements from both sets.

Methods:
- `union()`
- `|`

---

## Intersection
- Returns common elements.

Methods:
- `intersection()`
- `&`

---

## Difference
- Returns elements present in the first set but not in the second.

Methods:
- `difference()`
- `-`

---

## Symmetric Difference
- Returns elements that are in either set, but **not both**.

Methods:
- `symmetric_difference()`
- `^`

---

# Subset & Superset

| Method | Meaning |
|---------|---------|
| `issubset()` | Checks if one set is contained in another |
| `issuperset()` | Checks if one set contains another |

---

# Disjoint Sets
- Two sets with **no common elements**.

Method:
- `isdisjoint()`

---

# Commonly Used Methods

| Method | Purpose |
|---------|---------|
| `add()` | Add one item |
| `update()` | Add multiple items |
| `remove()` | Remove item (error if missing) |
| `discard()` | Remove item (no error) |
| `pop()` | Remove random item |
| `clear()` | Empty the set |
| `union()` | Combine sets |
| `intersection()` | Common elements |
| `difference()` | Unique elements of first set |
| `symmetric_difference()` | Non-common elements |
| `issubset()` | Subset check |
| `issuperset()` | Superset check |
| `isdisjoint()` | Check for no common elements |

---

# Operators Cheat Sheet

| Operator | Meaning |
|----------|---------|
| `in` | Membership test |
| `|` | Union |
| `&` | Intersection |
| `-` | Difference |
| `^` | Symmetric Difference |

---

# Set vs List

| Feature | Set | List |
|---------|-----|------|
| Ordered | ❌ No | ✅ Yes |
| Indexed | ❌ No | ✅ Yes |
| Duplicates | ❌ No | ✅ Yes |
| Mutable | ✅ Yes | ✅ Yes |
| Unique Values | ✅ Yes | ❌ No |

---

# Exam Tips

- Sets automatically remove duplicate values.
- Sets are **unordered**, so item order is not guaranteed.
- Use `set()` for an empty set (`{}` creates a dictionary).
- `remove()` raises an error if the item doesn't exist.
- `discard()` does not raise an error.
- `pop()` removes a **random** item.
- Use set operations (`|`, `&`, `-`, `^`) for mathematical set calculations.

---

# Memory Trick

**SET = Store Every Thing Once**

- **S** → Store unique values
- **E** → Eliminate duplicates
- **T** → Think mathematical operations (Union, Intersection, Difference)

Remember:

> **List = Ordered Collection 📋**  
> **Tuple = Locked Collection 🔒**  
> **Set = Unique Collection 🎯**