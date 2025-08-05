# Fix the errors in this program
# - It defines a function called 'output_larger' which asks the user for two numbers and outputs the larger of the two
# - The program calls this function
def output_larger
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)


output_larger
