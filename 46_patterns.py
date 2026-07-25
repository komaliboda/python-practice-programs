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
    
# Pattern 12: Increasing Alphabet Triangle 
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end= " ")
    print()

# Pattern 13: Floyd's Triangle
num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end = " ")
        num = num+1
    print()
# Pattern 14: Floyd's Alphabet Triangle
num = 1
for i in range(1,6):
    for j in range(i):
        print(chr(64+num),end = " ")
        num = num+1
    print()

# Pattern 15: Repeated Alphabet Triangle
for i in range(1,6):
    for j in range(i):
        print(chr(64+i),end = " ")
    print()

# Pattern 16: Expanding Increasing Alphabet Triangle (Reverse Start)
for i in range(5,0,-1):
    for j in range(i,6):
        print(chr(64+j),end = " ")
    print()

# Pattern 17: Inverted Increasing Alphabet Triangle
for i in range(6,1,-1):
    for j in range(1,i):
        print(chr(64+j),end = " ")
    print()

# Pattern 18: Increasing Star Triangle
for i in range(1,6):
    for j in range(i):
        print("*" ,end=" ")
    print()

# Pattern 19: Inverted Star Triangle
for i in range(1,6):
    for j in range(6,i,-1):
        print("*" ,end=" ")
    print()

# Pattern 20: Right-Aligned Star Triangle

for i in range(1,6):
    for j in range(5,i,-1):
        print("",end = "")
    for k in range(i):
        print("*" ,end=" ")
    print()

# Pattern 21: Inverted Right-Aligned Star Triangle
for i in range(1,6):
    for j in range(1,i):
        print("",end = " ")
    for k in range(6,i,-1):
        print("*",end = " ")
    print()
# Pattern 22: Full Pyramid Star Pattern
for i in range(1,6):
    for j in range(5,i,-1):
        print("",end = " ")
    for k in range(2*i-1):
        print("*",end = " ")
    print()

# Pattern 23: Inverted Full Pyramid Star Pattern
for i in range(4,-1,-1):
    for j in range(5,i,-1):
        print(" ",end = " ")
    for k in range(2 *i + 1):
        print("*",end = " ")
    print()

# Pattern 24: Diamond Star Pattern

for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end = " ")
    for k in range(2*i-1):
        print("*",end = " ")
    print()
for i in range(3,-1,-1):
    for j in range(5,i,-1):
        print(" ",end = " ")
    for k in range(2*i+1):
        print("*",end = " ")
    print()

# Pattern 25: Hollow Pyramid Star Pattern

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end = " ")
    for k in range(2*i-1):
        if  k == 0 or k == 2*i-2  or i == 5:
            print("*",end = " ")
        else:
            print(" ",end = " ")

    print()

# Pattern 26: Hollow Inverted Pyramid Star Pattern

for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(" ",end = " ")
    for k in range(2*i-1):
        if i == 5 or k == 0 or k == 2*i-2:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
    

    

    

    