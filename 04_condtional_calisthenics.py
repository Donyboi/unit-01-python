'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
print()
print("-------task1----")
print()
print()

if 12 >= 10: # This checks if 12 is greater than or equal to 10
    print(True)  # Since 12 is greater than 10, this condition is True
else:
    print(False)
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
print()
print("-------task2----")
print()
print()

age = 17

y_student =True

age < 18
if age <18 or y_student: # checks if there over or under 18
    price = 10
else:
    price =20

print("Ticket price: $",price) 



'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
print()
print("-------task3----")
print()
print()


# List of fruits
box_fruits = ["apple", "banana", "orange", "grape", "mango", "pineapple"]

# let someone enter a fruit name
human = input("Enter the name of a fruit: ").strip().lower()

# Check if the fruit is in the list
if human in box_fruits:
    print("Yes,that fruit is in the list.")
else:
    print("No, that fruit is not in the list.") # Prints a message if the fruit is not in the list

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''





'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
print()
print("-------task5----")
print()
print()

kilos = float(input("Enter the weight of the order in kilos: ")) # Get the weight of the order in kilos from the user
zone = input("Enter the destination zone (A or B): ") 
if kilos < 0: 
    print("Error: Order weight cannot be negative.") # Prints a error message if the weight is negative
elif zone == "A": 
    cost = kilos * 5   #miltiplying the weight of the oder by the cost per kilo
    print("The shipping cost is: $", cost) # Prints the shipping cost
elif zone == "B":
    cost = kilos * 7  #miltiplying the weight of the oder by the cost per kilo
    print("The shipping cost is: $", cost) # Prints the shipping cost
else:
    print("Error: Invalid destination zone. Please enter A or B.") # Prints a error message if the zone is invalid

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

print()
print("-------task6----")
print()
print()

def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("The triangle is Equilateral.")
        elif a == b or b == c or a == c:
            print("The triangle is Isosceles.")
        else:
            print("The triangle is Scalene.")
    else:
        print("Not a triangle.")
    
triangle_type(3, 4, 5)  
triangle_type(2, 2, 2) 
triangle_type(2, 2, 3)  
triangle_type(1, 2, 3)






