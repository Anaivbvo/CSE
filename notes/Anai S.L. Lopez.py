import random
colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "purple", "indigo", "violet"]
word = random.choices(colors)
print(word)

guesses = 8
while guesses < 0:
    guess = input("Try to guess the word! You have 8 tries! : ")
    if input == random.choices(colors):
        print("You won!")
    else:
        guesses = guesses - 1
        print("Aww too bad! Try again!")
if guesses == 0:
    print("Aww! You ran out guesses!")
    print("The word you were trying was: ")
    print(word)
