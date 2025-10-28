# """
# Identify the potential errors in the following code snippets and modify 
# them to include appropriate try/except blocks to handle exceptions gracefully.
# """


"""
Example 1: Division
"""
print("-----task 1------")
print()

def divide_numbers(num1, num2):
    try: #trying to divide the numbers
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError: #catching the zero division error
        print("you cant divide by zero")#give a message instead of a error code

# # Example usage:
# divide_numbers(10, 0)


"""
Example 2: Opening Files
"""
print("-----task 2------")
print()

def read_file(filename):
    try:#trying to open the file
    
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except:#catching all errors
        print("file does not exist")#give a message instead of a error code

# # Example usage:
# read_file("nonexistent.txt")

"""
Example 3: List Items
"""
print("-----task 3------")
print()


def get_item(lst, index):
    try:#trying to get the item
        item = lst[index]
        print("Item:", item)
    except IndexError:#catching the index error
        print("this item isnt on the list")#give a message instead of a error code


# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)
    


"""
Example 4: Dictionaries
"""
print("-----task 4------")
print()


def get_value(dictionary, key):
    try:#trying to get the value
        value = dictionary[key]
        print("Value:", value)
    except:#catching all errors
        print("key does not exist")#give a message instead of a error code

# # Example usage:
# my_dict = {"a": 1, "b": 2}
# get_value(my_dict, "c")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
print("-----task 5------")
print()
def process_file(filename):
    try:#trying to open the file
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:#catching the file not found error
        print("Error: File not found.")
    else:#if no errors occur
        print("File found successfully.")
    finally:
        print("try completed.")

# # Example usage:
# process_file("example.txt")