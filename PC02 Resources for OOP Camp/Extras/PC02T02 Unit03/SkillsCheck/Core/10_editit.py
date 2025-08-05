# Edit this program by defining another class (child of Game that also inherits from Playable) for Checkers
# - This class should override the constructor
#   = It should call Game's constructor, passing in "Checkers" as the name argument
# - This class should also override the play() function
#   = It should output a few lines of text describing a game of Checkers, for example:
#           "Player 1 is moving one of their pieces up the board"
#           "Player 2 is being defensive"
#           "Player 1 goes for some early captures"
#           "But Player 2 responds with a nice capture sequence, ending up on the opposite side of the board"
#           "There is no way for Player 1 to come back, Player 2 has this game locked down"
# - Finally, this class should override the show_rules() function
#   = It should output the rules of the game (players take turns moving disks diagonally and taking their opponents pieces)
# Instantiate a Checkers object and call its show_rules() and play() instance functions to test
from abc import ABC, abstractmethod


class Playable(ABC):
    @abstractmethod
    def play(self):
        pass


class Game(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def show_rules(self):
        pass


class Chess(Game, Playable):
    def __init__(self):
        Game.__init__(self, "Chess")

    def show_rules(self):
        print("Players take turns moving pieces on a board until the King is taken into Checkmate")
        print("\t- This is when the King cannot move without being captured")

    def play(self):
        print("Player 1 moves their pawn first")
        print("Player 2 responds with their own pawn")
        print("The game seems to be heating up with players making fast moves")
        print("Player 1 has got Player 2's King in Checkmate, that's the game!")


chess = Chess()
chess.show_rules()
chess.play()
