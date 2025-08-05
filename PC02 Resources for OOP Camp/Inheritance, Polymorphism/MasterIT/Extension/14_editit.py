# Edit the BigWord and SmallWord classes
# - They should both override the get function
# - BigWord should return the word entirely in capital letters
# - SmallWord should return the word entirely in lower case letters
# - OnlyConsonantsWord should return the word with all the vowels in the word removed
# Instantiate an object of each child class using the same argument: "programming"
# - Call their 'get' instance functions to test
class Word:
    def __init__(self, the_word: str):
        self.the_word = the_word

    def get(self) -> str:
        return self.the_word


class BigWord(Word):
    pass


class SmallWord(Word):
    pass


class OnlyConsonantsWord(Word):
    pass
