# Demonstrate Polymorphism in Python
# Two different classes have the same method name (role),
# but each method performs a different action.

class student:
    def role(self):
        print("The student is studying ")

class teacher:
    def role(self):
        print("The teacher is teaching ")

s1 = student()
t1 = teacher()
s1.role()
t1.role()