# Fix the docstring in this function (ensure it fully describes the function and all of its parameters/returned value)
def validate_integer(lower: int, upper: int) -> int:
    """
    Validates a user's integer between the lower and upper bounds
    """
    while True:
        try:
            number = int(input("Enter a number: "))
            if lower <= number <= upper:
                return number
        except ValueError:
            print("Enter a valid integer...")


print(f"You entered the number: {validate_integer(0, 100)}")
