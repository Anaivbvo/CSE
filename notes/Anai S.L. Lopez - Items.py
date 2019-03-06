health_level = 50
social_level = 0
reed_harm = False

# Consumable


class Consumable(object):
    def __init__(self, name):
        self.name = name


class Sweet(Consumable):
    def __init__(self, name):
        super(Sweet, self).__init__(name)


class AppleSlices(Sweet):
    def __init__(self, name, reed_harm):
        super(AppleSlices, self).__init__(name)
        self.reed_harm = True


# Equipment
class Equipment(object):
    def __init__(self, name):
        self.name = name


# Instruments
class Instruments(object):
    def __init__(self, name):
        self.name = name


# Papers
class Papers(object):
    def __init__(self, name):
        self.name = name
