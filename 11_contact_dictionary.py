print("-----your Contact dictonary-----")
print()
print()


contacts = {}


contacts = {}

while True:
    print("Contact Menu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. List contacts")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number (10 digits): ")
        if len(phone) == 10 and phone.isdigit():
            contacts[name] = phone
            print(f'Contact "{name}" added successfully.\n')
        else:
            print("Invalid phone number. Please enter exactly 10 digits.\n")

    elif choice == "2":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f'Contact "{name}" deleted successfully.')
        else:
            print(f'Contact "{name}" not found.')
    elif choice == "3":
        if contacts:
            print("--- Contact List ---")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
            print("")
        else:
            print("No contacts found.")
    elif choice == "4":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
