# Edit this program by overriding the make_reservation abstract function in the Restaurant class
# - It should check if the date parameter is already in the reservations list
#   = If so, it should output "There is already a reservation for that date"
#   = Otherwise, it should append that date to the reservations list and output "That date is now booked"
from abc import ABC, abstractmethod


class Reservable(ABC):
    @abstractmethod
    def make_reservation(self, date: str):
        pass


class Building(ABC):
    def __init__(self, address: str, name: str):
        self.address = address
        self.name = name

    @abstractmethod
    def view(self):
        pass


class Restaurant(Building, Reservable):
    def __init__(self, address: str, name: str):
        Building.__init__(self, address, name)
        self.reservations = []

    def view(self):
        print(f"Viewing the restaurant {self.name} at {self.address}")


bistro = Restaurant("123 Fake Street", "The Meet Plate")
bistro.make_reservation("01/01/1970")
bistro.make_reservation("01/02/1970")
bistro.make_reservation("06/10/1971")
bistro.make_reservation("01/02/1970")
