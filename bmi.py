name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
print(f"Your BMI is {bmi}.")
if bmi < 18.5:
    print(f"{name}, you are underweight.")
elif bmi < 25:
    print(f"{name}, you have a normal weight.")
elif bmi < 30:
    print(f"{name}, you are slightly overweight.")
elif bmi < 35:
    print(f"{name}, you are obese.")
else:
    print(f"{name}, you are clinically obese.")
    
