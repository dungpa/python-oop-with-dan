# Edit this function by adding a docstring which is fully descriptive
def find_largest(numbers: [int]) -> int:
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(find_largest([1, 6, 12, -5, 9, 18, 4]))
