# Find the largest number in a list using reduce and lambda

from functools import reduce 
numbers = [1,2,3,4,5]
result = reduce(lambda a,b: a if a > b else b, numbers)

print(result)
