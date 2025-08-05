# Fix the errors in this program
from abc import ABC, abstractmethod


class Chair(ABC):
    def __init__(self, num_legs: int):
        self.num_legs = num_legs

    @abstractmethod
    def sit(self):
        pass


class Stool:
    def __init__(self):
        Chair.__init__(self, 3)

    def sit(self):
        print("Sitting on a stool")


my_stool = Chair()
my_stool.sit()
