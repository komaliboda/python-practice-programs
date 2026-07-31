# Find the first repeating character in a string

s = input("Enter your name: ")
for ch in s:
    if s.count(ch) >= 1:
        print(ch)
        break