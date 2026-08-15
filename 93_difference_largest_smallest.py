# Find the difference between the largest and smallest elements in a list

numbers = [10,20,30,40,50]
largest = 0
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
for i in numbers:
    if i < shortest:
        smallest = i
print("The difference between largest and smallest is ",largest-smallest)
    
    