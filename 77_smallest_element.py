# Find the smallest element in a list

numbers = [10, 20, 30, 40]

min_element = numbers[0]

for i in numbers:
    if i < min_element:
        min_element = i

print(min_element)