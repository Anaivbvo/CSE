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
