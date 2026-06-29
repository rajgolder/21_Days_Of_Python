# 📘 Day 12 – Modules (Revision Notes)

## 🎯 Learning Objectives

* Understand what modules are.
* Learn different ways to import modules.
* Get familiar with commonly used built-in modules.

---

# Modules

## What is a Module?

A **module** is a Python file (`.py`) containing reusable code such as:

* Variables
* Functions
* Classes
* Constants

### Why use Modules?

* Code reusability
* Better organization
* Easier maintenance
* Reduces code duplication

---

# Creating a Module

* Write Python code in a `.py` file.
* Save the file.
* Import it into another Python file when needed.

---

# Importing Modules

### Import Entire Module

* Imports the whole module.
* Access members using `module_name.member`.

**Best when:** You need multiple functions from the module.

---

### Import Specific Functions

* Imports only selected functions or variables.
* No need to write the module name every time.

**Best when:** You only need a few functions.

---

### Import with Alias

* Rename modules or functions during import using `as`.
* Makes long names shorter and improves readability.

---

# Built-in Modules

Python provides many built-in modules that don't require installation.

Some common modules:

* `math`
* `os`
* `sys`
* `random`
* `statistics`
* `string`
* `datetime`
* `json`
* `collections`
* `re`

---

# OS Module

### Purpose

Used for interacting with the operating system.

### Common Uses

* Create directories
* Delete directories
* Change current directory
* Get current working directory
* Work with files and folders

---

# Sys Module

### Purpose

Provides information about the Python runtime and system.

### Common Uses

* Access command-line arguments
* Exit a program
* Check Python version
* View module search paths
* Get maximum integer size

---

# Statistics Module

### Purpose

Performs statistical calculations.

### Common Functions

* Mean
* Median
* Mode
* Standard Deviation

Useful for data analysis and data science.

---

# Math Module

### Purpose

Provides mathematical functions and constants.

### Common Features

* π (pi)
* Square root
* Powers
* Logarithms
* Floor
* Ceiling

Useful for scientific and mathematical computations.

---

# String Module

### Purpose

Provides useful string-related constants.

### Common Features

* All letters
* Digits
* Punctuation characters

Useful for text processing and validation.

---

# Random Module

### Purpose

Generates random values.

### Common Uses

* Random numbers
* Random integers
* Password generators
* OTP generators
* Games
* Simulations

---

# Types of Import

| Method                        | Use                                             |
| ----------------------------- | ----------------------------------------------- |
| `import module`               | Import entire module                            |
| `from module import function` | Import specific function                        |
| `from module import *`        | Import everything *(generally not recommended)* |
| `import module as alias`      | Import with a shorter name                      |

---

# Best Practices

* ✔ Import only what you need.
* ✔ Use aliases for long module names.
* ✔ Avoid `from module import *` in large projects.
* ✔ Keep your own modules organized and meaningful.

---

# Common Mistakes

* ❌ Forgetting to import a module before using it.
* ❌ Naming your own file the same as a built-in module (e.g., `math.py`, `random.py`).
* ❌ Using `import *`, which can cause name conflicts.
* ❌ Assuming all modules are built into Python (some must be installed separately).

---

# Quick Revision

### Module

* Reusable Python file
* Contains functions, variables, classes, etc.

### Import Methods

* Import whole module
* Import selected members
* Import with alias

### Built-in Modules

| Module       | Purpose                     |
| ------------ | --------------------------- |
| `os`         | Operating system operations |
| `sys`        | Python runtime information  |
| `math`       | Mathematical operations     |
| `statistics` | Statistical calculations    |
| `string`     | String constants            |
| `random`     | Random value generation     |

---

# Key Takeaways

* Modules make code reusable and organized.
* Python provides many built-in modules.
* Import only what you need.
* Use aliases to improve readability.
* Avoid wildcard (`*`) imports in real projects.

---

# Interview / Exam Questions

1. What is a module?
2. Why are modules used?
3. Different ways to import a module.
4. What is the purpose of the `os` module?
5. What is the purpose of the `sys` module?
6. Name some commonly used built-in modules.
7. Why should `from module import *` generally be avoided?
8. What is aliasing in Python imports?
