# Demonstrate append and read operations using a+ file mode

names = ["komali\n","siddu\n","koti\n","vishnu\n"]

with open("student.txt","r+") as file:
    print(file.writelines(names))
    file.seek(0)
    print(file.readline())


