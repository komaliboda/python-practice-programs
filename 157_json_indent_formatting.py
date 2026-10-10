# Program to demonstrate JSON formatting using the indent parameter.

import json

student = {
    "name": "komali",
    "age": 20,
    "branch": "Data Science"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    result = json.load(file)

print(student)