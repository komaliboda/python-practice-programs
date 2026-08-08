# Find the longest word in a sentence

s = "i love python "
s1 = s.split()
longest = ""
max_length = 0 
for word in s1:
    if len(word) > max_length:
        max_length = len(word)
        longest = word
print("Longest word is :",longest)
print("max Length is :",max_length)