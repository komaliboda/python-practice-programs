# Reverse a list using indexing without reverse() or slicing

num = [10,20,30]
reverse_list = []

for i in range(len(num)):
    nums = num[len(num)-1-i]
    reverse_list.append(nums)

print(reverse_list,end = "")