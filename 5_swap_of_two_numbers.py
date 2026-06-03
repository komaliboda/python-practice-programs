# swap of two numbers 

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("Before swapping: ")
print("First number: ", num1)
print("Second number: ",num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping: ")
print("First number: ", num1)
print("Second number: ",num2)