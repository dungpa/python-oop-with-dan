# Define an abstract class called 'Language'
# - Give it a constructor
#   = It should take parameter for the name of the language and assign it to an instance variable
# - Give it an abstract function called 'can_use_with'
#   = It should take a parameter for the name of something the language can be used with (like a person or a computer)
#   = This function should return a boolean value
# Define a child class called 'ProgrammingLanguage'
# - Override the 'can_use_with' function
#   = If the string parameter is "computer", return True, otherwise return False
# Define another child class called 'SpokenLanguage'
# - Override the 'can_use_with' function
#   = If the string parameter is "person", return True, otherwise return False
# Instantiate 'ProgrammingLanguage' and 'SpokenLanguage' objects (with any name)
# Create a list of things (like "person", "car", "computer", etc.)
# - Loop through every item in this list
# - Check if it can be used with both objects
#   = When one can be used, output "{object.name} can be used by a {item}"
