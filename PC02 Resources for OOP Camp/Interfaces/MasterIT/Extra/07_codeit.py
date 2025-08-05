# Define an interface called 'Storable'
# - Give it an abstract function called 'store' which takes a string parameter for the contents to store
# Define another interface called 'Lockable' which contains abstract functions for 'lock' and 'unlock'
# Define a class called 'Chest' which inherits from both interfaces
# - Give it a constructor which:
#   = Declares a 'contents' instance variable that starts as an empty string
#   = Declares a 'locked' instance variable which starts as True
# - Override the 'store' function and check is the 'locked' instance variable is False
#   = If so, it assigns the parameter to the 'contents' instance variable
#   = It then outputs "Storing {contents} in the chest"
# - Override the 'lock' function which sets 'locked' to True
# - Override the 'unlock' function which sets 'locked' to False
# Instantiate a Chest object and repeatedly ask the user the following
# - If they would like to unlock the chest
#   = If so, call the 'unlock' function
# - If they would like to lock the chest
#   = If so, call the 'lock' function
# - If they would like to store something in the 'Chest'
#   = If so, ask the user what they would like to store
#   = Then call the 'store' function
# - If they would like to quit
#   = If so, end the program
