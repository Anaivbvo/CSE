# Player
class Player(object):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.social = 10
        self.hydration = 20
        self.inventory = []

    def health_gained(self, amount1):
        self.health += amount1

    def hydration_gained(self, amount2):
        self.hydration += amount2

    def eat(self):
        print("Do you want to eat this item?")
        answer = input(">_")
        if answer.upper() in ['YES']:
            print("You ate the ", Consumable, ".")
            print(Consumable.description)
            Player.health = Player.health + Consumable.health
            print("You have gained, ", Consumable.health, "in health.")
        if answer.upper() in ['NO']:
            print("You have decided to not eat the ", Consumable, ".")

    def hydration_level(self):
        if self.hydration < 5:
            print("You're hydration levels are low! Be sure you are drinking the necessary amount of water.")
            print("this year's summer is hotter than usual. Drink water next time you have the chance.")
            print(self.hydration)

    def health_level(self):
        if self.health < 5:
            print("You are running low on health! make sure you're eating properly and staying hydrated!")
            print(self.health)

    def passing_out(self):


# Consumables

class Apple(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.amount1 = 5
        self.amount2 = 3


class Fries(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.amount1 = 7
        self.amount2 = -3


# Liquids

class FreshWater(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.amount1 = 0
        self.amount2 = 10


class SportsDrink(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.amount1 = 0
        self.amount2 = 12


# Health items


class SunScreen(object)