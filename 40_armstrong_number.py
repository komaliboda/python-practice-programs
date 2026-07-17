# Armstrong Number
# This program checks whether a given number is an Armstrong number using a while loop.
num  = int(input("enter a num: "))
count = 0
total = 0
same = num
temp = num
while num > 0:
    count += 1
    num //= 10
while temp > 0:
    last_digit = temp%10
    arm = (last_digit)**count
    total = total + arm
    temp //= 10
if total == same:
    print(same,"is a armstrong number")
else:
    print(same,"This is not a armstrong number")

    
    
    