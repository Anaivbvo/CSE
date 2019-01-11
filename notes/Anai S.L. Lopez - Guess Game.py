guesses = 5
wins = False
number = 5

while guesses > 0:
    num = int(input("What number am I thinking of from 1 - 10?"))
    if num > 10:
        print("Way too high! Try again.")
        guesses = guesses - 1
        print("Guesses left:")
        print(guesses)
    elif num < 0:
        print("Way too low! Try again!")
        guesses = guesses - 1
        print("Guesses left:")
        print(guesses)
    elif num > number:
        print("A bit too high! Try again.")
        guesses = guesses - 1
        print("Guesses left:")
        print(guesses)
    elif num < number:
        print("It's a little higher! Try again.")
        guesses = guesses - 1
        print("Guesses left:")
        print(guesses)
    elif guesses == 0:
        print("Oh no! you ran out of guesses!")
        print("Here's the actual number: ")
        print(number)
    elif num == number:
        print("You did it! Good job!")
        guesses = 0
