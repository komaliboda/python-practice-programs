# Convert a Python dictionary to a JSON string and back using dumps() and loads()

import json

student = {
    "name": "komali",
    "age": 19
}

s = json.dumps(student)
print(s)

s1 = json.loads(s)
print(s1)