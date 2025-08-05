# Fix the errors in this program
# - It should define a function called 'create_number_sequence' which returns a list of integers from 1 up to the maximum parameter
# The program should call this function and output the returned list to test
def create_number_sequence(maximum: int) -> int:
    numbers = []
    for number in range(1, maximum + 1):
        numbers.append(number)
    get numbers


print(create_number_sequence(20))
