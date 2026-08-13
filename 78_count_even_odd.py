numbers = [10, 20, 30, 40]
even_count = 0
odd_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)