contact = {"tayyab": "03134750371", "muneeb": "03104512229", "papa": "03015866470"}

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. View Contacts")
    print("4. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice in ("1", "add"):
        name = input("Enter contact name: ").strip().lower()
        number = input("Enter contact number: ").strip()

        if name and number:
            contact[name] = number
            print(f'Contact "{name}" with number "{number}" has been added.')
        else:
            print("Name and number cannot be empty.")

    elif choice in ("2", "remove", "delete"):
        name = input("Enter contact name: ").strip().lower()

        if name in contact:
            del contact[name]
            print(f'Contact "{name}" has been removed.')
        else:
            print(f'Contact "{name}" does not exist.')

    elif choice in ("3", "view"):
        if not contact:
            print("Your contact book is empty.")
        else:
            print("Your contacts:")
            for name, number in contact.items():
                print(f"{name}: {number}")

    elif choice in ("4", "quit", "exit"):
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose from add, remove, view, or quit.")
