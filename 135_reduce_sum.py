# Calculate the sum of all numbers using reduce and lambda

from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda a,b: a+b, numbers )

print(result)