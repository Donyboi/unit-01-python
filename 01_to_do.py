print("to do list")
print()
print()

with open ("todo.txt") as file:
    to_do = file.readlines()
    print(to_do)

while True:
    print("Current list:", to_do)
    add_remove = input("Do you want to add, remove, or clear all from your list? ").strip().lower()
    if add_remove == "add":
        item = input("Enter an item to add: ")
        to_do.append(item)




    elif add_remove == "remove":
        item = int(input("Enter an item to remove using numbers: "))
        del to_do[item - 1]
    elif add_remove == "clear all":
        to_do.clear()
        print("All items cleared from the list.")
    else:
        print("Please enter 'add', 'remove', or 'clear all'.")
    print()
    print("--------------")
    print()
