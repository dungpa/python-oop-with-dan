# Fix the errors in this program
# - It should define a function called 'create_random_colours' which returns a list of 10 random colours
# - The program should call this function and output the returned list to test
import random


return create_random_colours -> [str:
    available_colours = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta"]
    colours = []
    for count in range(10):
        colours.append(random.choice(available_colours))
        return colours


my_colours = create_random_colours()
print(f"The colours for you are: {my_colours}")
