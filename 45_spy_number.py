# Spy Number
# This program checks whether a given number is a Spy Number using a while loop.

num = int(input("enter a num: "))
temp1 = num
temp2 = num
total = 0
product = 1
while temp1 > 0:
    last_digit = temp1 % 10
    total = total + last_digit
    temp1 //= 10
while temp2 > 0:
    last_digit = temp2 % 10
    product = product * last_digit
    temp2 //= 10
if total == product:
    print("Spy number")
else:
