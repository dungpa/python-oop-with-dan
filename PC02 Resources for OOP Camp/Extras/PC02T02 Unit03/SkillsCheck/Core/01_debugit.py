# Fix the errors in this program
# - It should define an abstract class called Book which contains an abstract function
import abc


class Book(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def get_title(self):
        pass
