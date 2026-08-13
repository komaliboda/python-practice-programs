# Removing duplicate values from the list

num1 = [10,20,40,20,10]

num = []

for i in num1:
    if i not in num:
        num.append(i)
print(num)
        