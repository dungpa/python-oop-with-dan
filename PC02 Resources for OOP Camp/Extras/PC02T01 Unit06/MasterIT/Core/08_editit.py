# Define the missing instance functions in this class, which include
# - A function for adding a word to the Dictionary called 'add_word'
# - A function for outputting all the words in the Dictionary called 'output'
class Dictionary:
    def __init__(self):
        self.words = []

    def remove_word(self, word_to_remove):
        self.words.remove(word_to_remove)


my_dictionary = Dictionary()
my_dictionary.add_word("program")
my_dictionary.add_word("code")
my_dictionary.output()
my_dictionary.remove_word("program")
my_dictionary.output()
