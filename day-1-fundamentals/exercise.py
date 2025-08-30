# exercise.py - Practice Exercises
print("=== Python Fundamentals - Practice Exercises ===\n")

# Exercise 1: Personal Information Form
print("EXERCISE 1: PERSONAL INFORMATION")
print("Please provide your personal details:")
print("-" * 40)

# Get user input
full_name = input("Full Name: ")
age = input("Age: ")
city = input("City: ")
education = input("Education: ")
hobby = input("Hobby: ")

# Convert age to integer
age_int = int(age)

# Display formatted output
print(f"\n=== PERSONAL PROFILE ===")
print(f"Name: {full_name.upper()}")
print(f"Age: {age_int} years")
print(f"Location: {city.title()}")
print(f"Education: {education}")
print(f"Hobby: {hobby}")
print()

# Exercise 2: Simple Calculator
print("EXERCISE 2: SIMPLE CALCULATOR")
print("Let's perform some calculations!")
print("-" * 30)

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division carefully
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Display results
print(f"\nCALCULATION RESULTS:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
print(f"{num1} ÷ {num2} = {division}")
print()

# Exercise 3: String Manipulation
print("EXERCISE 3: STRING MANIPULATION")
sentence = input("Enter a sentence: ")

# String operations
length = len(sentence)
upper_case = sentence.upper()
lower_case = sentence.lower()
word_count = len(sentence.split())

print(f"\nSENTENCE ANALYSIS:")
print(f"Original: {sentence}")
print(f"Length: {length} characters")
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
print(f"Word count: {word_count} words")
print()

# Exercise 4: Type Conversion Challenge
print("EXERCISE 4: TYPE CONVERSION CHALLENGE")
# Get different types of input
str_number = input("Enter a number as text: ")
int_number = int(input("Enter a whole number: "))
float_number = float(input("Enter a decimal number: "))

# Convert and calculate
converted_int = int(str_number)
total = converted_int + int_number + float_number

print(f"\nCONVERSION RESULTS:")
print(f"Text '{str_number}' converted to integer: {converted_int}")
print(f"Sum of all numbers: {total}")
print(f"Data types - Text: {type(str_number)}, Whole: {type(int_number)}, Decimal: {type(float_number)}")
print()

print("🎉 Congratulations! You completed all exercises!")
print("=== Practice Exercises Complete ===")

# Bonus: Try these additional challenges
print("\n" + "="*50)
print("BONUS CHALLENGES:")
print("1. Create a BMI calculator")
print("2. Build a currency converter")
print("3. Make a time calculator (hours to minutes)")
print("4. Create a password strength checker")
