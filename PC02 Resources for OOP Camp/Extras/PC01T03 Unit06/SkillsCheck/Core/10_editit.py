# Edit this program by splitting this program into two functions
# - Call both of those functions so the program behaves the same after your edits
while True:
    colour_1 = input("Enter a primary colour (red/yellow/blue): ")
    if colour_1 in ["red", "yellow", "blue"]:
        break
while True:
    colour_2 = input("Enter a primary colour (red/yellow/blue): ")
    if colour_2 in ["red", "yellow", "blue"]:
        break
if (colour_1 == "red" and colour_2 == "yellow") or (colour_1 == "yellow" and colour_2 == "red"):
    print("orange")
if (colour_1 == "red" and colour_2 == "blue") or (colour_1 == "blue" and colour_2 == "red"):
    print("purple")
if (colour_1 == "yellow" and colour_2 == "blue") or (colour_1 == "blue" and colour_2 == "yellow"):
    print("green")
