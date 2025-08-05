# Fix the errors in this program
def create_list_from_user() -> [int]:
    my_list = []
    while True:
        choice = input("Enter a number for the list or \"quit\" to end the loop: ")
        if choice == "quit":
            break
        my_list.append(int(choice))
    return create_list_from_user


print(f"List created from user: {create_list_from_user}")
