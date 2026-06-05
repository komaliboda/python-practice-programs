# Simple intrest program
 
amount = int(input("enter amount : "))
time = int(input("enter time : "))
interest = int(input("enter intrest rate: "))
 
simple_interest = (amount*time*interest)/100
total = amount+simple_interest
print("Total Amount: ", total)

#Advanced simple intrest

amount = int(input("enter amount : "))
month = int(input("enter months : "))/12
days = int(input("enter days : "))/365
time = month+days
interest = int(input("enter intrest rate: "))
simple_interest = (amount*time*interest)/100
total = amount+simple_interest
print("Total Amount: ", total)
