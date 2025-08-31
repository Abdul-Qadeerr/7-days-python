# Day 2: Control Flow

Control flow is the order in which individual statements, instructions, or function calls are executed or evaluated in a Python program. Python provides control flow tools such as conditional statements and loops to make decisions and repeat tasks.

---

## 1️⃣ if Statement

The `if` statement is used to execute a block of code only if a specific condition is true.

**Example:**  
If a number is greater than 5, print a message.  
The program checks the condition and only runs the block if the condition is satisfied.

---

## 2️⃣ if-else Statement

The `if-else` structure provides an alternative path of execution when the condition is false.

**Example:**  
If a number is even, print "Even"; otherwise, print "Odd".  
This lets you handle two possible outcomes from one condition.

---

## 3️⃣ if-elif-else Ladder

This structure allows checking multiple conditions in sequence.  
Python evaluates them from top to bottom and executes the first block where the condition is true.

**Example:**  
If a score is 90 or above, assign grade A.  
If it is 80 or above, assign grade B.  
If it is 70 or above, assign grade C.  
Otherwise, assign grade F.  
Only one block executes depending on the first matched condition.

---

## 4️⃣ Logical Operators

Logical operators are used to combine multiple conditions.

- `and`: True only if both conditions are true.
- `or`: True if at least one condition is true.
- `not`: Reverses the result (True becomes False and vice versa).

**Example:**  
Check if a person is over 18 **and** has an ID to allow access.  
You can also use `or` to allow if either one is true.

---

## 5️⃣ Nested if Statements

An `if` block inside another `if` block is called a nested `if`.

**Example:**  
First check if a number is positive.  
Then inside that, check if it's also less than 10.  
This lets you build complex logic with multiple levels of decision-making.

---

## 6️⃣ Ternary Operator (Inline if)

Python allows a shorthand version of `if-else` using the ternary or conditional expression.  
It's written in a single line for simple decisions.

**Example:**  
Check if a number is even or odd and store the result in a variable using one line.  
This is useful for compact and readable assignments.

---

## ✅ Summary

- Use `if`, `if-else`, and `if-elif-else` to make decisions.
- Combine conditions with `and`, `or`, and `not`.
- Use nested conditions for layered decision-making.
- Use the ternary operator for concise one-line decisions.

Control flow is essential for adding logic to your code and making it dynamic.
