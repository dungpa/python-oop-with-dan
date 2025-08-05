# Edit this program by asking the user for the wall's width/height and the amount of available paint
# - Use these values as the arguments when calling the 'has_enough_paint' function
def has_enough_paint(width: float, height: float, amount_of_paint: float):
    paint_required = width * height
    if amount_of_paint >= paint_required:
        print("You have enough paint")
    else:
        print(f"You do not have enough paint, you need another {paint_required - amount_of_paint}")


has_enough_paint(2.6, 2, 10)
