weight = input("Enter your weight in kg: ")
height = input("Enter your height in cm: ")

bmi = float(weight) / ((float(height)/100)**2)
print(f"Your BMI is {round(bmi, 2)}.")
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You have a normal weight.")
elif bmi >= 25:
    print("You are overweight.")