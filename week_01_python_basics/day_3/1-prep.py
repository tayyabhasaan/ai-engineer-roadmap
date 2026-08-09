word = "Python"
#       012345

# Indexing
print("Indexing in Python")
print("first to last")
print(word[0])  # Output: P
print(word[1])  # Output: y
print(word[2])  # Output: t 
print(word[3])  # Output: h
print(word[4])  # Output: o
print(word[5])  # Output: n

print("last to first")
print(word[-1])  # Output: n
print(word[-2])  # Output: o
print(word[-3])  # Output: h
print(word[-4])  # Output: t
print(word[-5])  # Output: y
print(word[-6])  # Output: P


# Slicing 
print("Slicing in Python")
print(word[0:3])  # Output: Pyt
print(word[3:6])  # Output: hon
print(word[0:6])  # Output: Python

print(word[:3])   # Output: Pyt
print(word[3:6])  # Output: hon

print(word[::-1])  # Output: nohtyP


# Useful string methods
s = "Hello World"

print("Useful string methods")
print(s.lower())  # Output: hello world
print(s.upper())  # Output: HELLO WORLD
print(s.strip())  # Output: Hello World
print(s.replace("World", "Python"))  # Output: Hello Python
print(s.split(" "))  # Output: ['Hello', 'World'] split into a list
print(s.count("l"))  # Output: 3
print(len(s))  # Output: 11


# Concatination & repitation
print("Concatination & repitation")
print("Hi + there = ", "Hi" + " there")  # Output: Hi there
print("Ha * 3 = ", "Ha" * 3)  # Output: HaHaHa


# Membership check
print("Membership check")
print("l" in s)  # Output: True