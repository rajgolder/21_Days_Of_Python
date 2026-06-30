# 📘 Day 6: Tuples (Revision Notes)

## What is a Tuple?
- Ordered collection of items.
- **Immutable** (cannot be changed after creation).
- Allows duplicate values.
- Can store different data types.
- Written using **parentheses `()`**.

---

# Creating Tuples
- Empty tuple: `()`
- Using `tuple()`
- Tuple with values: `(item1, item2, item3)`

---

# Tuple Methods
| Method | Purpose |
|---------|---------|
| `tuple()` | Create a tuple |
| `count()` | Count occurrences of an item |
| `index()` | Find index of an item |
| `+` | Join tuples |

> Tuples have very few methods because they are immutable.

---

# Length
- Use `len()` to find the number of elements.

---

# Accessing Items
### Positive Indexing
- Starts from `0`.
- First item → `0`
- Last item → `len(tuple)-1`

### Negative Indexing
- Starts from the end.
- Last item → `-1`
- Second last → `-2`

---

# Slicing
- Extract a portion of a tuple.
- Returns a **new tuple**.
- Supports both positive and negative indexing.

---

# Converting Between Tuple and List
### Tuple → List
- Use `list()` when modifications are needed.

### List → Tuple
- Use `tuple()` after making changes.

---

# Membership Test
- Use the `in` operator.
- Returns `True` or `False`.

---

# Joining Tuples
- Use the `+` operator.
- Creates a new tuple.

---

# Deleting Tuples
- Individual items **cannot** be deleted.
- Entire tuple can be deleted using `del`.

---

# Tuple Characteristics (Important)

✅ Ordered

✅ Immutable

✅ Allows duplicates

✅ Supports indexing and slicing

✅ Can store multiple data types

❌ Cannot add, remove, or modify elements after creation

---

# Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| Mutable | ❌ No | ✅ Yes |
| Syntax | `()` | `[]` |
| Ordered | ✅ | ✅ |
| Duplicates | ✅ | ✅ |
| Faster | ✅ | ❌ |
| Methods | Few | Many |

---

# Commonly Used Functions

- `len()` → Number of elements
- `count()` → Count occurrences
- `index()` → Find position
- `list()` → Convert tuple to list
- `tuple()` → Convert list to tuple

---

# Exam Tips

- Tuples are **immutable**.
- Slicing always creates a **new tuple**.
- Use **positive** or **negative indexing** to access elements.
- Convert to a **list** if you need to modify values.
- `+` joins tuples and returns a new tuple.

---

# Memory Trick

**Tuple = Temporary Lock 🔒**

- `()` → Locked (cannot change)
- `[]` → Flexible (can change)

Remember:
> **Lists are editable, Tuples are fixed.**