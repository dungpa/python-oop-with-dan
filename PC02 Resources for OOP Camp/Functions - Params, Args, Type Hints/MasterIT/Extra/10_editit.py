# Edit this program by adding parameter type hints to all defined functions
# - Examine the function and the calling instruction to determine the correct type hint
def output_total(numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"The total of {numbers} is {total}")


def output_product(numbers):
    total = 0
    for num in numbers:
        total *= num
    print(f"The product of {numbers} is {total}")


def output_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    print(f"The smallest value in {numbers} is {smallest}")


def output_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print(f"The smallest value in {numbers} is {largest}")


my_numbers = [3.14, 10.2, 0.3, 23.8, 7.9, 15.12]
output_total(my_numbers)
output_product(my_numbers)
output_smallest(my_numbers)
output_largest(my_numbers)
