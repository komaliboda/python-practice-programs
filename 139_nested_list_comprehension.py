# Filter even numbers from a nested list using list comprehension

numbers = [[1,2],[3,4]]
result = [n for row in numbers for n in row if n%2 == 0]

print(result)