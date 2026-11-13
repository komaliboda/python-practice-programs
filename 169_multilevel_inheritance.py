# Demonstrate Multilevel Inheritance in Python
# Child inherits from Father, and Father inherits from Grandfather.

class grandfather:
    def house(self):
        print("grandfather owns a house 🏠 ")
class father(grandfather):
    def car(self):
        print("father owns a car 🚗 ")
class child(father):
    def bike(self):
        print("child owns a bike")
c1 = child()
c1.house()
c1.car()
c1.bike()

