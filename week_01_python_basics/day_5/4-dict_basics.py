person = {"name": "Tayyab", "age": 23, "university": "NUML"}

print("Person's name:", person["name"])  # Output: Tayyab
print("Person's age:", person["age"])    # Output: 24
print("Person's university:", person["university"])  # Output: NUML
person["age"] = 24  # Update age
print("Updated age:", person["age"])    # Output: 24

person["email"] = "tayyabhasaan0118@gmail.com"  # Add new key-value pair
print("Person's email:", person["email"])  # Output: tayyabhasaan0118@gmail.com

print(person.items())  # Output: dict_items([('name', 'Tayyab'), ('age', 24), ('university', 'NUML'), ('email', 'tayyabhasaan0118@gmail.com')])

for key, value in person.items():
    print(f"{key}: {value}")  # Output: name: Tayyab, age: 24, university: NUML, email: tayyabhasaan0118@gmail.com