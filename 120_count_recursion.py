# Print numbers from n down to 1 using recursion

def count(n):
    if n == 0:
        return 
    print(n)
    return count(n-1)

print(count(3))