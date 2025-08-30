Day 1: Python Fundamentals
🎯 Learning Objectives
Understand variables and data types

Learn basic input/output operations

Master type conversion techniques

Practice basic arithmetic operations

📚 Core Concepts
1. Variables
Variables are containers for storing data values. In Python, you don't need to declare variables before using them.

python
# Variable assignment examples
name = "Alice"      # String
age = 25           # Integer
height = 5.9       # Float
is_student = True  # Boolean
2. Data Types
Python has several built-in data types:

Data Type	Description	Example
int	Integer numbers	10, -5, 1000
float	Decimal numbers	3.14, -0.5, 2.0
str	Text data	"hello", 'Python'
bool	Boolean values	True, False
3. Type Conversion
Convert between types using built-in functions:

python
# Type conversion examples
num_str = "10"
num_int = int(num_str)    # Convert to integer
num_float = float(num_str) # Convert to float
text = str(100)           # Convert to string
4. Input/Output Operations
input(): Get user input (always returns string)

print(): Display output

f-strings: Format strings with variables

python
# Input/output examples
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}! You are {age} years old.")
5. Basic Arithmetic Operations
Python supports all basic mathematical operations:

Operator	Operation	Example	Result
+	Addition	5 + 3	8
-	Subtraction	5 - 3	2
*	Multiplication	5 * 3	15
/	Division	15 / 3	5.0
%	Modulus	10 % 3	1
**	Exponentiation	2 ** 3	8
💡 Best Practices
Use descriptive variable names

Always validate user input

Use f-strings for string formatting

Comment your code for clarity

🚀 Next Steps
Practice with the code examples in this folder

Complete the exercise.py file

Move to Day 2: Control Flow
