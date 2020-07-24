'''for abstract class implementation, import ABC'''

from abc import ABC, abstractmethod

class vehicle(ABC):
    '''cannot create instance directly, since it is abstarct class'''
    def __init__(self, tprice = 0, type = 'road'):
        self.type = type
        self.price = 0
        pass

    @abstractmethod
    def pricing(self):
        '''to be implemented by child classes as per requirement'''
        pass

class Bike(vehicle):
    def __init__(self, price, type):
        super().__init__(price, type)

    def pricing(self):
        self.price = price

class Car(vehicle):
    def __init__(self, price, type):
        super().__init__(price, type)

    def pricing(self):
        self.price = price

a = Bike(30000,'water')
print(a.price())

b = Car(400000)
print(b.price())
