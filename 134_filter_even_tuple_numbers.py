# Filter even numbers from a tuple using a function and filter

def is_even(n):
    return n % 2 == 0

numbers = (1,2,3,4,5)
result = filter(is_even, numbers )

print(tuple(result))