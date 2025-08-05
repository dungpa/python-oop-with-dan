# Define an Encryption class with private instance variables for
# - shift_amount (protected int): the amount to shift the plaintext by
# - plaintext (protected string): the plaintext to encrypt
# Define a CaesarEncryption child class of Encryption
# Define an 'encrypt' instance function in CaesarEncryption which shifts the plaintext by the shift amount
# - Return the encrypted text
# - You can loop through each letter in the plaintext
# - For each letter, get its numerical value with the ord(letter) function
# - Add the shift amount to this numerical value, then turn it back into a string using the chr(number) function
#
# Instantiate a CaesarEncryption object with a shift_amount of 3 and a plaintext of "messagetoencrypt"
# - Call the encrypt() function on this object and output the returned value to test the encrypt function
