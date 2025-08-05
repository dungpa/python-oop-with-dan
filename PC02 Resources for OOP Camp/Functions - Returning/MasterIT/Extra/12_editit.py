# Edit this program by calling the 'get_colour' function twice
# - Output the two random colours that were returned
# - Then check if those two random colours were the same
#   = If so, output "They are the same"
import random


def get_colour() -> str:
    return random.choice(["red", "green", "blue", "orange", "purple", "yellow"])
