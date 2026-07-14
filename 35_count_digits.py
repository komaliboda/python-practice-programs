# Count Digits
# This program counts the number of digits in a given number using a while loop.

num = int(input("Enter a number: " ))
count = 0
while num > 0:
    count += 1
    num //= 10
print("The count of the nuber is",count)