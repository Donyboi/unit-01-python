"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print("----task 1 -----")
print()

def my_name(name):
    print("hello" +" " + name)

my_name("billy")


"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print("----task 2 -----")
print()


def add_yay(a,b):
    return a ** b
x = add_yay(7,8)
print(x)

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print("----task 3 -----")
print()

def is_who(number):
    return number % 2==0
print(is_who(4))



"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print("----task 4 -----")
print()
def add_add(a,b,):
    return a *b
x = add_add(4,10)
print("length = 4")
print("width = 10")
print("area =",x)


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print("----task 5 -----")
print()
def resist(celius):
    return celius * 4 + 50
print(resist(10))
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.    
"""
print("----task 6 -----")
print()

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3])) 


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print("----task 7-----")
def calculate_total(price, quantity, discount=0.0):
    total = price * quantity
    if discount:
        total -= total * discount
    return total
print(calculate_total(10, 5))                
print(calculate_total(10, 5, discount=0.1))  

