"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive
"""
print()
print("-------task1----")
print()
print()

correct_password ="Donyboi123" #this is the passowrd

user_input = input("Enter your password")

if user_input.upper() == correct_password.upper():
    print("Access granted")
else:
    print("Acess denied")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
print()
print("-------task2----")
print()
print()

if user_input.strip() =="":
    print("invalid")
else:
    print("valid")
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
print()
print("-------task3----")
print()
print()
name = "cat"

new_name = name.replace("cat","dog")

print(new_name)

#replaced cat with dog


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
print()
print("-------task4----")
print()
print()

nam = input("Enter your name: ")
age = input("Enter your age: ")

sentence = nam + " is " + str(age) # this is were the inputs combined
print(sentence)


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

print()
print("-------task5----")
print()
print()

Number1 = float(input("Enter the numerator: "))
Number2 = float(input("Enter the denominator: "))

# Check for division by zero
if Number2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    quotient = Number1 / Number2
    rounded_number = round(quotient, 1) #round the number to the nearist tenth
    print(" (rounded):", rounded_number) 

    
