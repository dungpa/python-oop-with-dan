class Game:
    def __init__(self, name:str, players:int):
        self.players = players
        self.name = name
        print(f"Making a game called {name} where {players} players can join in")


nameout = input("Enter a word you want to name the game: ")
playersout = int(input("Enter the number of players you want: "))

game = Game(nameout, playersout)
print(game.name)
print(game.players)