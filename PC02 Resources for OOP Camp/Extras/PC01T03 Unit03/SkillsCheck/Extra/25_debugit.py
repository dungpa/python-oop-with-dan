# Fix the errors in this program
# - It should define a function called 'output_required_carpets' which outputs the number of carpets needed for the floor in three rooms of a house
# - The program should call this function to test
output_required_carpets
    print("Enter the information for your living room:")
    living_room_width = float(input("\tWidth: "))
    living_room_height = float(input("\tHeight: "))
    print("Enter the information for your kitchen:")
    kitchen_width = float(input("\tWidth: "))
    kitchen_height = float(input("\tHeight: "))
    print("Enter the information for your bedroom:")
    bedroom_width = float(input("\tWidth: "))
    bedroom_height = float(input("\tHeight: "))
    carpet_area = 12
    living_room_area = living_room_height * living_room_width
    kitchen_area = kitchen_height * kitchen_width
    bedroom_area = bedroom_height * bedroom_width
    total_area = living_room_area + kitchen_area + bedroom_area
    num_carpets = (total_area // carpet_area) + 1
    print(f"You will need {num_carpets} rolls of carpet for your house")


output_required_carpets
