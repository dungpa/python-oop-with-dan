# Fix the errors in this program
# - It should define an interface called Destroyable with one abstract function
from ABC import abstractmethod


class Destroyable(ABC):
    @abstractmethod
    def destroy(self):
        pass
