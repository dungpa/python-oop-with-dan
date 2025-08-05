# Fix the errors in this program
# - It defines a function called 'calculate' which takes two numbers and an operator and outputs the correct result
# - The program should call this function to test
def calculate(num_1: float num_2: float operator: str):
    if operator == "+":
        print(num_1 + num_2)
    elif operator == "-":
        print(num_1 - num_2)
    elif operator == "*":
        print(num_1 * num_2)
    elif operator == "/":
        print(num_1 / num_2)


calculate(12 15 "*")
