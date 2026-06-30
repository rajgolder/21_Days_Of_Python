# 📘 Day 15: Python Errors (Revision Notes)

## What are Python Errors?
- Errors occur when Python cannot execute code correctly.
- Reading error messages helps identify the problem and its location.
- Debugging = Finding and fixing errors.

---

# Common Python Errors

## 1. SyntaxError
- Invalid Python syntax.
- Code cannot run until fixed.

**Common Causes**
- Missing `:`
- Missing brackets or quotes
- Incorrect indentation
- Misspelled keywords

---

## 2. NameError
- Using a variable or function that hasn't been defined.

**Common Causes**
- Typo in variable name
- Variable not created before use

---

## 3. IndexError
- Accessing an index outside the valid range.

**Common Causes**
- List or tuple index too large
- Empty sequence

---

## 4. ModuleNotFoundError
- Python cannot find the module being imported.

**Common Causes**
- Wrong module name
- Module not installed

---

## 5. AttributeError
- Object doesn't have the requested attribute or method.

**Common Causes**
- Misspelled method
- Using a method that doesn't exist for that object

---

## 6. KeyError
- Dictionary key does not exist.

**Common Causes**
- Wrong key name
- Typo in key

**Tip**
- Use `get()` to avoid this error.

---

## 7. TypeError
- Operation performed on incompatible data types.

**Common Causes**
- Mixing strings and numbers
- Wrong argument type passed to a function

---

## 8. ImportError
- Python cannot import the requested object from a module.

**Common Causes**
- Incorrect function/class name
- Wrong import statement

---

## 9. ValueError
- Correct data type, but invalid value.

**Common Causes**
- Invalid string-to-number conversion
- Invalid function argument

---

## 10. ZeroDivisionError
- Attempting to divide by zero.

---

# Error Summary Table

| Error | Cause |
|--------|-------|
| `SyntaxError` | Invalid Python syntax |
| `NameError` | Variable/function not defined |
| `IndexError` | Index out of range |
| `ModuleNotFoundError` | Module not found |
| `AttributeError` | Invalid attribute or method |
| `KeyError` | Dictionary key not found |
| `TypeError` | Incompatible data types |
| `ImportError` | Cannot import requested object |
| `ValueError` | Invalid value for operation |
| `ZeroDivisionError` | Division by zero |

---

# Debugging Tips

- Read the **last line** of the error message first.
- Check the line number mentioned in the traceback.
- Look for spelling mistakes.
- Verify variable names and dictionary keys.
- Check data types before operations.
- Ensure indexes are within range.
- Confirm modules and functions exist before importing.

---

# Common Fixes

| Problem | Solution |
|----------|----------|
| Variable not found | Define it first |
| Wrong data type | Convert using appropriate type conversion |
| Missing key | Use `get()` or check with `in` |
| Wrong index | Check length before accessing |
| Import fails | Verify module/function name |
| Divide by zero | Check denominator before division |

---

# Exam Tips

- **SyntaxError** → Invalid syntax.
- **NameError** → Undefined variable.
- **IndexError** → Index outside range.
- **KeyError** → Missing dictionary key.
- **TypeError** → Wrong data types.
- **ValueError** → Right type, wrong value.
- **ModuleNotFoundError** → Module missing.
- **ImportError** → Cannot import object.
- **AttributeError** → Attribute/method doesn't exist.
- **ZeroDivisionError** → Division by zero.

---

# Memory Trick

**S N I M A K T I V Z**

Remember the sequence:

- **S** → SyntaxError
- **N** → NameError
- **I** → IndexError
- **M** → ModuleNotFoundError
- **A** → AttributeError
- **K** → KeyError
- **T** → TypeError
- **I** → ImportError
- **V** → ValueError
- **Z** → ZeroDivisionError

> **Rule of Thumb:**  
> Read the error message carefully—it usually tells you **what went wrong** and **where to fix it**.