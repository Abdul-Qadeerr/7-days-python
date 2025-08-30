# user_input.py - Input/Output Examples
print("=== User Input and Output Examples ===\n")

# 1. Basic Input
print("1. BASIC INPUT")
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"Hello {name}! You are {age} years old.")
print()

# 2. Multiple Inputs in One Line
print("2. MULTIPLE INPUTS")
data = input("Enter your name and age separated by space: ")
name, age = data.split()
print(f"Name: {name}, Age: {age}")
print()

# 3. Number Input with Validation
print("3. NUMBER INPUT VALIDATION")
try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
except ValueError:
    print("Error: Please enter valid numbers!")
print()

# 4. Formatted Output with f-strings
print("4. FORMATTED OUTPUT")
city = input("Enter your city: ")
state = input("Enter your state: ")
country = "India"

print(f"\n=== USER PROFILE ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {city}, {state}, {country}")
print(f"Profile: {age}-year-old from {city}, {state}")
print()

# 5. Practical Example - Registration Form
print("5. REGISTRATION FORM")
print("Please complete your registration:")
print("-" * 30)

username = input("Choose a username: ")
email = input("Enter your email: ")
password = input("Create a password: ")
phone = input("Enter your phone number: ")

print("\n=== REGISTRATION SUMMARY ===")
print(f"Username: {username}")
print(f"Email: {email}")
print(f"Password: {'*' * len(password)}")
print(f"Phone: {phone}")
print("Registration successful! ✅")
print()

print("=== Input/Output Practice Complete ===")
