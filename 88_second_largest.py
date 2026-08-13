#Find the second largest number in the list

num = [10,30,20]
first_max = 0
second_max = 0

for i in num:
    
    if i > first_max:
        second_max = first_max
        first_max = i
  
    elif i > second_max:
        second_max = i

print(second_max)
 