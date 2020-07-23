""" Inheritance in Python"""
"""without inheritance - most of common code across classes will be redundant"""
class Cycle():
    def __init__(self, price, colour, kind):
        self.price = price
        self.colour = colour
        self.kind = kind

class Bike():
    def __init__(self, price, colour, kind):
        self.price = price
        self.colour = colour
        self.kind = kind

class Car():
    def __init__(self, price, colour, kind):
        self.price = price
        self.colour = colour
        self.kind = kind

a = Cycle(5000, 'red', 'street')
b = Bike(100000, 'blue', 'office')
c = Car(1000000, 'white', 'tour')

print(a.price)
print(b.colour)
print(c.kind)