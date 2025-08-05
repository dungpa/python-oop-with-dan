# Define a function which takes a string for a maths expression and calculates/returns the correct result
# - Every expression should follow these rules
#   = Only posiive numbers allowed in the expression
#   = Only the operators +, -, *, and / are allowed
#   = Every expression is in the format NumberOperatorNumber
#       == For example, "6*1" or "105/4"
# Call this function using the expression "27*4" and output the result to test
#
# To calculate the correct result for the expression string, split the string into the three main parts
# - The first number
# - The operator
# - The second number
# Every digit up until the operator should belong to the first number
# Every digit after the operator should belong to the second number
# - You can append digits to a string variable and convert that string to a float value once the number has been retrieved
