

# Consumable


class Player(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.health_level = 100
        self.hydration_level = 100
        self.social_level = 10
        self.inventory = []


class Consumable(object):
    def __init__(self, name):
        self.name = name

    def Eat(self, health):
        self.health = health
        print("You ate the item.")
        print("You gained", health, " health.")


class AppleSlices(Consumable):
    def __init__(self, name, description):
        super(AppleSlices, self).__init__(name)
        self.name = name
        self.description = description
        self.health = Player.health_level + 2