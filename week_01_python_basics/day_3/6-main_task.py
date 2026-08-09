# write one program that does all three: takes a string input, prints it reversed, counts and prints the number of vowels, and prints it reformatted as a clean, properly capitalized sentence.
s = input("Enter a string: ")

# Print reversed string
print("Reversed string: ", s[::-1])

# Count and print number of vowels
vowels = "aeiou"
count = 0
for char in s.lower():
    if char in vowels:
        count += 1
print("Number of vowels in the string: ", count)

# Print reformatted sentence
fs = s.strip().lower().title()
print("Formatted sentence: ", fs)