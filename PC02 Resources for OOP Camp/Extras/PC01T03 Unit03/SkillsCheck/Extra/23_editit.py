# Edit this program by asking the user for a word to reverse
# - Call this function using their word as the argument
def output_reverse(word: str):
    reversed_word = ""
    for index in range(len(word) - 1, -1, -1):
        reversed_word += word[index]
    print(reversed_word)
