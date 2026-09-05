# Create a dictionary of even numbers and their squares using nested dictionary comprehension

numbers = [[1,2],[3,4]]
result = {n: n*n  for row in numbers for n in row if n%2 == 0}

print(result)