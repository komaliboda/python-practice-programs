# Find common elements between two lists

num1 = [10,20,40]
num2 = [20,30,40]
num = []

for i in num1:
    if i in num2:
        num.append(i)

print(num)
        