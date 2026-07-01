# 📘 Day 16: `datetime` (Revision Notes)

## What is `datetime`?
- Built-in Python module for working with **dates and times**.
- Used to create, format, compare, and manipulate date/time values.

---

# Main Classes

| Class | Purpose |
|--------|---------|
| `datetime` | Date and time together |
| `date` | Date only |
| `time` | Time only |
| `timedelta` | Difference between dates/times |

---

# Current Date & Time

Use `datetime.now()` to get the current:
- Day
- Month
- Year
- Hour
- Minute
- Second
- Timestamp

---

# Timestamp
- Number of seconds since **1 January 1970 (Unix Epoch)**.
- Useful for:
  - Logging
  - File timestamps
  - Databases
  - Time calculations

---

# Formatting Date & Time

Use `strftime()` to convert a date/time object into a formatted string.

### Common Format Codes

| Code | Meaning |
|------|---------|
| `%d` | Day (01–31) |
| `%m` | Month (01–12) |
| `%Y` | 4-digit year |
| `%y` | 2-digit year |
| `%H` | Hour (24-hour) |
| `%M` | Minute |
| `%S` | Second |
| `%B` | Full month name |
| `%b` | Short month name |
| `%A` | Full weekday |
| `%a` | Short weekday |

---

# String to Date

Use `strptime()` to convert a formatted string into a `datetime` object.

> **Remember:**  
> `strptime()` = **String → DateTime**

---

# Working with `date`

The `date` class stores only:
- Year
- Month
- Day

Useful methods:
- `today()`
- `.year`
- `.month`
- `.day`

---

# Working with `time`

The `time` class represents only:
- Hour
- Minute
- Second
- Microsecond

---

# Date & Time Difference

- Subtract two `date` objects.
- Subtract two `datetime` objects.
- Result is a **`timedelta`** object.

---

# `timedelta`

Represents a duration or time interval.

Can store:
- Weeks
- Days
- Hours
- Minutes
- Seconds
- Microseconds

Useful for:
- Adding days
- Subtracting dates
- Calculating age
- Countdowns

---

# Common Methods

| Method | Purpose |
|---------|---------|
| `now()` | Current date and time |
| `today()` | Current date |
| `strftime()` | Date → String |
| `strptime()` | String → Date |
| `timestamp()` | Unix timestamp |

---

# Common Classes

| Class | Stores |
|--------|--------|
| `datetime` | Date + Time |
| `date` | Date only |
| `time` | Time only |
| `timedelta` | Time duration |

---

# Real-World Uses

- Digital clocks
- Age calculation
- Countdown timers
- Attendance systems
- Blog post timestamps
- File modification dates
- Scheduling tasks
- Logging application events
- Time-series analysis

---

# Exam Tips

- `datetime.now()` → Current date and time.
- `date.today()` → Current date only.
- `strftime()` → Format a date/time object into a string.
- `strptime()` → Convert a string into a date/time object.
- Subtracting dates returns a `timedelta`.
- Unix timestamp starts from **1 January 1970**.

---

# Memory Trick

### Date Conversion

- **strftime()** → **Date → String**
- **strptime()** → **String → Date**

Think:

- **f = format** → `strftime()`
- **p = parse** → `strptime()`

---

# Quick Revision

- `datetime` → Date + Time
- `date` → Date only
- `time` → Time only
- `timedelta` → Time difference
- `now()` → Current date/time
- `today()` → Current date
- `strftime()` → Format date
- `strptime()` → Parse string
- `timestamp()` → Seconds since 1 Jan 1970