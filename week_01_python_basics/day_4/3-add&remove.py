from os import remove


list = []

print("list => ", list)  # Output: []
list.append("apple")
list.append("banana")
list.append("pineapple")
list.append("peach")

print("list after appending 4 items => ", list)  # Output: ['apple', 'banana', 'pineapple', 'peach']

list.remove("banana")
print("list after removing banana => ", list)  # Output: ['apple', 'pineapple', 'peach']

list.pop()
print("list after popping last item => ", list)  # Output: ['apple', 'pineapple']
