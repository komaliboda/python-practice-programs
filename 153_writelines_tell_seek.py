# Demonstrate writelines(), readlines(), tell(), and seek() in file handling

names = ["komali\n","siddu\n","koti\n","vishnu\n"]
with open("student.txt","w") as file:
    print(file.writelines(names))
    print(file.write("siddu"))
with open("student.txt","r") as file:
    print(file.readlines())
    print(file.tell())
    print(file.seek(0))