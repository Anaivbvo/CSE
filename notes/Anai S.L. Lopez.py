import random

bank = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'violet']
word = random.choices(bank)
answer = list(word)
guesses_left = 8
guessed = []

while guesses_left > 0:
    guess = input("Enter a letter: ")
    for guess in answer:
        print("%s is in the word" % guess)
        answer = "".join(answer)
        print("congratulations! that's the answer")
        exit()
    else:
        print("%s is not in the word" % guess)
        guesses_left -= 1

guessed = "".join(guessed)
print("You've guessed this so far: ")
guess = input("insert guess: ")


if guessed in answer:
    print("you have already guesses that!")
while guess in word:
    answer = list(answer)
    current_index = word.index(guessed)
    word.pop(current_index)
    word.index(current_index, "-")
    answer = "".join(answer)
    print("nope")
    correct = "correct"
true = "".join(true)
