# Edit this program by defining a Box class which inherits the Destroyable interface
# - Give it a constructor which requires a string parameter for the contents of the Box (saved to an instance variable)
# - Override the destroy() function to output one of two messages (randomly)
#   = "The box was destroyed, but the contents were still OK. The box contained {contents}"
#   = "The box was destroyed, along with the contents inside of it"
# Instantiate a Box object and call its destroy() function to test
from abc import ABC, abstractmethod


class Destroyable(ABC):
    @abstractmethod
    def destroy(self):
        pass
