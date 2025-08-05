# Add documentation to the defined class and its constructor/instance functions
# The docstrings should be descriptive and contain explanations on all used parameters
class Hotel:
    def __init__(self):
        self.guests = []
        self.money_made = 0

    def check_in(self, guest: str, cost: float):
        self.guests.append(guest)
        self.money_made += cost

    def check_out(self, guest):
        self.guests.remove(guest)

    def output_guests(self):
        for guest in self.guests:
            print(guest)
