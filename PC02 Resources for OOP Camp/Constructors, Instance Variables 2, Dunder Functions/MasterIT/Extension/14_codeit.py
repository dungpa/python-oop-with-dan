# Define an Encryptor class
# - Give it a constructor with parameters for a secret (string) and a shift amount (integer)
#   = Declare instance variables for both parameters
#   = Declare an instance variable for the 'encrypted_secret' which starts as an empty string
#   = To determine the value for 'encrypted_secret' use the following logic
#       * Loop through the 'secret' parameter letter by letter
#       * Turn the current letter into a number using the ord() function
#       * Increase the returned number by the 'shift' amount
#       * Turn this shifted number back into a character using the chr() function
#       * Append this character onto the 'encrypted_secret' string
# Instantiate an Encryptor object with the following secret and amount
# - secret: "thisisahiddenmessage"
# - amount: 3
# Output the 'encrypted_secret' instance variable
