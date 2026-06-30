# 📘 Day 4 Revision Notes

# Strings

- A **string (`str`)** is a sequence of characters used to store text.
- Strings can be enclosed in:
  - Single quotes `' '`
  - Double quotes `" "`
  - Triple quotes `''' '''` or `""" """` (for multiline strings)
- Use `len()` to find the length of a string.

---

# Creating Strings

- Single character and multiple characters are both strings.
- Triple quotes allow multiline strings.

---

# String Concatenation

- Joining two or more strings together.
- Uses the `+` operator.

Example:
- `"Hello" + " World"` → `"Hello World"`

---

# Escape Sequences

| Escape | Meaning |
|--------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

---

# String Formatting

Three common methods:

## 1. `%` Formatting (Old Style)
- Uses `%s`, `%d`, `%f`

---

## 2. `str.format()` (Recommended)

- Uses `{}` placeholders.

---

## 3. f-Strings ⭐ (Most Recommended)

- Introduced in Python 3.6.
- Prefix string with `f`.
- Cleaner, faster, and easiest to read.

---

# Strings as Sequences

Strings behave like sequences.

## Character Access (Indexing)

- Index starts from **0**.
- Negative indexing starts from **-1** (last character).

Example:
- First character → `0`
- Last character → `-1`

---

# String Slicing

Extract a portion of a string.

General syntax:

```
string[start:end:step]
```

### Common Slices

- First few characters
- Last few characters
- From a position to the end
- Entire string

---

# Reverse a String

Use slicing with a negative step.

```
[::-1]
```

---

# Skipping Characters

Use the **step** value while slicing.

Example:
- Every 2nd character
- Every 3rd character

---

# Common String Methods

## Case Conversion

| Method | Purpose |
|---------|---------|
| `capitalize()` | First letter uppercase |
| `title()` | First letter of every word uppercase |
| `upper()` | All uppercase |
| `lower()` | All lowercase |
| `swapcase()` | Toggle uppercase/lowercase |

---

## Searching

| Method | Purpose |
|---------|---------|
| `find()` | Returns first index or `-1` |
| `rfind()` | Returns last index or `-1` |
| `index()` | Returns first index (error if not found) |
| `rindex()` | Returns last index (error if not found) |
| `count()` | Counts occurrences |
| `startswith()` | Checks starting text |
| `endswith()` | Checks ending text |

---

## Modifying Strings

| Method | Purpose |
|---------|---------|
| `replace()` | Replace text |
| `strip()` | Remove leading/trailing characters or spaces |
| `split()` | Split into list |
| `join()` | Join list into string |
| `expandtabs()` | Replace tabs with spaces |

---

## Validation Methods

| Method | Checks |
|---------|--------|
| `isalnum()` | Letters and numbers only |
| `isalpha()` | Letters only |
| `isdigit()` | Digits only |
| `isdecimal()` | Decimal digits only |
| `isnumeric()` | Numeric characters |
| `islower()` | All lowercase |
| `isupper()` | All uppercase |
| `isidentifier()` | Valid Python variable name |

---

# Important Differences

## `find()` vs `index()`

| `find()` | `index()` |
|-----------|-----------|
| Returns `-1` if not found | Raises an error if not found |

---

## `isdigit()` vs `isdecimal()` vs `isnumeric()`

- `isdecimal()` → Strict decimal digits (`0-9`)
- `isdigit()` → Digits + some Unicode digits
- `isnumeric()` → Most flexible; accepts numeric symbols like `½`

---

# Important Points to Remember

- Strings are **immutable** (cannot be changed directly).
- Indexing starts at **0**.
- Negative indexing starts from **-1**.
- Slicing does **not** modify the original string.
- `len()` returns string length.
- `split()` returns a list.
- `join()` joins iterable elements into a string.
- Prefer **f-strings** for modern Python formatting.

---

# Quick Revision Checklist ✅

- String creation
- `len()`
- Concatenation
- Escape sequences
- String formatting (`%`, `format()`, `f-string`)
- Indexing
- Negative indexing
- Slicing
- Reverse string
- Step slicing
- Search methods
- String modification methods
- Validation methods
- `find()` vs `index()`
- `isdigit()` vs `isdecimal()` vs `isnumeric()`
```