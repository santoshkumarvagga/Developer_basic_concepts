"""
Composition - how to create complex objects from simpler ones.

Unlike Inheritance, which holds a "is a" relationship; Composition holds "has a" relationship.

Composition is having an object passed as a parameter to another object so that we can have an
abstraction of details of the passing class in the child/destination class. It is more secure when
compared to inheritance model,where we import all of parent class's attributes and
methods exclusively inside child class.

However, we can combine both inheritance and composition,as per needs.

"""


class vehicle:
    """composition class for object car"""

    def __init__(self, price, colour, car=None):
        self.price = price
        self.colour = colour

        self.car = car

        self.cars = []

        self.cars.append(self.car)

    def getvehiclecount(self):
        result = 0
        for c in self.cars:
            result += 1
        return result


class Car:
    """abstract details here"""

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return self.name + " " + str(self.model)


mycar = Car("Innova", "Z+")
a = vehicle(20000, "red", mycar)
print(a.car)
print(a.getvehiclecount())
