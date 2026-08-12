# List methods practice

numbers = [10, 20, 30]

# append()
numbers.append(40)
print("After append:", numbers)

# insert()
numbers.insert(1, 100)
print("After insert:", numbers)

# remove()
numbers.remove(100)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# count()
print("Count of 10:", numbers.count(10))

# index()
print("Index of 20:", numbers.index(20))

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# extend()
numbers.extend([40, 50])
print("After extend:", numbers)

# copy()
new_numbers = numbers.copy()
print("Copied list:", new_numbers)

# clear()
new_numbers.clear()
print("After clear:", new_numbers)