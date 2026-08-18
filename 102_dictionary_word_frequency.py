# Count the frequency of each word in a sentence using a dictionaryp

s = "apple mango apple mango banana"
word = s.split()
freq = {}

for i in word:
    if i not in freq:
        freq[i] = word.count(i)

print(freq)