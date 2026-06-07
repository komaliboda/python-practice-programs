#--------------------------------------
#project : menu calculator 
#description : performs basic operations
#--------------------------------------

num1 = float(input("Enter the  first number : "))
num2 = float(input("Enter the second number : "))
print("1.add,2.sub,3.multiply,4.divide")

choice = int(input("Enter your choice : ")) 
if choice == 1:
    print("Result",num1+num2)
elif choice == 2:
    print("Result",num1-num2)
elif choice == 3:
    print("Result",num1*num2)
elif choice == 4:
    if num2 != 0:
        print("Result",num1/num2)
    else:
        print("cannot divide by zero ")
else:
    print("Invalid chooce ")