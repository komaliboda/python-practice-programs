# Create a folder using os.mkdir() and a file inside it using file handling

import os
os.mkdir("students")
with open("students/studen.txt","w") as file:
    print(file.write("komali"))