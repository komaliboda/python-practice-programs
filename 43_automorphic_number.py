# Automorphic Number
# This program checks whether a given number is an Automorphic Number.

num = int(input("enter a number: "))
s = num*num
temp = num
count = 0
while num > 0:
    count+=1
    num//=10
last_digits = s%(10**count)
print(last_digits)
if temp == last_digits:
    print("automorphic")
else:
    print("not automorphic ")