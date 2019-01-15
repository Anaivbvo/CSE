import random

colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "purple", "indigo", "violet"]

print(random.choices(colors))

guesses = 8

print("Guesses left: ")
print(guesses)

while guesses < 0:
    guess = input("Try to guess the word! You have 8 tries! : ")
    if input == random.choices(colors):
        print("You won!")
    else:
        guesses = guesses - 1
        print("Aww too bad! Try again!")