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
randomWord = random.choices(bank)
guesses = 8
WrongGuesses = 0
ListOfGuesses = []
# index = random.randint(0,len(bank)-1)
# randomWord2 = bank[index]
