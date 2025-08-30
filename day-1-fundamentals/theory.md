### **Day 1: Python Fundamentals 🎯**

---

#### **Learning Objectives**

By the end of Day 1, you will:

* **Understand variables** and **data types**: You'll learn how to store different types of data in Python.
* **Learn basic input/output operations**: You'll interact with users by taking input and displaying output.
* **Master type conversion techniques**: You'll understand how to convert data from one type to another.
* **Practice basic arithmetic operations**: You'll work with mathematical operations such as addition, subtraction, multiplication, etc.

---

### **Introduction to Python 🐍**

---

#### **What is Python?**

Python is a **high-level**, **interpreted** programming language known for its **simplicity**, **readability**, and **versatility**. Designed to be easy to understand, Python lets you focus more on solving problems than on complex syntax.

**Key Characteristics of Python**:

* **High-level language**: Python abstracts low-level operations (like memory management), making it easier to write and read.
* **Interpreted**: Python code is executed line-by-line by an interpreter, which makes debugging easier.
* **Dynamically typed**: You don't need to declare variable types explicitly; Python does that automatically.
* **Garbage collected**: Python handles memory management for you.
* **Readable syntax**: Python prioritizes clear, concise code, which helps developers write maintainable programs.

---

#### **History of Python**

* **Created by**: **Guido van Rossum** in **1989**.
* **First released**: In **1991**, Python was introduced to the public.
* **Evolution**: Over the years, Python has evolved significantly:

  * **Python 2.x**: Was widely used but now officially discontinued as of **2020**.
  * **Python 3.x**: Released in **2008**, with many improvements. This is the current version.

---

#### **Why Python?**

Python is widely used because:

1. **Simplicity**: Python’s clean syntax makes it easy for beginners to understand and start coding quickly.
2. **Versatility**: Python can be used in:

   * Web development (Django, Flask)
   * Data science and machine learning (NumPy, pandas, TensorFlow)
   * Automation (scripts to automate repetitive tasks)
   * Game development (Pygame)
   * Scientific computing (SciPy, SymPy)
3. **Large Community**: Python has a massive global community with a wealth of resources, libraries, and frameworks.
4. **Cross-Platform**: Write Python code on one system (like Windows) and run it on another (like Linux or macOS) without modification.
5. **Rich Ecosystem**: Python has numerous libraries and frameworks for rapid development across many domains.
6. **Extensive Documentation**: Python has excellent documentation and a vast collection of tutorials and support materials.

---

#### **Python vs Other Languages**

| Feature              | Python                            | C/C++                                          | Java                 | JavaScript                |
| -------------------- | --------------------------------- | ---------------------------------------------- | -------------------- | ------------------------- |
| **Syntax**           | Simple, clean, and readable       | Complex                                        | Verbose              | Moderate                  |
| **Ease of Learning** | Easy to learn                     | Difficult                                      | Moderate             | Easy to learn             |
| **Execution**        | Interpreted (line-by-line)        | Compiled                                       | Compiled             | Interpreted               |
| **Use Cases**        | Web, Data Science, AI, Automation | Systems programming, performance-critical apps | Enterprise apps, Web | Web development, Frontend |
| **Community**        | Large and growing                 | Large but niche                                | Large                | Huge                      |

---

### **Core Concepts**

---

#### 1. **Variables in Python**

Variables are containers that store data values. In Python, you don’t need to declare variables before using them. You simply assign a value to a variable, and Python handles the type automatically.

**Examples of Variable Assignment**:

```python
name = "Qadeer"       # String (Text)
age = 20              # Integer (Whole number)
height = 5.9          # Float (Decimal number)
is_student = True     # Boolean (True or False)
```

Here, `name`, `age`, `height`, and `is_student` are variables storing different data types:

* `name` stores a **string**.
* `age` stores an **integer**.
* `height` stores a **float**.
* `is_student` stores a **boolean** value (`True` or `False`).

To display their values, you use the `print()` function:

```python
print(name)          # Output: Qadeer
print(age)           # Output: 20
print(height)        # Output: 5.9
print(is_student)    # Output: True
```

---

#### 2. **Data Types**

Python has several built-in data types, each serving different purposes:

| Data Type | Description                     | Example               |
| --------- | ------------------------------- | --------------------- |
| **int**   | Integer numbers (whole numbers) | `10`, `-5`, `1000`    |
| **float** | Decimal numbers                 | `3.14`, `-0.5`, `2.0` |
| **str**   | String (text data)              | `"hello"`, `"Python"` |
| **bool**  | Boolean values (True or False)  | `True`, `False`       |

**Example**:

```python
number = 10         # int
pi_value = 3.14     # float
greeting = "Hello"  # string
is_active = True    # boolean
```

These data types define what kind of information a variable can store.

---

#### 3. **Type Conversion**

Python allows you to convert between different data types using built-in functions.

**Common Type Conversions**:

* **`int()`**: Converts to an integer.
* **`float()`**: Converts to a float (decimal).
* **`str()`**: Converts to a string.

**Example**:

```python
num_str = "10"      # String
num_int = int(num_str)    # Convert to integer
num_float = float(num_str) # Convert to float

text = str(100)      # Convert integer to string

print(num_int)    # Output: 10
print(num_float)  # Output: 10.0
print(text)        # Output: "100"
```

---

#### 4. **Input/Output Operations**

Python provides simple ways to take **input** from the user and **output** information back.

* **`input()`**: Takes input from the user (always returns a string).
* **`print()`**: Displays output to the user.
* **f-strings**: Used to format strings and insert variable values directly.

**Example**:

```python
name = input("Enter your name: ")       # Returns a string
age = int(input("Enter your age: "))    # Convert input to integer

# Display the message using f-string
print(f"Hello {name}! You are {age} years old.")
```

This will prompt the user to enter their name and age, and then display:

```plaintext
Hello Qadeer! You are 20 years old.
```

---

#### 5. **Basic Arithmetic Operations**

Python supports basic arithmetic operations like addition, subtraction, multiplication, and more.

| Operator | Operation           | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `5 - 3`  | `2`    |
| `*`      | Multiplication      | `5 * 3`  | `15`   |
| `/`      | Division            | `15 / 3` | `5.0`  |
| `%`      | Modulus (remainder) | `10 % 3` | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |

**Example**:

```python
a = 10
b = 5

addition = a + b         # 10 + 5 = 15
subtraction = a - b      # 10 - 5 = 5
multiplication = a * b   # 10 * 5 = 50
division = a / b         # 10 / 5 = 2.0
modulus = a % b          # 10 % 5 = 0
exponentiation = a ** 2  # 10 ** 2 = 100

# Printing results
print(addition)          # Output: 15
print(subtraction)       # Output: 5
print(multiplication)    # Output: 50
print(division)          # Output: 2.0
print(modulus)           # Output: 0
print(exponentiation)    # Output: 100
```

---

### **Summary: Key Points from Day 1**

1. **Variables** store data in different types: strings, integers, floats, and booleans.
2. Python supports several **basic data types**: `int`, `float`, `str`,


`bool`.
3\. **Type conversion** allows conversion between data types using functions like `int()`, `float()`, and `str()`.
4\. **Input/Output operations** are done via `input()` for input and `print()` for output.
5\. Python provides basic **arithmetic operators** for calculations (`+`, `-`, `*`, `/`, `%`, `**`).

---

### **Next Steps**

* **Practice**: Write some basic code to interact with the user and perform arithmetic operations.
* **Experiment**: Try different type conversions and observe how Python handles various data types.
* **Exercises**: Work on a set of practice problems (stored in **exercise.py**) to solidify your understanding.
