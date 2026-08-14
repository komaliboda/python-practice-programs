# Find the second smallest number in the list
num = [10, 30, 40, 20, 5]

first_shortest = num[0]
second_shortest = float("inf")

for i in num:
    if i < first_shortest:
        second_shortest = first_shortest
        first_shortest = i
    elif i < second_shortest:
        second_shortest = i

print(second_shortest)