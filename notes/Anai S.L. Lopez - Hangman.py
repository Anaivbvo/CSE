import random
word_bank = ["absolute", "abstract", "academic", "accepted", "accident", "accuracy", "accurate", "achieved"]

guessed = []
random_word = random.choice(word_bank)
word = list(random_word)
true = list(word)
answer = "".join(word)
line = ""

for letter in word:
    line = line + "-"
    answer = answer.replace(answer, line)

correct = 7

while correct > 0:
    print(answer)
    answer = list(answer)
    if true == answer:
        answer = "".join(answer)
        print("you'vbe guessed correctly!! the word was %s" % answer)
        exit()
    guessed = "".join(guessed)
    print("letters you've guessed: %s" % guessed)
    guessed = list(guessed)
    guess = input("guess >_")
    guessed.append(guess)
    if guess in answer:
        print("you already guessed this")
        answer = "".join(answer)

    if guess.swapcase() in word:
        guess = guess.swapcase()
    while guess in word:
        answer = list(answer)
        current_index = word.index(guess)
        word.pop(current_index)
        word.insert(current_index, "-")
        answer.pop(current_index)
        answer.insert(current_index, guess)
        answer = "".join(answer)
        if guess.swapcase() in word:
            guess = guess.swapcase()
    if guess not in word and guess not in answer:
        answer = "".join(answer)
        print("try again:")
        correct = correct - 1
true = "".join(true)
print("the answer was %s" % true)
