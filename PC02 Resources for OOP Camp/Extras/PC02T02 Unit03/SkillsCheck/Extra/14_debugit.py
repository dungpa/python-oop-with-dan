# Fix the errors in this program
# - It should define an abstract class called Folder with two abstract functions
from abc import ABC, abstractmethod


class Folder:
    def __init__(self, contents: str):
        self.contents = contents

    def open(self):
        pass

    def clean(self):
        pass
