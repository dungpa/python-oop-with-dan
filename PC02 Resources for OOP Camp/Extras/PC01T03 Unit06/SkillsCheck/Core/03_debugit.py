# Fix the errors in this program
# - The 'is_even' function returns True if the parameter integer is even, otherwise it returns False
# - The 'get_random_even_number' function generates and returns a random even number
#   = It repeatedly generates a random number and checks if it is even using the 'is_even' function
#       == If the function call returns True, this function returns the random number
# - The program should call 'get_random_even_number' and output the returned integer
import random


is_even(number: int) -> bool:
    return number % 2 == 0


get_random_even_number() -> int:
    while True:
        number = random.randint(0, 100)
        if is_even[number]:
            return number

    
print(get_random_even_number())
