# checking the largest of three number 

# Taking a numbers from the user
num1 = int(input("enter a number 1 : "))
num2 = int(input("enter a number 2 : "))
num3 = int(input("enter a number 3 : "))

if num1 >= num2 and num1 >= num3:
    print("The largest  number is ", num1)
elif num2 >=  num1 and num2 >= num3:
    print("The  latgest number is ", num2)
else: 
    print("The largest number is ",num3)