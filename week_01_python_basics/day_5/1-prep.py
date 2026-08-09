# tuples - like lists, but immutable (can't be changed after creation). Use when data should not be modified.
points = (1, 2, 3, 4, 5)
points[0]  # Output: 1



# sets - unordered collections of unique items. Use when you need to store unique items and don't care about order.
nums = {1, 2, 3, 2, 1}
print(nums)  # Output: {1, 2, 3}
nums.add(4)  # Adds 4 to the set
nums.remove(1)  # Removes 1 from the set
print(nums)  # Output: {2, 3, 4}
print("3 in nums:", 3 in nums)  # Output: True



# Dictionaries - key-value pairs. Use when you need to associate values with unique keys.
person = {"name": "Tayyab", "age": 23, "city": "Lahore"}
print(person["name"])  # Output: Tayyab
person["age"] = 24  # Update age
person["country"] = "Pakistan"  # Add new key-value pair
print(person)  # Output: {'name': 'Tayyab', 'age': 24, 'city': 'Lahore', 'country': 'Pakistan'}

del person["city"]  # Remove key-value pair
print(person)  # Output: {'name': 'Tayyab', 'age': 24, 'country': 'Pakistan'}

person_keys = person.keys()  # Get all keys
person_values = person.values()  # Get all values

person.items()  # Get all key-value pairs as tuples

for key, value in person.items():
    print(f"{key}: {value}")  # Output: name: Tayyab, age: 24, country: Pakistan

print('"name" in person:', "name" in person)  # Check if key exists, Output: True