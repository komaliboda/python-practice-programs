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

# Pattern 5: Decreasing Repeated Number Pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end = " ")
    print()

# Pattern 6: Increasing Inverted Repeated Number Pattern
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end = " ")
    print()

# Pattern 7: Reverse Increasing Number Triangle
for i in range(6,1,-1):
    for j in range(i-1,6):
        print(j,end = " ")
    print()

# Pattern 8: Inverted Increasing Number Pattern
for i in range(1,6):
    for j in range(1,7-i):
        print(j,end = " ")
    print()

# Pattern 9: Inverted Decreasing Number Pattern
for i in range(6):
    for j in range(5,i,-1):
        print(j,end =" ")
    print()

# Pattern 10: Expanding Reverse Number Triangle
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end =" ")
    print()

# Pattern 11: Expanding Decreasing Number Triangle
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end= " ")
    print()
    