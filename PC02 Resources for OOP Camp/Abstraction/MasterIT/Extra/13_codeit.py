# Define a 'Vehicle' abstract class
# - Give it a constructor which has two parameters for a 'horse_power' and a 'miles_used'
#   = Assign both parameters to instance variables
# - Define an abstract function called 'drive' which accepts an integer parameter for the number of miles to drive
# - Define an abstract function called 'clean'
# Define a child class called 'Car'
# - Override the 'drive' function
#   = Add the miles driven parameter to the 'miles_used' instance variable
#   = Output "Driving {amount} miles"
# - Override the 'clean' function
#   = Output "Cleaning the car"
# Define another child class called 'Boat'
# - Override the 'drive' function
#   = Output "Piloting a boat over {amount} miles"
# - Override the 'clean' function
#   = Ask the user how many people will be helping them clean the boat
#   = Divide 40 by the number (the result being the amount of time it will take to clean the boat)
#   = Output "It will take {time} hours to clean the boat"
# Instantiate 'Car' and 'Boat' objects and call their 'drive' and 'clean' functions to test
