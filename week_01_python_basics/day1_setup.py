# Variables
# Name = "Tayyab"     # string
# age = 23            # int
# cgpa = 3.5          # float
# is_student = True   # bool

# print
# print("Name:", Name)
# print("Age:", age)
# print("CGPA:", cgpa)
# print("Is Student:", is_student)    

# input
# name = input("Enter your name: ")
# print("Hi!", name)

# f-string
name = input("Enter your name: ")
age = input("Enter your age: ")
cgpa = input("Enter your CGPA: ")
print(f"Hi {name}, your age is {age} and your CGPA is {cgpa}.")

# Type conversion
# taking input from user as string
a = input("Enter a number: ")           
b = input("Enter another number: ")
# converting string to int
A = int(a)
B = int(b)
# adding two numbers
sum = A + B
print("The sum of", A, "and", B, "is:", sum)