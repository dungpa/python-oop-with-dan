# Add elif and else statements to check for the missing conditions
# The elif and else statements should output a unique message for that dice roll
import random


dice_roll = random.randint(1, 6)
if dice_roll == 1:
    print("The lowest possible roll")
elif dice_roll == 5:
    print("Nearly the best you could get!")
