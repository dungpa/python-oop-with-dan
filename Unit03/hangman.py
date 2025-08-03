from random import randint

words = ["cat"]
chosen_word = words[randint(0, len(words) - 1)]

guessed_letters = []
guesses = 12
while guesses > 0:
    revealed_word = ""
    for letter in chosen_word:
        guessed = False
        for guessed_letter in guessed_letters:
            if letter == guessed_letter:
                guessed = True
                break
        if guessed:
            revealed_word += letter + " "
        else:
            revealed_word += "_ "
    print(revealed_word)

    has_won = True
    for letter in revealed_word:
        if letter == "_":
            has_won = False
    if has_won:
        print("You have revealed the entire word!")
        break

    while True:
        guess = input("Enter a letter to guess: ")
        already_guessed = False
        for letter in guessed_letters:
            if letter == guess:
                already_guessed = True
                break
        if already_guessed:
            print("That letter was already guessed!")
        else:
            guessed_letters.append(guess)
            guesses -= 1
            break
    print(guessed_letters)
