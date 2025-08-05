# Fix the errors in this program
from abc import ABC, abstractmethod


class Chair(ABC):
    def init(self, num_legs: int, material: str:
        num_legs = num_legs
        material = material

    @abstractmethod
    def sit(self):
        pass


class OfficeChair(Chair):
    def sit(self):
        print(f"This nice office chair has {self.num_legs} legs and is made from {self.material}")


chair = OfficeChair(5, "leather")
chair.sit()
