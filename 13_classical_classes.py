"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print("----task 1 -------")

class Person:
    species = 'human'
   

    def __init__(self, name, age):
     self.name = name
     self.age = age

dony = Person("Dony" ,17 )
print(dony.name)
print(dony.age)


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print("----taks 2------")
print()
print()

class Animal: #creating class
    speak = ''
    def __init__(self, name):
     self.name = name
     

class Dog: #sub class
    speak = 'wolf'
   

    
     

dony2 = Animal("Dog:bark" ) 
print(dony2.name)

print()

class Cat:#sub class
    speak = 'meow'
   

    
     

dony3 = Animal("Cat:meow" )
print(dony3.name)



           
        

                 
      

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

print("----taks 3------")
print()
print()


class BankAccount:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance

# a function using self and amount for both depositing and withdrawing
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        
        else:
            print("Not enough balance.")

#create an account
account = BankAccount("Donyboi", 75)

#testing
account.deposit(65)
account.withdraw(40)
account.withdraw(205)