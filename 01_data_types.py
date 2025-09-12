"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
print("------task1------")
print()
print()
don_float=15.6



don_intger=int(don_float)
print(don_float)
print(don_intger)

print()
print()
print("------task1------")

#turn a float into a integer


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
print("------task2------")
print()
print()


number =float(input("enter a number"))
if number > 0:
    print("the number is positve")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")

print("------task2------")
print()
print()

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
print()
print("------task3------")
print()
print()

dony3=input("give ne a float:")

dony3=float(dony3)

print(type(dony3))

dony4=input("give me a integer:")

dony4=int(dony4)
print(type(dony4))


print("------task3------")
print()
print()
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
print("------task4------")
print()
print()

x={
    "apple":7,
    "mango":8
}
print(x["apple"])

print("------task3------")
print()
print()

#i made a dictonary that prints apple.
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""