# Define a RockPaperScissors class with instance variables for player 1's and player 2's score
# - Start them both at 0 in the constructor
# Define an instance function for playing a single round of Rock Paper Scissors
# - Ask both players for Rock/Paper/Scissors input
# - Return 0, 1, or 2
#   = 0 if it was a draw
#   = 1 if player 1 won
#   = 2 if player 2 won
#   = Rock beats Scissors, Scissors beats Paper, Paper beats Rock
# Define an instance function for playing 'best of #' with the best of number as a parameter (integer)
# - Start an infinite while loop
#   = Call the Rock Paper Scissors instance function you defined and store the returned value in a variable
#   = If that variable is equal to 1, increase player 1's score
#   = If that variable is equal to 2, increase player 2's score
#   = If either player's score is greater than half of the 'best of' number
#       == Output that player as the winner
#       == End the infinite while loop
