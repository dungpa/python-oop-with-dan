# Add docstrings to the defined class and its instance functions
import random


class Dice:
    def __init__(self, num_sides: int):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

    def roll_multiple(self, number: int):
        total = 0
        for _ in range(number):
            total += self.roll()
        return total
