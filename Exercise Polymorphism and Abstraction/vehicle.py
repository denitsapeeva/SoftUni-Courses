from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 0.9

    def drive(self, distance):
        all_consumption = (self.fuel_consumption + self.INCREASED_FUEL_CONSUMPTION) * distance
        if self.fuel_quantity >= all_consumption:
            self.fuel_quantity -= all_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 1.6

    def drive(self, distance):
        all_consumption = (self.fuel_consumption + self.INCREASED_FUEL_CONSUMPTION) * distance
        if self.fuel_quantity >= all_consumption:
            self.fuel_quantity -= all_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel*0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)