a = input("Enter first value: ")
op = input("Select Operator. (+, -, *, /): ")
b = input("Enter second value: ")

if op == "+":
    print(f"{a} + {b} = {int(a) + int(b)}")
elif op == "-":
    print(f"{a} - {b} = {int(a) - int(b)}")
elif op == "*":
    print(f"{a} * {b} = {int(a) * int(b)}")
elif op == "/":
    print(f"{a} / {b} = {int(a) / int(b)}")