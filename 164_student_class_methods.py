# Create a Student class using __init__() and display student details using a method

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("name: ",self.name)
        print("marks: ",self.marks)
    def check_result(self):
        if self.marks >= 35:
            print("pass")
        else:
            print("fail")

student1 = student("komali",85)
student2 = student("vishnu",92)
student1.display()
student2.display()
student1.check_result()
student2.check_result()
