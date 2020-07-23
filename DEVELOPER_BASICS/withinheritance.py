"""Inheritance in Python"""
class Automobile():
    '''Base class'''
    def __init__(self, price=None, colour=None):
        self.price = price
        self.colour = colour

    def show_vehicle_name(self):
        '''display vehicle name'''
        print("Vehicle name is :", end=' ')

class Bike(Automobile):
    '''for class Bike'''
    def __init__(self, price, colour, mileage):
        super().__init__(price, colour)
        self.mileage = mileage

        super().show_vehicle_name()

    def __str__(self):
        return 'Bike'


class Car(Automobile):
    '''for class Car'''
    def __init__(self, price, colour, servicecharge):
        super().__init__(price, colour)
        self.servicecharge = servicecharge

        super().show_vehicle_name()

    def __str__(self):
        return 'Car'

b = Bike(2000, 'red', 18)
print(b)
print(b.price)
print(b.colour)
print(b.mileage)

c = Car(3000, 'blue', 3900)
print(c)
print(c.price)
print(c.colour)
print(c.servicecharge)
