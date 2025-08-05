# Fix the docstring in this function (ensure it fully describes the function and all of its parameters/returned value)
import random


def generate_random_integer(lower: int, upper: int) -> int:
    """
    Generates and returns a random integer between the lower/upper parameters
    :return lower: the upper bound for the random number
    :return upper: the randomly generated integer
    """
    return random.randint(lower, upper)


print(generate_random_integer(0, 100))
