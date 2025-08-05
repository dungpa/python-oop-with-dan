# Edit this program by splitting this program into two functions
# - Call both of those functions so the program behaves the same after your edits
words = []
while True:
    word = input("Enter a word to add (or \"quit\" to stop adding words): ")
    if word == "quit":
        break
    else:
        words.append(word)
print("Outputting the words up to 3 characters long...")
for word in words:
    if len(word) <= 3:
        print(f"\t{word}")
