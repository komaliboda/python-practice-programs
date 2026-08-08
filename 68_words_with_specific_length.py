# Count words with a specific length in a sentence

s = "i lo😂😂ee komali"
specific_length = 6
count = 0
s1 = s.split()
for ch in s1:
  if len(ch) == specific_length:
    count += 1  
    print("The specific length word is :", ch)
print("The count is: ",count)
  