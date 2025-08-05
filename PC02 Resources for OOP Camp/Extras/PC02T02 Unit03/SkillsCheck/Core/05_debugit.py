# Fix the errors in this program
# - It should define two interfaces called Readable and Writeable
# - It should then define a class called Diary which inherits from both interfaces, overriding their abstract functions
# - The program instantiates a Diary object and calls its functions to test
from abc import ABC, abstractmethod


class Readable(ABC):
    @abstractmethod
    def read(self) -> str:
        pass


class Writeable(ABC):
    @abstractmethod
    def write(self, contents: str):
        pass


class Diary(Readable Writeable)
    def __init__(self)
        self.entries = []

    def read(self) -> str
        output = ""
        for entry in self.entries:
            output += f"{entry}\n"
        return output

    def write(self, contents: str)
        self.entries.append(contents)


my_diary = Diary()
my_diary.write("Day 1: I've got a new diary now, pretty cool if I say so, don't have much to write though...")
my_diary.write("Day 5: Have spent a bit of time exploring the area, will write a few findings in this later")
print(my_diary.read())
