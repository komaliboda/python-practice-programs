# Find the least frequent character in a string

s = "apple"
min_count = s.count(s[0])
min_char = s[0]

for ch in s:
    if s.count(ch) < min_count:
        min_count = s.count(ch)
        min_char = ch

print(min_char, min_count)