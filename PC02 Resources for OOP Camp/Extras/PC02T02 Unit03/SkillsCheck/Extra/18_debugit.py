# Fix the errors in this program
# - It should define an abstract class called DVD which contains an abstract function
# - It should define a child class called TVSeries which inherits DVD and overrides the constructor/abstract function
# - The program instantiates a TVSeries object and calls its view_box() function to test
from abc import ABC, abstractmethod


class DVD(ABC):
    def __init__(self, title: str, runtime: float):
        self.title = title
        self.runtime = runtime

    @abstractmethod
    def view_box(self):
        pass


class TVSeries:
    def __init__(self, title: str, runtime: float, num_episodes: int):
        DVD.__init__(self, title, runtime)
        self.num_episodes = num_episodes

    def view_box(self):
        print(f"It is a box set of {self.title}")
        print(f"\tIt has {self.num_episodes} episodes, which lasts {self.runtime} hours in total")


box_set = TVSeries("Coding Beginners", 9.5, 15)
box_set.view_box()
