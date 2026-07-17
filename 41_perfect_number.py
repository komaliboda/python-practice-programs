# Perfect Number
# This program checks whether a given number is a Perfect Number using a for loop.
num = int(input("enter a num: "))
total = 0
for i in range(1,num):
    if num %i == 0:
        print(i)
        total = total+i
if num == total:
    print("perfect number ")
else:
    print("not perfect number ")
    