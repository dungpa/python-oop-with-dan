class Game:
    pass

game = Game()
game.name = "roblominecrasteamtendo"
game.players = 6

game.name = input("Enter a word you want to name the game")
game.players = int(input("Enter the number of players you want: "))

print(game.name)
print(game.players)
