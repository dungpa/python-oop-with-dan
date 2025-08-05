# Fix the errors in this program
# Incorrect docstring syntax in some areas
# And some docstrings are missing sections needed for their function
import random


class Coin:
    """"
    Represents a single coin in currency (like a penny)
    """"
    def __init__(self, worth: float):
        ""
        Constructs a Coin object
        :param worth: the worth of the Coin
        """
        self.worth = worth

    def flip(self) -> bool:
        """
        Flips a Coin returning either heads or tails
        """
        return random.random() < 0.5

    def __str__(self) -> str:
        """
        Returns a neat string representing the Coin object
        urn: a neat formatted string e.g. £0.40
        """
        return f"£{self.worth}"
