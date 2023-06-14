from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, brand):
        pass

    @abstractmethod
    def pass_driving_licence(self):
        pass


class Car(Vehicle):

    def __init__(self, brand):
        self.brand = brand

    def pass_driving_licence(self):
        return 'cat B'

    def __str__(self):
        return self.brand


car = Car('Renault')
print(car)
