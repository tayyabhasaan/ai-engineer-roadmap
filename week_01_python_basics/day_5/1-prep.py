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
person = {"name": "Alice", "age": 30, "city": "New York"}