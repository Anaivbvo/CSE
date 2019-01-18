import random
bank = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
guesses = 8

word = random.choices(bank)
print(word)
word2 = list(word)
print(word2)
print(len(word2))
word3 = word.split(' ')
print(word3)
