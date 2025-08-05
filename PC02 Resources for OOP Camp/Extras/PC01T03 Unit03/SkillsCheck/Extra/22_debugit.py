# Fix the errors in this program
# - It should define a function called 'output_cards' which outputs a parameter number of random cards
#   = This function should add strings to the 'card' variable to create a name of a card
#       == For example, "Ace of Diamonds"
# - The program should call this function to test
import random


def output_cards():
    for count in range(num):
        card = ""
        suit = random.randint(0, 3)
        value = random.randint(0, 12)
        if value == 0:
            card += "Ace"
        elif value == 10:
            card += "Jack"
        elif value == 11:
            card += "Queen"
        elif value == 12:
            card += "King"
        else:
            card += f"{value + 1}"
        value += " of "
        if suit == 0:
            card += "Hearts"
        elif suit == 1:
            card += "Diamonds"
        elif suit == 2:
            card += "Clubs"
        else:
            card += "Spades"
        print(f"\t{card}")


cards(6)
