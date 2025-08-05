# Define a function called convert_to_int
# - It takes a string representing a binary number (e.g. "1000101") as a parameter
# - It then converts this into an base 10 integer and returns the result
#   = Create a power variable which starts at 1
#   = Create a result variable which starts at 0
#   = Loop through the binary string backwards (from the last digit to the first digit)
#           === Strings can act as lists, in that they have a length (len(word)) and have indexes (word[index])
#       == Convert the current digit of the binary string into an integer digit
#       == Add the digit multiplied by the power to the result
#       == Multiply the power by 2
#   = Return the result (which is the converted decimal number)
# Call this function twice using these binary numbers:
# - 111110001       (should result in 497)
# - 100000101101    (should result in 2093)
# Output the results of those convert_to_int function calls
