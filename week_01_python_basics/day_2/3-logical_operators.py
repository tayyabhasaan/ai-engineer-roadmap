# Logical operators — ask the user for their age (input → int) and whether they have a student ID (input → compare to "yes" to get a bool). Print whether they qualify for a student discount (must be under 25 and have a valid ID).

# Taking age as input
age = int(input("Enter your age: "))
student_id = bool(input("Enter you student id: "))

if age < 25 and student_id:
    print("You qualify for 20% student discount.")
elif age < 25 or student_id:
    print("You qualify for 10% student discount.")
elif age >= 25 and not student_id:
    print("You do not qualify for any student discount.")
    