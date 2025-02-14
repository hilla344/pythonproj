
height=int(input("Enter your height in metres: "))
weight=int(input("Enter your weight in kilograms: "))

BMI=float(weight/(height*height))
print("Your BMI is:",BMI)
if BMI < 18.5:
    print("you're underweight")
elif BMI >= 18.5 and BMI <= 25:
    print("you are normal")
elif BMI >= 25 and BMI <= 30:
    print("you are overweight")
else:
    print("you are obese")