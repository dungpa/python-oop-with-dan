# Edit this program by asking the user for two float values
# - Validate these so they are definitely float values (no bounds)
# - Repeatedly ask the user until they input a valid value
# Call the 'output_smaller' function using those two values as arguments
def output_smaller(num_1: float, num_2: float):
    if num_1 < num_2:
        print(num_1)
    else:
        print(num_2)
