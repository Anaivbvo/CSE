# Consumable
class Consumable(object):
    def __init__(self, name, health, hydration):
        super(Consumable, self).__init__(name)
        self.health = health
        self.hydration = hydration


# Solids
class Apples(Consumable):
    def __init__(self, name, description):
        super(Apples, self).__init__(name, health=12, hydration=2)
        self.name = name
        self.description = description
        self.amount = Player.health + 12
        self.amount1 = Player.hydration + 2


class Gum(Consumable):
    def __init__(self, name, description):
        super(Gum, self).__init__(name, health=0, hydration=0)
        self.name = name
        self.description = description
        self.amount = Player.health + 0
        self.amount1 = Player.hydration + 0


class Noodles(Consumable):
    def __init__(self, name, description):
        super(Noodles, self).__init__(name, health=10, hydration=4)
        self.name = name
        self.description = description
        self.amount = Player.health + 10
        self.amount1 = Player.hydration + 4


class Fries(Consumable):
    def __init__(self, name, description):
        super(Fries, self).__init__(name, health=8, hydration=-5)
        self.name = name
        self.description = description
        self.amount = Player.health + 4
        self.amount1 = Player.hydration - 5


# Liquids
class FreshWater(Consumable):
    def __init__(self, name, description):
        super(FreshWater, self).__init__(name, health=0, hydration=15)
        self.name = name
        self.description = description
        self.amount = Player.health + 0
        self.amount1 = Player.hydration + 15


class FountainWater(Consumable):
    def __init__(self, name, description):
        super(FountainWater, self).__init__(name, health=0, hydration=5)
        self.name = name
        self.description = description
        self.amount = Player.health + 0
        self.amount1 = Player.hydration + 5