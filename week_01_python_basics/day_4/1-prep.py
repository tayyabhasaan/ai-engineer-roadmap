# list 
fruits = ["apple", "banana", "cherry"]

# indexing & slicing
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
print(fruits[1:3])  # Output: ['banana', 'cherry']

# Core list methods
print("fruit.append(\"apple\")=> ", fruits.append("apple"))              # Adds "apple" to the end of the list
print("fruit.remove(\"banana\")=> ", fruits.remove("banana"))            # Removes "banana" from the list
print("fruit.insert(1, \"grapes\")=> ", fruits.insert(1, "grapes"))      # Inserts "grapes" at index 1
print("fruit.pop()=> ", fruits.pop())                                # Removes and returns the last item in the list
print("fruit.pop(0)=> ", fruits.pop(0))                              # Removes and returns the item at index 0
print("fruit.sort()=> ", fruits.sort())                              # Sorts the list in ascending order
print("fruit.reverse()=> ", fruits.reverse())                        # Reverses the order of the list
print("len(fruits)=> ", len(fruits))                                 # Returns the number of items in the list

# checking membership and looping
print("apple" in fruits)  # Output: true
for fruit in fruits:
    print(fruit)  # Output: apple, grapes, cherry

# Mutability
fruits[0] = "kiwi"  # Modifies the first item in the list
