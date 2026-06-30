# 📘 Day 2 Revision Notes

## Built-in Functions
- Built-in functions are available without importing any module.
- Common functions:
  - `print()` → Display output
  - `input()` → Take user input
  - `len()` → Length of an object
  - `type()` → Check data type
  - `int()` → Convert to integer
  - `float()` → Convert to float
  - `str()` → Convert to string
  - `list()` → Convert to list
  - `dict()` → Create dictionary
  - `min()` → Smallest value
  - `max()` → Largest value
  - `sum()` → Sum of values
  - `sorted()` → Sort values
  - `help()` → Documentation
  - `dir()` → List available attributes/functions

---

# Variables

## What is a Variable?
- Stores data in memory.
- Created using the assignment operator (`=`).

## Variable Naming Rules
- Must start with a letter or `_`
- Cannot start with a number
- Can contain letters, numbers, and `_`
- Cannot contain spaces or special characters (`@`, `-`, `$`, etc.)
- Case-sensitive (`age`, `Age`, `AGE` are different)

## Naming Convention
- Use **snake_case** for multi-word variables.
- Prefer meaningful names over single letters.

Example:
- `first_name`
- `birth_year`
- `total_marks`

## Multiple Variable Assignment
- Multiple variables can be assigned in one line.

## User Input
- `input()` accepts input from the keyboard.
- Returned value is always of type **string**.

---

# Data Types

| Data Type | Description |
|-----------|-------------|
| `str` | Text |
| `int` | Whole numbers |
| `float` | Decimal numbers |
| `bool` | True or False |
| `list` | Ordered mutable collection |
| `tuple` | Ordered immutable collection |
| `set` | Unordered unique collection |
| `dict` | Key-value pairs |
| `complex` | Complex numbers |

---

# Checking Data Type

- `type()` returns the data type of a variable or value.

Useful for debugging and understanding data.

---

# Type Casting

## Purpose
Convert one data type into another.

Common casting functions:
- `int()`
- `float()`
- `str()`
- `list()`
- `set()`

### Important Notes
- User input is always a **string**.
- Convert strings to numbers before arithmetic.
- Convert numbers to strings before concatenating with text.
- Converting float to int removes the decimal part (does not round).

---

# Number Types

## Integer (`int`)
- Whole numbers
- Positive, negative, or zero

Example:
- `-5`
- `0`
- `100`

---

## Float (`float`)
- Decimal numbers

Example:
- `3.14`
- `-2.5`
- `0.0`

---

## Complex (`complex`)
- Numbers with real and imaginary parts.

Example:
- `2 + 3j`

---

# Important Points to Remember

- Variables store values.
- `=` means assignment, **not equality**.
- Follow snake_case naming convention.
- `input()` always returns a string.
- Use `type()` to check data types.
- Use casting functions when changing data types.
- Python is case-sensitive.
- Avoid using Python keywords as variable names.

---

# Quick Revision Checklist ✅

- Built-in functions
- Variable naming rules
- Snake case convention
- Multiple variable assignment
- User input
- Basic data types
- `type()`
- Type casting
- Integer, Float, Complex numbers
```