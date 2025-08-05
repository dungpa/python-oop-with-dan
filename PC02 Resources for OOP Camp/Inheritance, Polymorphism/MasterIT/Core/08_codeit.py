# Define a Game parent class with the following instance variables (given values from parameters in the constructor)
# - name (string): the name of the game
# - num_players (int): the number of players the game supports
# Define an instance function called 'output_game_info' which outputs information about the Game (its name and number of players)
#
# Define two children classes for specific Game types
# - Examples include Chess, Checkers/Draughts, SnakesAndLadders, Monopoly, and more
# - Override the constructor to take no parameters
#   = Run the parent's constructor using hard coded values for the name/number of players
# - Override the 'output_game_info' instance function to output the game's name, the number of players, and the rules of the game
#   = Chess: take the other player's King
#   = Checkers/Draughts: take the other player's pieces
#   = Snakes and Ladders: reach the final space
#   = Monopoly: earn the most money
