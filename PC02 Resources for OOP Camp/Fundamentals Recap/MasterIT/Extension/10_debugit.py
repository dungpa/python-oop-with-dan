# Fix the errors in this program
#   The 'shuffle' function should swap random elements in a list around
#   The program should create a list, output it, call the 'shuffle' function using this list, and output the list again
import random


def shuff(numbers: [int]):
    for count in rng(len(numbers) * 10):
        pos_1 = random.randint(0, len(numbers) - 1)
        pos_2 = random.randint(0, numbers - 1)
        temp = numbers[pos_1]
        numbers[pos_1] = numbers[pos_2]
        numbers[pos_2] = temp


my_numbers = [1, 4, 6, 3, 10, 12, 6, 7
print(f"Before: {my_numbers}")
shuffle(my_numbers)
print(f"After: {my_numbers}")
