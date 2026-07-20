# pattern 1: number pattern  
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = " ")
    print()

# pattern 2 : repeated number pattern 
for i in range(1,6):
    for j in range(i):
        print(i,end = " ")
    print()