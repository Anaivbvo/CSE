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


class Noodles(Consumable):
    def __init__(self, name, description):
        super(Noodles, self).__init__(name, health=10)
        self.name = name
        self.description = description
        self.amount = Player.health + 10
