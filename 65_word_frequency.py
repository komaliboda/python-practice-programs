# Count the frequency of each word in a sentence

s = "i love python and i love java"
s1 = s.split()
t = ""

for words in s1:
    if words not in t:
        t += words
        print(words,s1.count(words))
    