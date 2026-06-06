# checking the largest of two number 

# Taking a number from the user
num1 = int(input("enter a number 1 : "))
num2 = int(input("enter a number 2 : "))

if num1 > num2:
    print("The largest  number is ", num1)
elif num2 > num1:
    print("The  latgest number is ", num2)
else: 
    print("num 1 and num 2 are same")