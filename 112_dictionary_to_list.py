# Convert dictionary keys, values, or key-value pairs into lists

student = {
    "name": "Komali",
    "age": 20,
    "course": "Python"
}

keys = list(student.keys())
values = list(student.values())
items = list(student.items())

print("Keys:", keys)
print("Values:", values)
print("Key-value pairs:", items)