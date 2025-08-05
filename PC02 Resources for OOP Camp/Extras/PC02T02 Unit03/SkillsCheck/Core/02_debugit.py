# Fix the errors in this program
# - It should define an abstract class called Vehicle which contains an abstract function
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(top_speed: float):
        self.top_speed = top_speed

    @abstractmethod
    def speed_up(amount: float):
        pass
