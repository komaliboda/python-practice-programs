# Check whether a file exists using os.path.exists()

with open("student.txt","w") as file:
    print(file.write("komali"))

import os

if os.path.exists("student.txt"):
    print("File exists")
else:
    print("file doesn't exist)