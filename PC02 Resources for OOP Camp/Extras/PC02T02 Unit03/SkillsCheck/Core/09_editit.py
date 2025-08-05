# Edit this program by defining a class called Enemy
# - Inherit the HasHealth and CanJump interfaces
# - Add a constructor which sets a health instance variable to 3
# - Override the jump instance function
#   = It should output "Jumping on the character"
# - Override the get_health instance function
#   = It should return the health instance variable
# - Override the hit instance function
#   = It should remove the amount parameter from their health instance variable
# Test this class by instantiating an Enemy object and call its jump/hit/get_health instance functions to test
from abc import ABC, abstractmethod


class CanJump(ABC):
    @abstractmethod
    def jump(self):
        pass


class CanWalk(ABC):
    @abstractmethod
    def walk(self):
        pass


class HasHealth(ABC):
    @abstractmethod
    def get_health(self) -> int:
        pass

    @abstractmethod
    def hit(self, amount: int):
        pass


class Character(CanWalk, HasHealth):
    def __init__(self, starting_health: int):
        self.health = starting_health

    def walk(self):
        print("Walking across the map")

    def get_health(self) -> int:
        return self.health

    def hit(self, amount: int):
        self.health -= amount


player = Character(20)
player.walk()
player.hit(4)
print(f"The player has {player.get_health()} points of health left")
