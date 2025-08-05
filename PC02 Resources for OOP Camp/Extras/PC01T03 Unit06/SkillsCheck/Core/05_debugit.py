# Fix the errors in this program
# - It should define a function called 'shuffle_colours' which shuffles a list of strings (for colours)
# - The program should call this function and output a list of colours before/after the shuffle
import random


def shuffle_colours colours: str:
    for shuffle_count in range(len(colours) ** 2):
        index_1 = random.randint(0, len(colours) - 1)
        index_2 = random.randint(0, len(colours) - 1)
        temp = colours[index_1]
        colours[index_1] = colours[index_2]
        colours[index_2] = temp


my_colours = ["red", "blue", "green", "yellow", "purple", "brown", "black", "white", "orange"]
print(my_colours)
shuffle_colours()
print(my_colours)
