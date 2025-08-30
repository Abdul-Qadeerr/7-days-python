# type_conversion.py - Type Conversion Practice
print("=== Type Conversion Practice ===\n")

# 1. String to Number Conversion
print("1. STRING TO NUMBER CONVERSION")
number_str = "123"
float_str = "45.67"

# Convert to integer
number_int = int(number_str)
print(f"String '{number_str}' to integer: {number_int} (Type: {type(number_int)})")

# Convert to float
number_float = float(float_str)
print(f"String '{float_str}' to float: {number_float} (Type: {type(number_float)})")
print()

# 2. Number to String Conversion
print("2. NUMBER TO STRING CONVERSION")
age = 25
salary = 50000.50

age_str = str(age)
salary_str = str(salary)
print(f"Integer {age} to string: '{age_str}' (Type: {type(age_str)})")
print(f"Float {salary} to string: '{salary_str}' (Type: {type(salary_str)})")
print()

# 3. Mixed Type Operations
print("3. MIXED TYPE OPERATIONS")
# This will cause error without conversion
num_str = "10"
num_int = 5

# Wrong way (will cause error)
# result = num_str + num_int  # TypeError

# Right way - convert first
result = int(num_str) + num_int
print(f"'{num_str}' + {num_int} = {result}")
print()

# 4. Boolean Conversion
print("4. BOOLEAN CONVERSION")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(-1): {bool(-1)}")
print(f"bool('Hello'): {bool('Hello')}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print()

# 5. Practical Example - Calculator Input
print("5. PRACTICAL EXAMPLE - CALCULATOR INPUT")
input1 = input("Enter first number: ")
input2 = input("Enter second number: ")

# Convert to numbers before calculation
num1 = float(input1)
num2 = float(input2)

sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")
print()

print("=== Type Conversion Practice Complete ===")
