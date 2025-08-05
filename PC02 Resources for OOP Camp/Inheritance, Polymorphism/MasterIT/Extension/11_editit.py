# Override the parent's constructor in each of the child classes
# - They should specify the number of sides in their dice
# - Standard dice have 6 sides
# - Tabletop dice have 20 sides
# - Classic dice have 4 sides
# Instantiate one object of each of the children classes and output the result of their 'roll' instance function
import random


class Dice:
    def __init__(self, num_sides: int):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)


class StandardDice(Dice):
    pass


class TabletopDice(Dice):
    pass


class ClassicDice(Dice):
    pass
