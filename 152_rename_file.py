# Rename a file using the os module

with open("student.txt","w") as file:
    print(file.write("komali"))

import os
os.rename("student.txt","students.txt)
