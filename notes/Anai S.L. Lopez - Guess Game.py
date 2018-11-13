number = .randint(0, 10)
guesses = 5
wins = False

while guesses > 0:
    number = int(input("What's number am I thinking of from 1 - 10?"))
    if number > 10:
        print("Way too high! Try again.")
        guesses = guesses - 1
    elif number > number:
        print("A bit too high! Try again.")
        guesses = guesses - 1
    elif number < number:
        print("It's a little higher! Try again.")
        guesses = guesses - 1
    elif number == number:
        print("You did it! Good job!")
        guesses = 0
