# Demonstrate file pointer position using tell and seek

with open("student.txt","w") as file:
    print(file.write("komali"))


with open("student.txt","r") as file:
    print(file.read(3))
    print(file.tell())
    file.seek(0)
    print(file.read(3))