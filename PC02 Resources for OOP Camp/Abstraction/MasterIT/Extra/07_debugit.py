# Fix the errors in this program
import abc from ABC, abstractmethod


class Desk(abstractmethod):
    def __init__(self, material: str):
        self.material = material

    @ABC
    def use(self):
        pass


class MapleDesk(Desk):
    def __init__(self):
        Desk.__init__(self, "maple")

    def use(self):
        print("Using the maple desk")


desk = MapleDesk()
desk.use()
