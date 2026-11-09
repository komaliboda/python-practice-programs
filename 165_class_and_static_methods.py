# Demonstrate class methods and static methods using a Student class

class student:
    college = "malineni"
    @classmethod
    def change_name(cls,name):
        cls.college = name
        print(cls.college)
    @staticmethod
    def marks_check(marks):
        if marks >= 0 and marks <= 100:
            print("Valid marks")
        else:
            print("Invalid marks")
student1 = student()
student1.change_name("abc college ")
student.change_name("xyz college ")
student.marks_check(10)
print(student.college)    