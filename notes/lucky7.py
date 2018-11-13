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
print("First dice is: %d." % FirstDice)
print("Second dice is: %d." % SecondDice)
Adding = (FirstDice + SecondDice)
 if Adding is 7:
     print("Congratulations! You rolled a lucky 7!")
     Money = (Money + 5)
     print(Money)
 else:
     print("You lost, better luck next time.")
     Money = (Money - 1)
     print(Money)
     