import random

"""
if x.lower() in randomWord.lower():
    print(x,"is in the word!")
    listOfGuesses.append(x)
    print("Letters guessed so far: ",listOfGuesses)
    print()
else:
    print(x,"is not in the word.")
    wrongGuesses += 1
    print(wrongGuesses, "wrong guesses.")
    listOfGuesses.append(x)
    print("Letters guessed so far: ",listOfGuesses)
    print()

   print("You lost the game!")
   return x
"""

bank = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "violet"]
word = random.choices(bank)
letter_in_word = list(word)
guesses_left = 8
list_of_guesses = []
print(word)

while guesses_left > 0:
    guess = input("Enter a letter: ")
    if guess in letter_in_word:
        print("%s is in the word" % guess)
    else:
        print("%s is not in the word" % guess)
        guesses_left -= 1
    print("You have: ", guesses_left, "guesses so far")
    list_of_guesses.append(guess)
    print("Guesses made so far:", list_of_guesses)
if guesses_left == 0:
    print("You ran out of guesses! :0!!")
