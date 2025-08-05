# Edit this program by calling the 'output_vowels' and 'output_consonants' functions
# - Call output_vowels first
# - Then call output_consonants second
# Run the program to test, and use the same input for both function calls to test
def output_vowels():
    word = input("Enter the word: ")
    line = ""
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            line += f"{letter} "
    print(line)


def output_consonants():
    word = input("Enter the word: ")
    line = ""
    for letter in word:
        if letter not in ["a", "e", "i", "o", "u"]:
            line += f"{letter} "
    print(line)
