# 📘 Day 14 – Higher Order Functions (Revision Notes)

## Higher Order Functions (HOF)

### Definition
A Higher Order Function is a function that:
- Accepts one or more functions as arguments, or
- Returns another function.

### Why use them?
- Makes code reusable
- Reduces repetition
- Makes programs more modular
- Commonly used in functional programming

### First-Class Functions
In Python, functions are treated like normal objects. They can:
- Be assigned to variables
- Be passed as arguments
- Be returned from other functions
- Be stored in data structures

---

## Function as a Parameter

A function can receive another function as an argument.

### Benefits
- Reuse existing functions
- Write flexible code
- Avoid duplicate logic

**Remember:** The function itself is passed, not its result.

---

## Function as a Return Value

A function can create and return another function.

### Why?
- Different behavior based on input
- Dynamic function creation
- Used in decorators and closures

---

## Closures

### Definition
A closure is an inner function that remembers variables from its outer function even after the outer function has finished executing.

### Key Points
- Uses nested functions
- Preserves state
- Commonly used in decorators and callbacks

**Memory Trick**
Closure = "Function + Remembered Variables"

---

## Decorators

### Definition
A decorator adds extra functionality to an existing function without changing its original code.

### Uses
- Logging
- Authentication
- Timing execution
- Validation
- Access control

### Syntax
Uses the `@` symbol.

### Multiple Decorators
Applied from bottom to top.

---

# Built-in Higher Order Functions

## map()

### Purpose
Transforms every element in an iterable.

Input:
- Function
- Iterable

Output:
- New iterator with transformed values

Use when:
- Every item needs modification.

---

## filter()

### Purpose
Keeps only elements that satisfy a condition.

Input:
- Function returning True/False
- Iterable

Output:
- Filtered iterator

Use when:
- Removing unwanted items.

---

## reduce()

### Purpose
Combines all elements into a single value.

Located in:
`functools`

Examples:
- Sum
- Product
- Maximum
- Concatenation

---

# map vs filter vs reduce

| Function | Purpose | Output |
|----------|---------|--------|
| map | Transform | New iterable |
| filter | Select | Filtered iterable |
| reduce | Combine | Single value |

---

# HOF vs Closure vs Decorator

| Concept | Purpose |
|---------|---------|
| Higher Order Function | Takes/returns functions |
| Closure | Remembers outer variables |
| Decorator | Extends another function |

---

# Quick Revision

✅ Higher Order Function → Takes or returns functions

✅ Closure → Remembers outer variables

✅ Decorator → Adds functionality without modifying code

✅ map() → Transform

✅ filter() → Select

✅ reduce() → Combine

---

# Common Interview Questions

1. What is a Higher Order Function?
2. Why are Python functions called first-class objects?
3. What is a closure?
4. Difference between closure and decorator?
5. Difference between map(), filter(), and reduce()?
6. Why is reduce() imported from functools?