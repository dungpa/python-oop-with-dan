# This file contains pre-defined child classes for the items that can be found in a room
# - The program has a list of these items called game_items
# - It also has a list of items the player has picked up called picked_up_items
# The game works by asking the user (repeatedly) what they would like to do from a set of actions
# - Show items around me should show the list of items (their names) in the console
# - Examine an item should examine a specific item
# - Pick up an item should remove it from the game_items list and add it to the picked_up_items list
# - Use an item should show the list of picked_up_items to the user and let them choose which one to use
# - End game should end the game loop
# Define an abstract class called Item which has abstract functions for the three main actions:
# - show() (outputs the name of the item)
# - examine() (outputs some key information about that item)
# - use() (outputs some text for using that item)
# Inherit this Item class in each of the specific items below
# - Each child class contains a comment for what each of those abstract functions should do
# Play the game and make sure you can view, examine, pick up, and use each item in the room
class Compass:
    # show: "A compass"
    # examine: "It is a small compass which seems to be pointing towards north"
    # use: "You turn to the north in the room; it doesn't seem to lead anywhere"
    pass


class Torch:
    # show: "A small torch"
    # examine: "It is a small handheld torch with a switch on the side of it"
    # use: "You turn on the torch and light up the area. It is daytime though, so that didn't change much"
    pass


class Bag:
    # show: "A backpack"
    # examine: "A large backpack, looks like it was made for hiking. Seems sturdy enough to take anywhere"
    # use: "You look inside the backpack and spot a few travelling essentials. It should have enough room to store
    #       everything you can see in this room too"
    pass


class Map:
    # show: "A map"
    # examine: "A map of the immediate area, including roads, village names, and some key areas to avoid. A useful
    #           companion for travels"
    # use: "You look closely at the map and spot your location. Tracing the road to the nearest village, you think
    #       it should only take a few hours to walk there"
    pass


game_items = [Compass(), Torch(), Bag(), Map()]
picked_up_items = []
while True:
    print("You are in your room, and can see a few items around you. What do you do?")
    print("\t1. Show the items around me")
    print("\t2. Examine an item")
    print("\t3. Pick up an item")
    print("\t4. Use an item")
    print("\t5. [End Game]")
    choice = input("Choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        break
