# Fix the errors in this program
# - It should define a function called 'output_num_vowels' which outputs the number of vowels in a string parameter
# - The program should call this function to test
def output_num_vowels(word: str):
    count = 100
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            count -= 1
    print(f"There are {count} vowels in {word}")


output_num_vowels("programming")
