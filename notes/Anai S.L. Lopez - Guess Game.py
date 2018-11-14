import random

number = (random.randint(1, 10))
guesses = 5
wins = False

while guesses > 0:
    number = int(input("What's number am I thinking of from 1 - 10?"))
    if number > 10:
        print("Way too high! Try again.")
        guesses = guesses - 1
    elif number < 0:
        print("Way too low! Try again!")
    elif number > number:
        print("A bit too high! Try again.")
        guesses = guesses - 1
    elif number < number:
        print("It's a little higher! Try again.")
        guesses = guesses - 1
    elif number == number:
        print("You did it! Good job!")
        guesses = 0
    elif guesses == 0:
        print("Oh no! you ran out of guesses!")
        print("Here's the actual number: ")
        print(number)
