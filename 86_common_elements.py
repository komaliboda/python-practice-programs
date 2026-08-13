# Find common elements between two lists

num1 = [10,20,40]
num2 = [20,30,40]
common = []

for i in num1:
    if i in num2:
        common.append(i)

print(common)
        