# Use list comprehension with if-else to check even numbers

numbers = [1,2,3,4,5,6]
result = [n  if n%2 == 0 else 0 for n in numbers]
print(result)