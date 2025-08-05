# Edit this program by defining a 'HiddenDesk' child class
# - It should inherit from 'Desk'
# - It should override the 'show_contents' function
#   = The function should output the contents instance variable, but replace each letter with an underscore
#   = For example, the contents "documents" would be output as "_ _ _ _ _ _ _ _ _"
# Instantiate a 'HiddenDesk' object with "documents" as its contents and call the 'show_contents' function to test
from abc import ABC, abstractmethod


class Desk(ABC):
    def __init__(self, contents: str):
        self.contents = contents

    @abstractmethod
    def show_contents(self):
        pass
