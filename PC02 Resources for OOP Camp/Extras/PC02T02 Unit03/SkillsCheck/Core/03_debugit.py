# Fix the errors in this program
# - It should define an abstract class called Book which contains an abstract function
# - It should then define a child class called Dictionary which overrides the abstract function
# - The program should instantiate a Dictionary object and call its functions to test
from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, contents: str):
        self.title = title
        self.contents = contents

    def get_title(self) -> str:
        return self.title

    @abstractmethod
    def get_contents(self) -> str:
        pass


class Dictionary(ABC):
    def __init__(self):
        Book.__init__(self, "Dictionary", "Words in a dictionary")
        self.words = []

    def add_word(self, word: str):
        self.words.append(word)

    def get_contents(self) -> str:
        output = ""
        for word in self.words:
            output += f"{word} "
        return output


dictionary = Dictionary()
dictionary.add_word("code")
dictionary.add_word("program")
print(dictionary.get_title())
print(dictionary.get_contents())
