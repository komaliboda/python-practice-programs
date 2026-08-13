# Count the occurrences of a particular number in a list


numbers = [10, 20, 20, 30, 20, 10]
count = 0

particular_number = int(input("enter a particular number to count: "))

for i in numbers:
    if i == particular_number:
        count += 1

print(count)