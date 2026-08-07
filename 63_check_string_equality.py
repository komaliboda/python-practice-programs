# Check whether two strings are equal without using the == operator

s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()
if len(s1) == len(s2):
    for ch1,ch2 in zip(s1,s2):
        if ch1 != ch2:
            print("Not Equal")
            break
    else:
        print("Equal")
else:
    print(" Not Equal ")