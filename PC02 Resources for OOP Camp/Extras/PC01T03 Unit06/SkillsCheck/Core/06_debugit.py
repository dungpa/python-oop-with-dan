# Fix the errors in this program
# - It should define a function called 'count_down' (the docstring explains what it does)
# - The program should call this function using an argument of 26 to test
def count_down(start: int):
    """
    Counts down from the parameter to 0 (inclusive)

    :param start: the number to start counting down from
    """
    print(f"Counting down from {start}...")
    for counter in range(start, start, 2):
        print(f"\t{counter}")


count_down(26)
