# This program calculates your BMI (body mass index)

height = float(input("What is your height in m?"))
weight = float(input("What is your weight in kg?"))

BMI = weight / (height ** 2)
BMI = "{:.2f}".format(BMI)
BMI = float(BMI)

if BMI <= 18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI} and you are a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI} and you are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI} and you are obese")
else:
    print(f"Your BMI is {BMI} and you are clinically obese")

