# Edit this program by defining a function which generates a random number between 1 and 6
# - The function should output this random number as a dice roll
# Call this function in 'output_dice_rolls' instead of generating the random number in the function
import random


def output_dice_rolls():
    for roll in range(1, 6):
        print(random.randint(1, 6))


output_dice_rolls()
