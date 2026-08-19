# Find the key with the highest value in a dictionary

s = {
    "math" : 75,
    "english " : 70,
    "social" : 80
     }
highest_marks = 0
subject= ""

for key,values in s.items():
    
    if values > highest_marks:
        highest_marks = values
        subject = key

print(subject,highest_marks)
