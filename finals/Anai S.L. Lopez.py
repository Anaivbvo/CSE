HealthLevel = 100
SocialLevel = 0
ReedLevel = 100

# Consumable


class Reed(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.ReedHarm = False


class Consumable(object):
    def __init__(self, name):
        self.name = name


class AppleSlices(Consumable):
    def __init__(self, name, description, health, harm):
        super(AppleSlices, self).__init__(name)
        self.name = name
        self.description = description
        self.health = health
        self.harm = harm


class Gum(Consumable):
    def __init__(self, name, description, health):
        super(Gum, self).__init__(name)
        self.name = name
        self.description = description
        self.health = health
        self.ReedHarm = False


class Noodle(Consumable):
    def __init__(self, name, description, health, harm):
        super(Noodle, self).__init__(name)
        self.name = name
        self.description = description
        self.health = health
        self.harm = harm


class Fries(Consumable):
    def __init__(self, name, description, health, harm):
        super(Fries, self).__init__(name)
        self.name = name
        self.description = description
        self.health = health
        self.harm = harm


