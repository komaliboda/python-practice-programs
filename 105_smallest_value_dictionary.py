# Find the key with the smallest value in a dictionary

s = {
    "math" : 75,
    "english " : 70,
    "social" : 80
     }
smallest_marks = s["math"]
subject= ""

for key,values in s.items():
    
    if values < smallest_marks:
        smallest_marks = values
        subject = key

print(subject,smallest_marks)
