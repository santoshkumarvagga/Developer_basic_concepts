""" Inheritance in Python"""
"""without inheritance - most of common code across classes will be redundant"""
class Cycle():
    def __init__(self, price, colour, weight):
        self.price = price
        self.colour = colour
        self.kind = kind

class Bike():
    def __init__(self, price, colour, mileage):
        self.price = price
        self.colour = colour
        self.kind = kind

class Car():
    def __init__(self, price, colour, servicecharge):
        self.price = price
        self.colour = colour
        self.kind = kind

a = Cycle(5000, 'red', 25)
b = Bike(100000, 'blue', 18)
c = Car(1000000, 'white', 15000)

print(a.price)
print(b.colour)
print(c.kind)