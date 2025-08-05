# Fix the errors in this program
# - This program defines a function called is_even
#   = It should return a boolean value for whether or not the num parameter is even
# - It gets an integer value from the user and assigns it to a variable
# - This variable is then used as an argument for the is_even function, outputting the result to the console
class is_even(num: int) -> bool:
    ret num % 2 = 0


num = int("Enter a number: ")
print(Is the number {num} even? {is_even(num)})
