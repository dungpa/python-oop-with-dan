# Define a Card class with instance variables for a suit (string) and a value (int)
# - Assign both values using parameters from a constructor
#
# Define a Deck class with an instance variable for a list of Card objects
# - Start it as an empty list in the constructor
# Define the following instance functions
# - fill: takes an integer parameter for the number of Cards to add to the list
#   = Generate that many random Cards
#       == For the value, generate a random number between 1 and 11
#       == For the suit, choose a random string from this list: "Hearts", "Diamonds", "Clubs", "Spades"
# - shuffle: swaps random Cards in the list around to shuffle that list
#       == Repeats a loop for a set number of times (like 100 or 1000)
#       == For each loop, it generates two random indexes (between 0 and the last valid index)
#       == It then swaps the values at those elements around (create a third temporary variable to help with this)
# - draw: returns the first Card in the list (removing it from the list)
# Instantiate a Deck object and give it an empty list to start with
# - Call its fill function to give it 52 cards
# - Call its shuffle function to shuffle that Deck
# - Call its draw function to draw the first Card
