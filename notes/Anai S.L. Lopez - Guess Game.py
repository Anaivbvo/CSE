number = 5
guesses = 5
wins = False

while guesses > 0:
    num = int(input("What's number am i thinking of from 1 - 10?"))
    if num > 11:
        print("Way too high! Try again.")
        guesses = guesses - 1
    elif num > number:
        print("A bit too high! Try again.")
        guesses = guesses - 1
    elif number < 4:
        print("It's a little higher. Try again you got this!")
        guesses == guesses - 1
        