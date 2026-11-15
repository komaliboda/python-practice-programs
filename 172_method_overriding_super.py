# Demonstrate Method Overriding and super() in Python
# The Dog class overrides the sound() method of Animal.
# super() calls the parent class method before executing
# the child class method.

class Animal:
    def sound(self):
        print("Animal makes sound ")
class dog(Animal):
    
    def sound(self):
        super().sound()
        print("Dog barks")
a1 = dog()
a1.sound()