# Find duplicate elements in a list

numbers = [10, 20, 10, 10, 20, 30]
temp = []
duplicates = []

for i in numbers:
    if i not in temp:
        temp.append(i)
    elif i not in duplicates:
        duplicates.append(i)

print("Duplicate elements:", duplicates)