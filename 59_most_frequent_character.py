# Find the most frequent character in a string

s = input("Enter something: ")
max_count = 0
max_char = ""
for ch in s:
    if max_count < s.count(ch):
        max_count = s.count(ch)
        max_char = ch
print(max_char,max_count)

        
    