"""
- with every wrong letter chosen the number of guesses goes down
- rewrite the whole sentence after each turn
- every letter guessed is made into a list
- one one turn you have the number of guesses left, the sentence itself, and the list of letters guessed
"""

# Ex:
list1 = ["item0", "item1", "item2"]
print(list1)

"""
# Try 1:
hangman1 = []
print(hangman1)
hangman1.append("rhythm")


hangman1A = input("Try to guess the word! You have 8 tries!: ")
print("______")
guesses = 8
while guesses <0:
 if input == hangman1:
    print("You won!")
 else:
    guesses = guesses - 1
    print("Wrong letter, try again!")
"""

# Try 2:

hangman2 = []
print(hangman2)
hangman2.append("spoon")

guesses = 8

while guesses < 0:
    hangman2A = input("Try to guess the word! You have 8 tries! : ")
    if input == hangman2:
        print("You won!")
    else:
        guesses = guesses - 1
        print("Aww too bad! Try again!")
