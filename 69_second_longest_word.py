# Find the second longest word in a sentence

s = "i love python"
s1 = s.split()
second_longest = ""
first_longest = ""
max_length = 0
second_length = 0
for i in s1:
    if len(i) > max_length:
        second_longest = first_longest
        second_length = max_length
        first_longest = i
        max_length = len(i)

    elif len(i) > second_length:
        second_longest = i
        second_length = len(i)
print(second_longest)
   
     
