# Count the frequency of each character in a string using a dictionary

s = "banana"
freq = {}
for i in s:
    if i not in freq:
        freq[i] = s.count(i)

print(freq)
        