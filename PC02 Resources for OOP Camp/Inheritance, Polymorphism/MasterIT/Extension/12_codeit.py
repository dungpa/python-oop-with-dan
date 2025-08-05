# Define a File parent class with instance functions for 'save' and 'load' (both using pass for empty functions)
# - save should take two parameters for the location of the file (string) and a list of strings to write to the file
# - load should take one parameter for the location of the file (string)
# Define a child class of File called TextFile which overrides save and load
# - save should do the following:
#   = Open the file at the file location using file = open(file_path, "w")
#   = Loop through the list of lines to write
#   = Write each one to the file using file.write(line)
#   = Close the file after the loop using file.close()
# - load should do the following:
#   = Open the file at the file location using file = open(file_path, "r")
#   = Read every line from the file into a list using lines = file.readlines()
#   = Return that list of lines
# To test, instantiate a TextFile object and use these arguments for the save and load functions
# - save
#   = location: "test_file.txt"
#   = data: ["line 1", "line 2", "line 3"]
# - load
#   =  location: "test_file.txt"
# Output the returned list from the 'load' function and make sure it is the same as the argument list used for the save function
