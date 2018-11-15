import random

Rounds = 1
BestRounds = 1
Money = 15
MostMoney = Money

print("You have 15 dollars so far! Let's see if you can keep this money, or lose it all!")
print("Money/{Dollars} so far:")
print(Money)

while Money > 0:
    if MostMoney < Money:
        MostMoney = Money
        BestRounds = Rounds
Rounds = (Rounds + 1)
print(" You have %s dollars." % Money)
FirstDice = random.randint(1, 6)
SecondDice = random.randint(1, 6)
print(" First Dice is %s." % FirstDice)
print(" Second Dice is %s." % SecondDice)
Adding = (FirstDice + SecondDice)
if Adding is 7:
    print("Congratulations! You rolled a lucky 7!!!")
    Money = (Money + 5)
    print(Money)
else:
    print(" Aww, you lost the bet! Better luck next time!")
    Money = (Money - 1)
    print(Money)