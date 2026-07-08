# BMI (Body Mass Index) Calculator
# This program calculates BMI and displays the health category.

weight = int(input("Enter your weight: "))
height = float(input("Enter your height:  "))
bmi = weight/(height*height)
print(bmi)
if bmi < 18.5:
    print("under weight ")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("overweight")
else:
    print("obese")
    