todo = []

while True:
    print("\nTodo Menu")
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice in ("1", "add"):
        item = input("Enter an item to add: ").strip()
        if item:
            todo.append(item)
            print(f'"{item}" has been added to the list.')
        else:
            print("Item cannot be empty.")

    elif choice in ("2", "remove"):
        item = input("Enter an item to remove: ").strip()
        if item in todo:
            todo.remove(item)
            print(f'"{item}" has been removed from the list.')
        else:
            print(f'"{item}" is not in the list.')

    elif choice in ("3", "view"):
        if not todo:
            print("Your todo list is empty.")
        else:
            print("Your todo list:")
            for item in todo:
                print(f"- {item}")

    elif choice in ("4", "quit", "exit"):
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose from add, remove, view, or quit.")
