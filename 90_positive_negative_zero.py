# Separate positive and negative numbers into two lists

numbers = [10,20,-10,-3,50]
positive_list = []
negative_list = []

for i in numbers:
    if i > 0:
        positive_list.append(i)
    else:
        negative_list.append(i)

print(positive_list)
print(negative_list)