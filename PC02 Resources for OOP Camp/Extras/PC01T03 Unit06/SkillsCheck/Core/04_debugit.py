# Fix the docstring for this function
def hide_word(word: str) -> str:
    """
    Returns a series of asterisks (*) for each letter in the parameter word
    hidden_word = ""
    for letter in word:
        hidden_word += "*"
    return hidden_word


password = input("Enter your password: ")
print(f"You entered {hide_word(password)}")
