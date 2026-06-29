# 📘 30 Days of Python – Day 10: Loops (Revision Notes)

## Loops

* Used to execute a block of code repeatedly.
* Two types of loops:

  * `while` loop
  * `for` loop

---

## While Loop

* Executes as long as the condition is `True`.
* Stops when the condition becomes `False`.
* Can have an optional `else` block that executes after the loop finishes normally.

---

## For Loop

* Used to iterate over a sequence.
* Can iterate through:

  * Lists
  * Tuples
  * Strings
  * Dictionaries
  * Sets
  * `range()` sequences

---

## Dictionary Iteration

* Iterating over a dictionary returns **keys** by default.
* Use `.items()` to access both **keys and values**.

---

## Break

* Immediately terminates the loop.
* Control moves to the first statement after the loop.

---

## Continue

* Skips the current iteration.
* Continues with the next iteration of the loop.

---

## `range()` Function

* Generates a sequence of numbers.
* Syntax:

  * `range(stop)`
  * `range(start, stop)`
  * `range(start, stop, step)`
* Default values:

  * Start = `0`
  * Step = `1`
* Negative step is used for reverse iteration.

---

## Nested Loops

* A loop inside another loop.
* Commonly used for:

  * Patterns
  * Matrices
  * Tables
  * Multi-dimensional data

---

## Loop `else`

* Executes only if the loop completes normally.
* Does **not** execute if the loop is terminated using `break`.

---

## `pass`

* Placeholder statement.
* Used when a statement is syntactically required but no action is needed.
* Useful while writing incomplete code.

---

# Key Points to Remember

* `while` → Runs until a condition becomes `False`.
* `for` → Iterates over a sequence.
* `break` → Exits the loop immediately.
* `continue` → Skips the current iteration.
* `range()` → Generates number sequences.
* Nested loops → Loop inside another loop.
* Dictionary iteration → Keys by default; use `.items()` for key-value pairs.
* Loop `else` runs only if the loop finishes without `break`.
* `pass` is a placeholder that does nothing.

---

# Quick Revision Checklist

* ✅ While loop
* ✅ While-else
* ✅ For loop
* ✅ Looping through lists, strings, tuples, dictionaries, and sets
* ✅ `break`
* ✅ `continue`
* ✅ `range()`
* ✅ Nested loops
* ✅ Loop `else`
* ✅ `pass`
