# Demonstrate Multiple Inheritance in Python
# A child class inherits methods from two parent classes.

class Father:
    def gardening(self):
        print("Father likes gardening")

class Mother:
    def cooking(self):
        print("Mother likes cooking")

class Child(Father, Mother):
    def playing(self):
        print("child likes playing 😁 ")

c1 = Child()
c1.gardening()
c1.cooking()
c1.playing()