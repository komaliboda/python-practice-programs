# Prime Number
# This program checks whether a given number is prime using a for loop.

num = int(input("Enter a number:"))
is_prime = True
if num <= 1:
    is_prime = False
for i in range(2,num):
    if num%i == 0:
        is_prime = False 
        break
if is_prime:
    print(num," is prime ")
else:
    print("not prime")