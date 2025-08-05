# - Edit this function by adding a fully descriptive docstring
def create_numbers(start: int, end: int, step: int) -> [int]:
    numbers = []
    for num in range(start, end, step):
        numbers.append(num)
    return numbers


my_numbers = create_numbers(10, 60, 7)
print(my_numbers)
