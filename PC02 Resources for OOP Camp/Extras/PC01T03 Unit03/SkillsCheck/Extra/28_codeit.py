# Define a function which takes a word and outputs the morse code encoding of it
# - This turns every letter in the word into a series of dots . and dashes -
# - Here is the encoding for every letter of the alphabet
# 	A 	. _ 	  		N 	_ .
#  	B 	_ . . . 	  	O 	_ _ _
#  	C 	_ . _ . 	  	P 	. _ _ .
#  	D 	_ . . 	  		Q 	_ _ . _
#  	E 	. 	  			R 	. _ .
#  	F 	. . _ . 	  	S 	. . .
#  	G 	_ _ . 	  		T 	_
#  	H 	. . . . 	  	U 	. . _
#  	I 	. . 	  		V 	. . . _
#  	J 	. _ _ _ 	  	W 	. _ _
#  	K 	_ . _ 	  		X 	_ . . _
#  	L 	. _ . . 	  	Y 	_ . _ _
#  	M 	_ _ 	  		Z 	_ _ . .
# - There are two ways of handling this conversion
#   = Check if the current letter in the word matches any of these 26 letters using if/elif statements
#   = Turn the current letter into a number (for an index) and use that index to retrieve the correct conversion from a list
#       == To turn a letter into a number, use the ord(letter) function
#       == For the letters A to Z, it will return the numbers 65 to 90
#       == Subtract 65 from the number to get an index between 0 and 25
#       == Store the morse code sequences in elements in a list and use the index to retrieve the correct one for the current letter
