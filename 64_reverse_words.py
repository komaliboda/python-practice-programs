# Reverse the order of words in a sentence
s = "i love python"
s1 = s.split()
for i in range(len(s1)):
    print(s1[len(s1)-1-i],end = " ")