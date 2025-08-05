# Define a CodeDoor child class for this Door class
# It should override the constructor to define one additional instance variable
# - code (private string): the code to input into the door to unlock it
# Define an unlock instance function in the CodeDoor child class
# - It should take a code parameter
# - Set the locked instance variable to False if the code matches the instance variable code
class Door:
    def __init__(self):
        self._locked = True

    def is_open(self) -> bool:
        return not self._locked
