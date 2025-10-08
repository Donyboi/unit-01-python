"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print("------task1-----")
print()
print()

for x in range(1,11):# the range function generates a sequence of numbers from 1 to 10
    print(x)


"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print("------task2-----")
print()
print()

for xbob in range(900, 1001, 10): 
    print(xbob)
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print("------task3-----")
print()
print()

for zbob in range(1,101,9):
    print(zbob)


"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print("------task4-----")
print()
print()

total = 0
for num in range(1, 11):
    total += num
print(total)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()