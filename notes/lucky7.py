import random.
Rounds = 1
BestRounds = 1
Money = 15
MostMoney = Money

while Money > 0:
 if MostMoney < Money:
    MostMoney = Money
    BestRounds = Rounds
Rounds = (Rounds + 1)
print("You have %d dollars." % Money)

FirstDice = random.randint(1, 6)
SecondDice = random.randint(1, 6)

DiceTotal = (FirstDice + SecondDice)