# 📘 Day 17 – Exception Handling (Revision Notes)

---

# 1. Exception Handling

### Purpose
- Prevents the program from crashing when an error occurs.
- Allows graceful handling of errors.

### Keywords
- `try` → Code that may raise an exception.
- `except` → Runs if an error occurs.
- `else` → Runs only if no exception occurs.
- `finally` → Always runs (whether an exception occurs or not).

### Common Exceptions
- `TypeError`
- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `IndexError`
- `KeyError`

### Generic Exception
- `except Exception as e`
- Stores the error message in `e`.

---

# 2. Packing & Unpacking Arguments

## Unpacking (`*` and `**`)

Used to expand collections into individual arguments.

### `*` (Lists/Tuples)
- Unpacks elements as positional arguments.
- Used when a function expects separate arguments.
- Can unpack into variables.
- Can be used with functions like `range()`.

Example idea:
- `[2, 7] → range(*args)`

### `**` (Dictionaries)
- Unpacks dictionary items as keyword arguments.
- Dictionary keys must match function parameter names.

---

## Packing

Used when the number of arguments is unknown.

### `*args`
- Collects positional arguments into a **tuple**.

### `**kwargs`
- Collects keyword arguments into a **dictionary**.

---

# 3. Spreading (`*`)

Used to expand or merge collections.

Common uses:
- Combine multiple lists.
- Create a new list from existing lists.
- Insert elements while creating a new list.

Example idea:
- `[0, *list1, *list2]`

---

# 4. `enumerate()`

### Purpose
Returns both:
- Index
- Value

Useful when you need the position of items while looping.

Returns:
- `(index, item)`

---

# 5. `zip()`

### Purpose
Iterates through multiple iterables simultaneously.

- Combines elements with the same index.
- Stops when the shortest iterable ends.

Common uses:
- Combine two or more lists.
- Parallel iteration.
- Create dictionaries or paired data.

---

# Symbols Summary

| Symbol | Purpose |
|---------|---------|
| `*` | Pack/Unpack positional arguments |
| `**` | Pack/Unpack keyword arguments |

---

# Functions Summary

| Function | Purpose |
|----------|---------|
| `enumerate()` | Returns index and value |
| `zip()` | Combines multiple iterables |
| `range()` | Creates a sequence of numbers |

---

# Quick Memory Tricks

- **try** → Try this code.
- **except** → Handle errors.
- **else** → Runs if no error occurs.
- **finally** → Always runs.
- **`*args`** → Many positional arguments (Tuple).
- **`**kwargs`** → Many keyword arguments (Dictionary).
- **`*list`** → Unpack or spread a list.
- **`**dict`** → Unpack a dictionary.
- **`enumerate()`** → Index + Value.
- **`zip()`** → Pair items together.

---

# One-Line Revision

- Exception handling → Prevents program crashes.
- `try` → Risky code.
- `except` → Handles exceptions.
- `else` → Executes if no exception occurs.
- `finally` → Always executes.
- `*args` → Packs positional arguments into a tuple.
- `**kwargs` → Packs keyword arguments into a dictionary.
- `*` → Unpacks lists/tuples.
- `**` → Unpacks dictionaries.
- `enumerate()` → Returns index and value.
- `zip()` → Combines multiple iterables.