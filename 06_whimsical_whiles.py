""""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
bob = 1 
while bob < 10: # This is the condition
    print(bob)
    bob += 1 #  increacing the number by 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
tommy = 10
while tommy >= 1:
    print(tommy)
    tommy -= 1 # decreasing the number by 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
carly = int(input("give number: "))
result = 1
while carly > 0: # while the number is greater than 0 it will keep looping
    result = carly * result # multiplying the number by result
    carly -= 1 # decreasing the number by 1
print(result)

  


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = "password123"
john = "" 
while john != password: # while the user guess is not equal to the password it will keep looping
    john = input("Enter the password: ")
    if john == password:
        print("Access Granted!") # giving feedback
    else:
        print("Incorrect password, try again.") # giving feedback
    


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""



"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
# Program to print the first n Fibonacci numbers using a while loop

n = int(input("Enter the number of Fibonacci numbers to print: "))

# First two Fibonacci numbers
a, b = 0, 1
count = 0

while count < n: 
    print(a)
    a, b = b, a + b  # Update values of a and b
    count += 1