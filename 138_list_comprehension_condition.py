# Calculate squares of even numbers using list comprehension

numbers = [1,2,3,4,5]
result = [n*n for n in numbers if n%2 == 0]

print(result)