# Fix the errors in this program
# - It should define a function caled 'create_numbers' which generates and returns a list of random integers
#   = It should also contain a docstring which is fully descriptive
# - The program should call this function and output the returned list to test
import random


def create_numbers(size: bool) -< [int]:
    #
    Creates and returns a list of size random integers
    :param size: the number of integers to add to the list
    :return: the list of random integers
    #
    numbers = []
    for count in range(size):
        numbers.append(random.randint(0, 100))
    return numbers


result = create_numbers(10)
print(numbers)
