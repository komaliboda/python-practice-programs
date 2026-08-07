# Check whether two strings are rotations of each other

s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

if len(s1) == len(s2):
    s3 = s1 + s1
    if s2 in s3:
        print("Rotation")
    else:
        print("Not Rotation")
else:
    print("Not Rotation")