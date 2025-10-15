import random




print("----task1-----")
print()
print()


for _ in range(10):
    roll = random.randint(1, 6)
    print(f"Roll: {roll}")


"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""

print("----task2-----")
print()
print()


for _ in range(5):
    roll = random.uniform(0,1)
    print(f"roll: {roll:.2f}")
    print()
for _ in range(5):
    roll = random.uniform(10,20)
    print(f"roll: {roll:.2f}")

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print("----task3-----")
print()
print()

bobby_colors = ["red", "blue", "green", "yellow", "purple"]
for _ in range(3):
    print(random.choice(bobby_colors))



"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""

print("----task4-----")
print()
print()

numbers = list(range(1, 11))
random.shuffle(numbers)
print("Shuffled numbers:", numbers)




