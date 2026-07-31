# Find the first non-repeating character in a string

s = "komali"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
  
  