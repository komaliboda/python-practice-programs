# Neon Number
# This program checks whether a given number is a Neon Number using a while loop.

num = int(input("enter a num:"))
temp = num
square = num*num
total = 0
while square > 0:
    last_digit = square%10
    total = total + last_digit
    square //= 10
if num == total:
    print("Neon number")
else:
    print("Not a neon number")
    