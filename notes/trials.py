import random

"""
- with every wrong letter chosen the number of guesses goes down
- rewrite the whole sentence after each turn
- every letter guessed is made into a list
- one one turn you have the number of guesses left, the sentence itself, and the list of letters guessed
"""

# Ex:
list1 = ["item0", "item1", "item2"]
print(list1)

"""
# Try 1:
hangman1 = []
print(hangman1)
hangman1.append("rhythm")

hangman1A = input("Try to guess the word! You have 8 tries!: ")
print("______")
guesses = 8
while guesses <0:
 if input == hangman1:
    print("You won!")
 else:
    guesses = guesses - 1
    print("Wrong letter, try again!")
"""

# Try 2:

hangman2 = []
print(hangman2)
hangman2.append("spoon")

guesses = 8

while guesses < 0:
    hangman2A = input("Try to guess the word! You have 8 tries! : ")
    if input == hangman2:
        print("You won!")
    else:
        guesses = guesses - 1
        print("Aww too bad! Try again!")
""""""

bank = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
guesses = 8

word = random.choices(bank)

"""
import random
bank = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'violet']
word = random.choices(bank)
letter_in_word = list(word)
guesses_left = 8
list_of_guesses = []
print(letter_in_word)

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
    print("You ran out of guesses!")
"""

"""
import random
bank = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'violet']

word_found = False
word_choice = random.choice(bank)
found = []

for i in range(0, len(word_choice)):
    found.append("-")

def check_found(found):
    global word_choice
    looper = 0
    for i in found:
        if i != "-":
            looper += 1
    if looper == len(word_choice):
        return True

while not word_found:
    print(" ".join(found))
    letter = input("Enter a letter: ")
    looper = 0
    for i in word_choice:
        if i == letter:
            found[looper] = i
            looper += 1
            checker = check_found(found)
            if checker == True:
                letter_found = True
    if letter == word_choice:
        print("done")
"""

"""while guesses_left > 0:
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
true = "".join(true)"""