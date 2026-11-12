# Demonstrate inheritance in Python using Parent and Child classes

# Access parent class methods through a child class object.

class parent:
    
    def house(self):
        print("parent owns house")

class child(parent):
    def car(self):
        print("child owns a car")
    

c1 = child()
c1.house()
c1.car()