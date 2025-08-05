# Edit this program by editing the 'output_larger' function
# - Instead of using user input, use arguments for the two numbers used in the function
# When calling the function at the end of the Python file, use the arguments 12 and -12 to test
def output_larger():
    user_num_1 = int(input("Enter the first number: "))
    user_num_2 = int(input("Enter the second number: "))
    if user_num_1 > user_num_2:
        print(user_num_1)
    else:
        print(user_num_2)


output_larger()
