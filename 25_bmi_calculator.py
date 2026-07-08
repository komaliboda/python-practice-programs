# BMI (Body Mass Index) Calculator
# This program calculates BMI and displays the health category.

weight = int(input("Enter your weight: "))
height = float(input("Enter your height:  "))
bmi = weight/(height*height)
print("BMI: ",round(bmi,2)
if bmi < 18.5:
    print("Category: under weight ")
elif bmi < 24.9:
    print("Category: Normal")
elif bmi < 29.9:
    print("Category: overweight")
else:
    print("Category: obese")
    