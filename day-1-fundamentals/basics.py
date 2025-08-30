# basics.py - Basic Python Syntax Examples
print("=== Python Basics ===\n")

# 1. Variables and Data Types
print("1. VARIABLES AND DATA TYPES")
name = "Aarav Sharma"          # string
age = 25                       # integer
height = 5.9                   # float
is_indian = True               # boolean
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Indian: {is_indian} (Type: {type(is_indian)})")
print()

# 2. Basic Arithmetic Operations
print("2. ARITHMETIC OPERATIONS")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Integer Division (a // b): {a // b}")
print(f"Modulus/Remainder (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")
print()

# 3. String Operations
print("3. STRING OPERATIONS")
first_name = "Raj"
last_name = "Kumar"
full_name = first_name + " " + last_name  # Concatenation
print(f"Full Name: {full_name}")
print(f"Name in uppercase: {full_name.upper()}")
print(f"Name length: {len(full_name)} characters")
print()

# 4. Boolean Operations
print("4. BOOLEAN OPERATIONS")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"Not True: {not True}")
print()

print("=== Basics Demonstration Complete ===")
