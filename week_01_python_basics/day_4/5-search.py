names = [ "tayyab", "ali", "ahmed", "hassan", "bilal" ]

search = input("Enter a name to search: ")

if search in names:
    print(f"{search} is found in the list.")
else:
    print(f"{search} is not found in the list.")
