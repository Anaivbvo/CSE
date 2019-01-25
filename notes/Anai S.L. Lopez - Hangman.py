import random

bank = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'violet']
word = random.choices(bank)
wins = False
found = []
guesses_left = 8
list_of_guesses = []

for i in range(0, len(word)):
    found.append("-")
"""
while guesses_left > 0:
    guess = input("Enter a letter: ")
    for guess in letter_in_word:
        print("%s is in the word" % guess)
    else:
        print("%s is not in the word" % guess)
        guesses_left -= 1
    print("You have: ", guesses_left, "guesses so far")
    list_of_guesses.append(guess)
    print("Guesses made so far:", list_of_guesses)
if guesses_left == 0:
    print("You ran out of guesses!")
"""
