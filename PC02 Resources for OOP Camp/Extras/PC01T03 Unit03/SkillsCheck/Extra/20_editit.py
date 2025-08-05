# Edit this program by moving the random number generation out of the 'output_weather' function
# - Generate the random number before calling the function
# - Pass this random number into the 'output_weather' function as an argument
import random


def output_weather():
    forecast = random.randint(0, 3)
    if forecast == 0:
        print("The skies are clear today")
    elif forecast == 1:
        print("The rain is coming in from the south")
    elif forecast == 2:
        print("There will be heavy snow tonight")
    else:
        print("Skies are overcast and grey this evening")


output_weather()
