# counting a specific character 

s = input("enter something: ").lower()
specific_char = input("Enter a specific character: ").lower()
count = 0
for ch in s:
    if ch in specific_char:
        count += 1
print("The count is :",count)
    