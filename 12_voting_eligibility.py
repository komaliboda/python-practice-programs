# Voting eligibility system 

age = int(input("enter your age: "))

if age < 0 :
    print("Invalid age")
elif age > 100:
    print("Invalid age")
elif age > 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote ")