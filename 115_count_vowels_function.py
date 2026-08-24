# Count the number of vowels in a string using a function

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count
print(count_vowels("komali"))
