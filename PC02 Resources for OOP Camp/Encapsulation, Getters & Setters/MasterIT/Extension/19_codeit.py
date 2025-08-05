# Define a 'Pen' class
# - Give it a constructor which takes parameters for a colour and a maximum amount of ink
#   = Declare private instance variables for both parameters, and another private instance variable for the 'current_ink' (starting at the maximum)
# - Define a getter function to get the colour
# - Define an instance function called 'refill' which tops the current_ink back up to the maximum
# - Define an instance function called 'write' which takes a string parameter for the sentence to write
#   = It should remove 1 ink per letter in that parameter
#       == Output each letter that gets written if there is enough ink left over
#   = If the ink falls to 0, stop writing (as there is no more ink) and output the letters that were written
#
# Instantiate a Pen object with any colour and a maximum ink of 20
# - Call the getter function to output the colour of the Pen
# - Call the write function to try writing the sentence "The quick brown fox jumps over the lazy dog"
# - Call the refill function
