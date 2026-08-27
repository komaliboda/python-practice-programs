# Calculate the sum of numbers from 1 to n using recursion

def add(n):
    
    if n == 0:
        return 0
    
    return n + add(n-1)

print(add(5))