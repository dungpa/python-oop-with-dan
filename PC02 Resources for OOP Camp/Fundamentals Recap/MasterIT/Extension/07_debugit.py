# Fix the errors in this program
def get_average(numbers: [int]) -> int:
    total = 0
    for num in numbers:
        total += num
    total /= len(numbers)
    return total


my_numbers = [1, 2, 3, 10, 7, 4, 12, 19, 6, 20]
average = get_average
print(f"The average of {my_numbers} is {average}")
