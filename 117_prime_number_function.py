# Check whether a number is prime using a function

def prime(n):
    if n < 2:
        return False
    is_prime = True
    for i in range(2,n):
        if n%i == 0:
            is_prime = False
            break
    return is_prime
print(prime(7))
            