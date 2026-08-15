# Find elements that appear only once in a list

numbers = [10,20,30,4,10,60,20,4]
unique = []

for i in numbers:
    if numbers.count(i) == 1:
        unique.append(i)

print(unique)