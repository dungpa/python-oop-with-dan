# Edit this program by splitting this program into two functions
# - Call both of those functions so the program behaves the same after your edits
import random

words = []
while True:
    word = input("Enter a new word to add (or \"quit\" to stop adding words): ")
    if word == "quit":
        break
    else:
        words.append(word)
chosen_word = random.choice(words)
hidden_word = ""
for letter in chosen_word:
    hidden_word += "_ "
print(f"The hidden word is: {hidden_word}")
