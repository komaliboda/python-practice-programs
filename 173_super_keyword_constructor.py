# Demonstrate super() with Constructor in Python
# The Student class inherits from the Person class.
# super().__init__(name) calls the parent class constructor.
# The child class initializes its own roll number.


class person:
    def __init__(self,name):
        self.name = name
class student(person):
    
    def __init__(self,name,roll_no):
        
        super().__init__(name)
        self.roll_no = roll_no
        
student1 = student("komu",7)
print(student1.name,student1.roll_no)