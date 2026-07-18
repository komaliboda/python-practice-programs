# Strong Number
# This program checks whether a given number is a Strong Number using a while loop.

num = int(input("enter a number: "))
temp = num
total = 0

while num > 0:
    fact = 1
    last_digit = num%10
    for i in range(1,last_digit+1):
        fact = fact*i
    total = total+fact
    num//=10
if temp == total:
    print("Strong number ")
else:
    print("not a strong number ")
    
    