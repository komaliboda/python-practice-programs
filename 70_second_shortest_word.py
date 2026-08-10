# Find the second shortest word in a sentence

s = "i love python"
words = s.split()

first_shortest = words[0]
second_shortest = ""

first_length = len(words[0])
second_length = float("inf")

for word in words:
    if len(word) < first_length:
        second_shortest = first_shortest
        second_length = first_length
        first_shortest = word
        first_length = len(word)
    elif len(word) < second_length and len(word) != first_length:
        second_shortest = word
        second_length = len(word)

print("second shortest:", second_shortest)

