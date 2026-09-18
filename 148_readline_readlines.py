# Read lines from a file using readline and readlines

with open("student.txt","w") as file:
    file.write("komali\n")
    file.write("koti\n")
    file.write("siddu\n")
    file.write("vishnu\n")

with open("student.txt","r") as file:
    print(file.readline())
    print(file.readlines())
    