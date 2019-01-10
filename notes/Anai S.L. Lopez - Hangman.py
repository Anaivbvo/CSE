"""
- with every wrong letter chosen the number of guesses goes down
- rewrite the whole sentence after each turn
- every letter guessed is made into a list
- one one turn you have the number of guesses left, the sentence itself, and the list of letters guessed
"""

"""
Create the game Hangman in Python. This game must pick a work from a word bank of at least 10 words of various sizes. 
You can use lists to store information throughout the program, but when printing in terminal, users should not see a 
list.

Good Example: *ello Wor*d
Bad example: ["*", "e", "l", "l", "o", " ", "W", "o", "r", "*", "d"]

To help you, here is a list of steps to follow:
1. Make a word bank of 10+ words
2. Create all the variables that you will need to keep track of.
3. Take in a guess and keep track of it.
4. Check to see if the letter is in the word
5. Generate a hidden word based on what letters are guessed. (If there are no letters guessed, no letters will be 
revealed)
6. Check to see if the user has won. If there are no more letters to guess, the game should end.
"""

# Ex:
list1 = ["item0", "item1", "item2"]
print(list1)

# Try 1:
hangman1 = []
print(hangman1)
hangman1.append("rhythm")


hangman1A = input("Try to guess the word! You have 8 tries!: ")
print("______")
guesses = 8
if input == hangman1:
