# find the smallest of three numbers 
a = int(input("Enter a number 1:  "))
b = int(input("Enter a number 2: "))
c = int(input("Enter a number 3: "))

if a == b and b == c:
    print("Three numbers are same")
elif a<=b and a<=c:
    print("a is smaller ")
elif b<=a and b<=c:
    print("b is smaller ")
else:
    print("c is smaller ")