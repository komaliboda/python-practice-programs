# Palindrome Number
# This program checks whether a given number is a palindrome using a while loop.
num = int(input("Enter a number: " ))
rev = 0
temp = num
while num > 0:
    last_digit = num % 10
    rev = (rev*10)+last_digit
    num //= 10
if temp == rev:
    print(" palindrome Number")
else:
    print("Not a palindrome Number ")