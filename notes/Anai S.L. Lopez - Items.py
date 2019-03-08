class Player(object):
    def __init__(self, name, health=100, social=10, hydration=100, ):
        self.name = name
        self.health = health
        self.social = social
        self.hydration = hydration
        self.inventory = []

    def name(self):
        name = input("Helli, what is your name? >_ ")
        Player.name = name

    def health_gained(self, amount):
        self.health += amount


class Consumable(Item):

    def __init__(self, name, health):
        super(Consumable, self).__init__(name)
        self.health = health

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


class Noodles(Consumable):
    def __init__(self, name, description):
        super(Noodles, self).__init__(name, health=10)
        self.name = name
        self.description = description
        self.amount = Player.health + 10


ME = Player()
