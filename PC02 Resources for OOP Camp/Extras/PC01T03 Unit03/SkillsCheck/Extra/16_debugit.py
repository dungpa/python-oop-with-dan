# Fix the errors in this program
# - It should define a function called 'output_hobby' which asks the user for hobby information and outputs it in a list
# - The program should call this function to test
def output_hobby():
    print("Enter this information about your hobby:")
    name = input("\tIt's name: ")
    time_spent = input("\tTime spent doing this hobby (in hours): ")
    rating = input("\tYour rating (0 to 10): ")
    print("\nYour information for this hobby:")
    print(f"\tName: {name}")
    print(f"\tTime Spent: {time_spent} hours")
    print(f"\tYour Rating: {rating} out of 10")


output_name
