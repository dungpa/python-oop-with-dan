# Define a FizzBuzz class with instance variables for the first and second players' scores
# - Start them both at 0 in the constructor
# Define an instance function for playing a single round
# - Take two parameters for the fizz number (int) and the buzz number (int)
# - Start at 1 and continue to count upwards 1 at a time
# - Ask alternating players (player 1, then player 2, then player 1, etc.) for an input
#   = If the number is divisible by both, the answer should be "FizzBuzz"
#   = Otherwise, if the number is divisible by fizz, the answer should be "Fizz"
#   = Otherwise, if the number is divisible by buzz, the answer should be "Buzz"
#   = Otherwise, if the number is not divisible by fizz or buzz, the answer should be the number itself
# - Check if the current player is correct
#   = If so, increase their score by 1
#   = If not, decrease their score by 1
# - End the game after the first 20, 30, 40, etc. (any you want) numbers
# - Output the scores of both players after the game ends
# Instantiate a FizzBuzz object and play a game (using 3 and 7 as the Fizz and Buzz numbers)
