# Demonstrate reading, writing, and overwriting a file using file modes

with open("student.txt","w") as file:
    file.write("komali\n")
    file.write("koti\n")
    file.write("siddu\n")
    file.write("vishnu\n")

with open("student.txt","r") as file:
    print(file.readline())
    print(file.readlines())

file = open("student.txt","w")
content = file.write("srinu")
print(content)
file.close()
