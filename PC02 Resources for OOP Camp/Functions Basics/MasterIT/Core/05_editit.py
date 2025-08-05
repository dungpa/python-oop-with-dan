# Edit this program
# - Ask the user for a number of coins to flip
# - Call the flip_coin function that many times
import random


def flip_coin():
    if random.randint(0, 1) == 0:
        print("Heads")
    else:
        print("Tails")
