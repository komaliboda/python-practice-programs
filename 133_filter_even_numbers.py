# Filter even numbers from a list using filter and lambda

numbers = [1,2,3,4,5,6]
result = filter(lambda n: n%2 == 0,numbers)

print(list(result))