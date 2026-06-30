# 📘 Day 8: Dictionaries (Revision Notes)

## What is a Dictionary?
- Stores data as **key : value** pairs.
- Mutable (modifiable).
- Keys are unique.
- Values can be of any data type.
- Written using **curly braces `{}`** or `dict()`.

---

# Creating Dictionaries
- Empty dictionary → `{}`
- Using `dict()`
- Dictionary with key-value pairs.

---

# Dictionary Characteristics

✅ Stores data as **key : value**

✅ Mutable (can add, update, remove items)

✅ Keys must be unique

✅ Values can be duplicated

✅ Fast lookup using keys

---

# Length
- Use `len()` to count the number of **key-value pairs**.

---

# Accessing Values

| Method | Description |
|---------|-------------|
| `dict[key]` | Returns value (raises error if key doesn't exist) |
| `get(key)` | Returns value or `None` if key doesn't exist |

> Prefer `get()` when you're unsure whether a key exists.

---

# Adding Items
- Add a new **key-value pair** by assigning a value to a new key.

---

# Modifying Items
- Assign a new value to an existing key.

---

# Checking Keys
- Use the `in` operator to check whether a key exists.

---

# Removing Items

| Method | Purpose |
|---------|---------|
| `pop(key)` | Removes specified key |
| `popitem()` | Removes the last inserted item |
| `del` | Deletes a specific key or the entire dictionary |
| `clear()` | Removes all items |

---

# Copying Dictionaries
- Use `copy()` to create a duplicate dictionary.
- Changes to the copy won't affect the original.

---

# Dictionary Views

| Method | Returns |
|---------|----------|
| `keys()` | All keys |
| `values()` | All values |
| `items()` | Key-value pairs as tuples |

---

# Commonly Used Methods

| Method | Purpose |
|---------|---------|
| `get()` | Safe value lookup |
| `keys()` | Get all keys |
| `values()` | Get all values |
| `items()` | Get key-value pairs |
| `pop()` | Remove specific key |
| `popitem()` | Remove last item |
| `clear()` | Empty dictionary |
| `copy()` | Copy dictionary |

---

# Dictionary vs List vs Tuple vs Set

| Feature | Dictionary | List | Tuple | Set |
|---------|------------|------|-------|-----|
| Ordered | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| Mutable | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| Indexed | ❌ By key | ✅ | ✅ | ❌ |
| Duplicate Values | ✅ | ✅ | ✅ | ❌ |
| Unique Keys | ✅ | ❌ | ❌ | Elements are unique |

---

# Exam Tips

- Dictionaries store data as **key : value** pairs.
- Keys must be **unique**.
- Use `get()` instead of `[]` to avoid errors for missing keys.
- `items()` returns key-value pairs as tuples.
- `keys()` returns all keys.
- `values()` returns all values.
- `copy()` creates an independent copy.
- `clear()` removes all items, while `del` deletes the dictionary itself.

---

# Memory Trick

**DICT = Direct Information by Custom Tags 🏷️**

- **D** → Data in pairs
- **I** → Indexed by keys
- **C** → Changeable (Mutable)
- **T** → Tagged with unique keys

Remember:

> **List = Ordered Collection 📋**  
> **Tuple = Fixed Collection 🔒**  
> **Set = Unique Collection 🎯**  
> **Dictionary = Key → Value Mapping 🗂️**