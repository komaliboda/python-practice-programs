# Count the number of vowels and the consonants of the string

s = input("enter something : ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for i in s:
    if i in vowels:
        vowel_count += 1
    elif i.isalpha():
        consonant_count += 1
print("The  vowel count is :",vowel_count)
print("The consonant count is :", consonant_count)