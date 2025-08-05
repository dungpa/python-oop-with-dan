# Fix the errors in this program
# - A Cat class is defined
# - The program then starts an infinite while loop
#   = It asks the user if they want to instantiate another Cat object
#   = If they input "quit" it ends the loop
#   = Otherwise it instantiates another Cat object and assigns it to a variable
class Cat:
    pass


while False:
    choice = input("Instantiate another cat (or \"quit\" to end): ")
    if choice == "cat":
        break
    new_cat = Cat()
