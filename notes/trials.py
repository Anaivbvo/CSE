import random

"""
bank = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "violet"]
randomWord = random.choices(bank)
print(randomWord)

wrongGuesses = 0
listOfGuesses = []

while wrongGuesses != 8:
    x = input("Enter a letter: ")
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
# word = random.choices(bank)
guesses = 8
wrong = 0
ListOfGuesses = []
# index = random.randint(0,len(bank)-1)
# randomWord2 = bank[index]


while guesses > 0:
    word = "Red"
    g = input("Enter a letter: ")
    if g == word:
        print("%s is in the word" % g)
        guesses = guesses
        print("You have: ", guesses, "guesses so far")
        ListOfGuesses.append(g)
        print("Guesses made so far:", ListOfGuesses)
        wrong = wrong
        print("You have made", wrong, "wrong guesses so far")
        print("Good job!!")
    else:
        print("%s is not in the word" % g)
        guesses = guesses - 1
        print("You have: ", guesses, "guesses so far")
        ListOfGuesses.append(g)
        print("Guesses made so far:", ListOfGuesses)
        wrong = wrong + 1
        print("You have made", wrong, "wrong guesses so far")
        print("Try again!!")
if guesses == 0:
    print("You ran out of guesses! :0!!")
