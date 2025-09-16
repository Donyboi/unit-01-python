"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print()
print("-------task1----")
print()
print()

lis = [False,"hello",12,"people"]
print(lis)


"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
print()
print("-------task2----")
print()
print()

li = [True,31]
li.append("Eyes")
print(li)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print()
print("-------task3----")
print()
print()
# Create a list with 3 elements and print it.
l = ["mango",True,0.2]
l.remove("mango")
print(l)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print()
print("-------task4----")
print()
print()


my_list = ["apple", "banana", "cherry", "date"]

my_list[1]="orange" #Modify an element at a specific index with a new value. 

print(my_list) # Print the updated list.
"""




Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

print()
print("-------task5----")
print()
print()

cars = []

cars.append("old car")

print(cars)

cars.append("ugly car") #added ugly cars to the list

print(cars)


"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print()
print("-------task6----")
print()
print()

cars2 = ["ford","tesla","volvo"]

cars2.remove("ford") #roemove ford from the list 

print(cars2)

del cars2[1] #removed the first item

print(cars2) #print the rest of the list


"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print()
print("-------task7----")
print()
print()

my_list =["red","green","blue","yellow"] #old variable

 

first_two = my_list[:2] #creating the new variable 

print(first_two)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

print()
print("-------task8----")
print()
print()

list_a = ["bob","tom"] 

list_b = ["james","todd"]

lists = list_a + list_b #the plus symbol adds elements of list_a individually into list_b

print(lists)