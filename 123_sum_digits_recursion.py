# Calculate the sum of digits using recursion

def sum_of_digit(n):
    if n == 0:
        return 0
    return sum_of_digit(n//10)+(n%10)

print(sum_of_digit(1235))
    
    