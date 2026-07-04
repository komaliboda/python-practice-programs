# Electricity bill calculator 

# Taking units from the user
units = int(input("enter units :"))
if units <= 100:
    bill = units* 1.5
elif units <= 200:
    unit = units - 100
    bill = 100* 1.5+unit* 2.5
else:
    unit = units - 200
    bill = 100* 1.5+100* 2.5+unit* 4
print("Total Bill : ", bill)
    
    