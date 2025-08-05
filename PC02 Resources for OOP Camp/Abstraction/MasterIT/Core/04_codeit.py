# Define an abstract class called 'House'
# - Give it a constructor which requires an integer parameter for a number of rooms
#   = Assign this parameter to a 'num_rooms' instance variable
# - Give it an abstract function called 'explore'
# Define a child class of 'House' called 'Mansion'
# - Override the constructor
#   = It should call the parent's constructor and set the number of rooms to 15
# - Override 'explore'
#   = It should output "Exploring a mansion with {num_rooms} rooms"
# Define another child class called 'Bungalow'
# - Override 'explore'
#   = It should output "Exploring this one-story bungalow with {num_rooms} rooms"
# Instantiate 'Mansion' and 'Bungalow' objects and call their 'explore' functions to test
