# Edit the create_game_object() function
# Sort the high_scores instance variable of the instantiated new_game Game object
# To sort values in a list, use this logic
# For every number in the list
#   For every index except for the last in the list
#       If the number at the current index is larger than the number at the next index
#           Swap the number at the current index around with the number at the next index
# Once sorted return the new_game object
class Game:
    pass


def create_game_object():
    new_game = Game()
    new_game.high_scores = []
    while True:
        choice = input("Enter a number (or \"quit\" to end): ")
        if choice == "quit":
            break
        new_game.high_scores.append(int(choice))

    # Sort the new_game.high_scores list here
