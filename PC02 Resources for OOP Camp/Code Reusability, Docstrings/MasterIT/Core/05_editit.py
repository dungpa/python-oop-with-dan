# Edit this program by adding fully-descriptive docstrings to both functions
def get_integer() -> int:
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Please enter a valid integer...")


def is_even(number: int) -> bool:
    return number % 2 == 0


my_number = get_integer()
result = is_even(my_number)
print(f"{my_number} is even: {result}")
