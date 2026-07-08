# Income Tax Calculator
# This program calculates income tax based on annual income.

annual_income = int(input("Enter your income: "))
if annual_income < 250000:
    tax = (annual_income * 0)/100
    print("Tax : ",tax)
elif annual_income <= 500000:
    tax = (annual_income * 5)/100
    print("Tax : ",tax)
elif annual_income <= 1000000:
    tax = (annual_income * 20)/100
    print("Tax : ",tax)
else:
    tax = (annual_income * 30)/100
    print("Tax : ",tax)
