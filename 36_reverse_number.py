# Reverse a Number
# This program reverses a given number using a while loop.

num = int(input("Enter a number: " ))
rev = 0
while num > 0:
    last_digit = num % 10
    rev = (rev*10)+last_digit
    num //= 10
print("The reverse number is",rev)