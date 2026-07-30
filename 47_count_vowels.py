# Count the number of vowels in a string

s = input("enter something: ").lower()
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:
        count += 1
print("The count is :",count)