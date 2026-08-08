# Find the shortest word in a sentence

s = "i love python "
s1 = s.split()
shortest_word = s1[0]
min_length = len(s1[0])
for word in s1:
    if len(word) < min_length:
        min_length = len(word)
        shortest_word = word
print("The shortest word is :", shortest_word)
print("min Length is :",min_length)