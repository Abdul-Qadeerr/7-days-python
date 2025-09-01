````markdown
# 3 Loops in Python — Theory & Examples

> Focus: `for` loop, `while` loop, and **nested loops**  
> Goal: Clear theory + clean examples for exam/revision notes

---

## 1) `for` Loop

**Definition:**  
`for` loop sequence (list, tuple, string, dict, range, iterator) par iterate karta hai. Jab iterations ki count roughly pata ho ya aap kisi collection ke har item par kaam karna chahte ho, `for` best hai.

**Syntax:**
```python
for variable in iterable:
    # body
````

**Examples:**

```python
# 1) Range based
for i in range(1, 6):      # 1,2,3,4,5
    print(i)

# 2) List iterate
nums = [10, 20, 30]
for n in nums:
    print(n)

# 3) String iterate
for ch in "AI":
    print(ch)              # A \n I

# 4) Dictionary iterate (keys by default)
user = {"name": "Malik", "role": "Data Analyst"}
for k in user:
    print(k, user[k])      # key + value
```

**Useful Patterns:**

```python
# enumerate: index + value
arr = ["DS", "ML", "DL"]
for idx, val in enumerate(arr, start=1):
    print(idx, val)

# zip: parallel iteration
names = ["A", "B", "C"]
scores = [88, 92, 76]
for name, score in zip(names, scores):
    print(name, score)
```

**Loop `else`:**
`else` tab chalti hai jab loop **normally** finish ho (i.e., `break` na lage).

```python
for x in [1, 2, 3]:
    if x == 99:
        break
else:
    print("Completed without break")
```

---

## 2) `while` Loop

**Definition:**
`while` tab tak chalta hai jab tak condition `True` rahe. Jab iterations ki exact count **pehle se na pata ho**, ya condition-driven loops chahiye hon, `while` use karo.

**Syntax:**

```python
while condition:
    # body
```

**Examples:**

```python
# 1) Count until condition fails
i = 1
while i <= 5:
    print(i)
    i += 1

# 2) Input-driven loop (conceptual)
# while user_input != "quit":
#     user_input = input(">> ")
```

**Safety Tip (Infinite Loop):**
Condition ko update karna na bhoolo, warna infinite loop ho jayega.

```python
# Infinite example (DON'T DO THIS):
# while True:
#     pass
```

**Loop `else` with while:**

```python
n = 3
while n > 0:
    n -= 1
else:
    print("Loop ended normally (no break)")
```

---

## 3) Nested Loops

**Definition:**
Ek loop ke andar doosra loop. 2D/3D data structures (matrix), combinations, grids ya pattern printing ke liye useful.

**Syntax (2-level):**

```python
for i in outer_iterable:
    for j in inner_iterable:
        # body
```

**Examples:**

```python
# 3x3 grid
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# Multiplication table (1..3 x 1..3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:2}", end=" ")
    print()
```

**Nested with `while`:**

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j, end=" | ")
        j += 1
    print()
    i += 1
```

---

## Control Statements: `break`, `continue`, `pass`

* **`break`**: loop ko turant terminate karta hai
* **`continue`**: current iteration skip, next iteration par jump
* **`pass`**: placeholder (kuch nahi karta)

**Examples:**

```python
for i in range(1, 6):
    if i == 3:
        continue   # skip 3
    if i == 5:
        break      # stop loop entirely
    print(i)       # 1, 2, 4

# pass (placeholder)
for _ in range(3):
    pass  # later implement
```

---

## Performance & Best Practices

* `for` on iterables is **Pythonic** and usually clearer than manual index loops.
* Large loops me heavy work ko minimize karo; repeated computations loop ke bahar precompute kar lo.
* Dictionaries par iterate karte waqt `.items()` fast & clear:

  ```python
  for k, v in mydict.items():
      ...
  ```
* Agar sirf derived collection chahiye ho to **comprehensions** use karo (faster, concise).

**List Comprehension vs Loop:**

```python
# Loop
squares = []
for x in range(5):
    squares.append(x*x)

# Comprehension (equivalent, concise)
squares = [x*x for x in range(5)]
```

---

## Common Pitfalls

* **Off-by-one errors** with `range(start, stop)` (stop exclusive hota hai).
* **Modifying list while iterating** (unexpected behavior). Make a copy or build a new list.
* **Infinite loops** in `while` due to missing state updates.
* Shadowing variable names (`for list in lists:`) se bachain.

---

## Quick Practice

1. `for` loop se 1–100 tak even numbers print karo.
2. `while` loop se user se inputs lo jab tak wo `"exit"` na likhe (hint: break).
3. Nested loops se 5x5 identity matrix jaisa pattern print karo (1 diagonal par, baqi 0).
4. `for-else`: ek list me number `x` dhoondo; mil jaye to print “found” aur `break`; warna loop ke baad `"not found"` print ho.

---

## Mini Cheatsheet

* `for x in iterable:` — iterate items
* `for i, x in enumerate(xs, start=1):` — index + item
* `for a, b in zip(A, B):` — parallel iteration
* `while cond:` — condition-driven loop
* `break / continue / pass` — control flow
* `for ... else` & `while ... else` — run `else` **only if** no `break`

---

```
::contentReference[oaicite:0]{index=0}
```
