# Demonstrate Hierarchical Inheritance in Python
# Multiple child classes inherit from one parent class.

class Parent:
    def display(self):
        print("mom is saying that: ")
class Son(Parent):
    def play(self):
        print("her son is playing")
class Daughter(Parent):
    def dance(self):
        print("her daughter is dancing")
s = Son()
s.display()
s.play()
d = Daughter()
d.display()
d.dance()