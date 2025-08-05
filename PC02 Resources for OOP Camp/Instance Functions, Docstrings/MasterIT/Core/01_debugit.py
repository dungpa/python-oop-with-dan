# Fix the errors in this program
# Each instance function in this class is missing syntax
class Chest:
    def __init__(self, item: str):
        self.item = item
        self.locked = False

    def lock():
        self.locked = True

    def unlock self:
        self.locked = False

    get_item(self)
        if not self.locked:
            return self.item
