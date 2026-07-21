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

# pattern 3 : decreasing the number pattern 
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()

# Pattern 4: Reverse Increasing Triangle
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end = " ")
    print()