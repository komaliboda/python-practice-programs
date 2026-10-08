# Create a new file using x mode without overwriting an existing file

with open("student.txt","x") as file:
    print(file.write("komali"))

