# Define an instance function in this class that returns only the positive numbers from the numbers list
# Then, instantiate a NumberStorage object and add these numbers to it: 12, -4, 8, -10, 9
# - Call the instance function you defined to make sure it only outputs 12, 8, and 9
class NumberStorage:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)
