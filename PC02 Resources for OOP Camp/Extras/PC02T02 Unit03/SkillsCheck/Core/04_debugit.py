# Fix the errors in this program
# - It defines an interface called Driveable
# - It then defines an abstract class called Vehicle that inherits the Driveable interface
# - It also defines a child class called Bus which inherits from Vehicle and overrides its abstract functions
# - The program instantiates a Bus object and calls its functions to test
from abc import ABC, abstractmethod


class Driveable(ABC):
    @abstractmethod
    def get_fuel(self) -> float:
        pass

    @abstractmethod
    def drive(self, distance: float):
        pass


class Driveable(Vehicle):
    def __init__(self, miles_per_gallon: float):
        self.miles_per_gallon = miles_per_gallon
        self.fuel = 60

    def get_fuel(self) -> float:
        return self.fuel

    @abstractmethod
    def drive(self, distance: float):
        pass


class Bus(Vehicle):
    def drive(self, distance: float):
        print(f"Driving the bus {distance} miles")
        self.fuel -= (distance / self.miles_per_gallon)
        print(f"The bus has {self.fuel} gallons left")


school_bus = Bus(8)
school_bus.drive(20)
school_bus.drive(45)
