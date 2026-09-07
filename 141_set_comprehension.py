# Create a set of unique even numbers using set comprehension

numbers = [1,2,2,2,3,3,4,5,6]
result = {n for n in numbers  if n%2 == 0}

print(result)