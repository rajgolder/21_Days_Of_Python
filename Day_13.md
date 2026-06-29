# 📘 Day 13 – List Comprehension (Revision Notes)

## 🎯 Learning Objectives

After completing this chapter, you should understand:

* What list comprehension is
* Why list comprehension is preferred over traditional loops
* How to use conditions in list comprehension
* What lambda functions are
* When to use lambda functions

---

# List Comprehension

## Definition

List comprehension is a concise and Pythonic way to create a new list from an existing iterable.

Instead of writing multiple lines using a `for` loop, list comprehension allows you to write the same logic in a single line.

---

## Advantages

* Shorter and cleaner code
* Faster than using a normal `for` loop
* Easy to read for simple operations
* Can perform transformations while creating a list
* Can filter elements using conditions

---

## Basic Syntax

```
[expression for item in iterable]
```

### Components

* **Expression** → Operation performed on each element
* **Item** → Current element during iteration
* **Iterable** → Sequence being traversed

---

## Conditional List Comprehension

Conditions can be added to include only elements that satisfy a requirement.

### Syntax

```
[expression for item in iterable if condition]
```

### Common Uses

* Filter even numbers
* Filter odd numbers
* Remove unwanted values
* Select positive or negative numbers
* Extract specific elements from data

---

## Nested List Comprehension

List comprehension can also iterate through nested lists.

### Common Use

* Flattening a 2D list into a 1D list
* Processing matrices
* Working with nested data structures

---

## Applications

List comprehension is commonly used for:

* Creating lists
* Mathematical operations
* Data filtering
* String processing
* Flattening nested lists
* Creating tuples or dictionaries

---

## Best Practices

✅ Use list comprehension for simple operations.

✅ Use a normal `for` loop when the logic becomes too complex.

✅ Keep readability more important than writing everything in one line.

---

## Lambda Function

## Definition

A lambda function is a small anonymous (unnamed) function.

It can:

* Take any number of arguments
* Contain only one expression
* Return the result automatically

---

## Characteristics

* Anonymous (no function name)
* Single expression only
* No explicit `return` statement
* Mostly used for short, temporary functions

---

## Syntax

```
lambda parameters: expression
```

---

## Why Use Lambda Functions?

* Reduces code size
* Useful for one-time functions
* Often used with higher-order functions like:

  * `map()`
  * `filter()`
  * `reduce()`
  * `sorted()`

---

## Lambda Inside Another Function

A lambda function can be created and returned from another function.

This allows:

* Dynamic function creation
* Function factories
* Cleaner functional programming

---

## When to Use Lambda

Use lambda when:

* The function is short.
* The function is used only once.
* Only a single expression is needed.

Avoid lambda when:

* The logic is complex.
* Multiple statements are required.
* Readability decreases.

---

# List Comprehension vs For Loop

| List Comprehension         | For Loop                 |
| -------------------------- | ------------------------ |
| Short and concise          | More verbose             |
| Faster execution           | Slightly slower          |
| Best for simple operations | Better for complex logic |
| More Pythonic              | More flexible            |

---

# Normal Function vs Lambda Function

| Normal Function                 | Lambda Function       |
| ------------------------------- | --------------------- |
| Has a name                      | Anonymous             |
| Uses `def`                      | Uses `lambda`         |
| Can contain multiple statements | Only one expression   |
| Uses `return`                   | Returns automatically |

---

# Key Points to Remember

* List comprehension creates a new list in a concise way.
* It is generally faster than a traditional `for` loop.
* Conditions can be added using `if`.
* Nested list comprehension can flatten nested lists.
* Lambda functions are anonymous functions.
* Lambda functions contain only one expression.
* Lambda functions are commonly used with higher-order functions.

---

# Common Mistakes

❌ Making list comprehensions too long and difficult to read.

❌ Using lambda for complex logic.

❌ Forgetting that lambda supports only one expression.

❌ Using list comprehension when a normal loop is more readable.

---

# Quick Revision

### List Comprehension

* Creates a new list
* Compact syntax
* Faster than loops
* Supports conditions
* Supports nested iteration

### Lambda Function

* Anonymous function
* Single expression
* Automatic return
* Useful with higher-order functions

---

# Interview / Exam Questions

1. What is list comprehension?
2. What are the advantages of list comprehension?
3. What is the syntax of list comprehension?
4. How do you add conditions in list comprehension?
5. What is nested list comprehension?
6. What is a lambda function?
7. Why are lambda functions called anonymous functions?
8. Difference between a normal function and a lambda function.
9. When should you use lambda functions?
10. Compare list comprehension and a traditional `for` loop.
