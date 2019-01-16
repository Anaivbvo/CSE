mainStr = "Hello, This is a sample string"

otherStr = mainStr.replace('s', 'X')

print(otherStr)

"""
guesses = 8
while guesses < 0:
    guess = input("Try to guess the word! You have 8 tries! : ")
    if input == random.choices(colors):
        print("You won!")
    else:
        guesses = guesses - 1
        print("Aww too bad! Try again!")
if guesses == 0:
    print("Aww! You ran out guesses!")
    print("The word you were trying was: ")
    print(word)
    
"""

x = ["abbbb", "123a", "nnnnas"]
xi = [s.replace('a', 'b') for s in x]
print(xi)
