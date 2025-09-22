import math

# Additionw
# Subtraction
# Multiplication
# Division
# Exponents
# Floor Division
# Remainder
# Example Code Output:

# Welcome to the Calculatinator-inator 9000!

# Enter the first number: 10
# Enter the second number: 5

# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Floor Division
# 6. Exponential
# 7. Remainder

# Enter choice: 3

# Result: 50.0

print("Welcome to the Calculatinator-inator 9000!")


math1 = float(input("Enter the first number: "))
math2 = float(input("Enter the second number: "))
if math1 and math2 == str:
	print("THIS IS NOT A NUMBER :)")

print()
print("Select operation:")
print()
print("1. Addition")
print()
print("2. Subtraction")
print()
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
print()
choice = input("Enter choice (1/2/3/4/5/6/7): ")

if choice == "1":
	result = math1 + math2
	print(f"Result: {result}")
elif choice == "2":
	result = math1 - math2
	print(f"Result: {result}")
elif choice == "3":
	result = math1 * math2
	print(f"Result: {result}")
elif choice == "4":
	if math2 != 0:
		result = math1 / math2
		print(f"Result: {result :.2f}")
	else:
		print("Error: Division by zero.")
elif choice == "5":
	if math2 != 0:
		result = math1 // math2
		print(f"Result: {result :.2f}")
	else:
		print("Error: Division by zero.")
elif choice == "6":
	result = math1 ** math2
	print(f"Result =: {result}")
elif choice == "7":
	if math2 != 0:
		result = math1 % math2
		print(f"Result: {result}")
	else:
		print("Error: Division by zero.")
else:
	print("Invalid input.")
	