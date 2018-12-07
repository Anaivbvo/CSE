import random
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
    FirstDice = random.randint(0, 6)
    SecondDice = random.randint(0, 6)
    print("Dice #1 is %s" % FirstDice)
    print("Dice #2 is %s" % SecondDice)
    Adding = (FirstDice + SecondDice)
    if Adding is 7:
        print("Congratulations! You got a lucky 7!")
        Money = (Money + 5)
        print(Money)
    else:
        print("Aww you lost the bet! Too bad!")
        Money = (Money - 1)
        print(Money)
print("The number of rounds to run out money is: %s" % Money)
print("You should have stopped at round %d when you had %d dollars" % (BestRounds, MostMoney))
