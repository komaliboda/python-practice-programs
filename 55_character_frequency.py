# Count the frequency of each character in a string without printing duplicates

s = "banana"
t = ""
for ch in s:
    if not ch in t:
        t += ch
        print(ch,"-"*4,s.count(ch))