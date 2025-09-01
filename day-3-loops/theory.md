````markdown
# Day 3: Loops

Loops in Python are used to execute a block of code repeatedly until a certain condition is met. They help automate repetitive tasks and reduce redundancy in programs.  

Python mainly provides three types of loops: **for loop**, **while loop**, and **nested loops**.  

---

## 1️⃣ for Loop  
The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range).  

**Example:**  
Print numbers from 1 to 5.  
The loop will run once for each number in the sequence.  

```python
for i in range(1, 6):
    print(i)
````

---

## 2️⃣ while Loop

The `while` loop executes a block of code as long as a condition is true.

**Example:**
Print numbers from 1 to 5 using a `while` loop.

```python
num = 1
while num <= 5:
    print(num)
    num += 1
```

---

## 3️⃣ Nested Loops

A loop inside another loop is called a nested loop.
They are useful for working with multi-dimensional data (like matrices).

**Example:**
Print a 3x3 grid of numbers.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i},{j}", end="  ")
    print()
```

---

## 🔄 Loop Control Statements

### 🔹 break

Used to exit the loop immediately.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

### 🔹 continue

Skips the current iteration and moves to the next one.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### 🔹 pass

Does nothing; acts as a placeholder.

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

---

## ✅ Summary

* Use `for` loops to iterate over sequences.
* Use `while` loops when the number of iterations is not fixed.
* Use **nested loops** for complex iterations.
* Control loop behavior using `break`, `continue`, and `pass`.
* Loops help in automating repetitive tasks and make programs more efficient.

```

---
