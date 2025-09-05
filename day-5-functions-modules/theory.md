# 📘 Functions & Modules in Python

## **Functions in Python** 

* **Definition:**
  A function is a reusable block of code that performs a specific task.
  Instead of writing the same code again and again, we put it inside a function and call it whenever needed.

* **Syntax:**

  ```python
  def function_name(parameters):
      # code block
      return value
  ```

* **Example:**

  ```python
  # Function to add two numbers
  def add(a, b):
      return a + b

  # Calling the function
  result = add(5, 3)
  print("Sum =", result)   # Output: Sum = 8
  ```

* **Advantages of Functions:**

  1. Code reusability
  2. Easy debugging and maintenance
  3. Improves readability
  4. Allows modular programming

---

## 2. **Modules in Python**

* **Definition:**
  A module is simply a file containing Python code (functions, variables, classes).
  It allows you to organize code logically and reuse it in different programs.

* **Types:**

  1. **Built-in modules** → Already available in Python (e.g., `math`, `random`, `os`)
  2. **User-defined modules** → Created by the programmer

* **Using a Module:**

  ```python
  import math

  print(math.sqrt(16))    # Output: 4.0
  print(math.pi)          # Output: 3.141592653589793
  ```

* **Creating a User-defined Module:**

  1. Create a file `mymodule.py`:

     ```python
     def greet(name):
         return f"Hello, {name}!"
     ```

  2. Use it in another file:

     ```python
     import mymodule

     print(mymodule.greet("Qadeer"))   # Output: Hello, Qadeer!
     ```

* **Advantages of Modules:**

  1. Code organization
  2. Reusability across projects
  3. Maintains clean structure
  4. Encourages modular programming

---

✅ **Summary:**

* Functions = Small reusable code blocks.
* Modules = Files that group related functions/variables together.
* Both improve **reusability, readability, and maintainability** in Python programming.

---
