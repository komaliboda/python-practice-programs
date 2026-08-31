# Check whether numbers are even or odd using a lambda function

check = lambda n :"even" if n%2 == 0 else "odd"

for i in range(1,5):
    
    print(i,check(i))