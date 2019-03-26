class LiquidConsumable(object):
    def __init__(self, name, description, health_plus, hydration_plus):
        self.name = name
        self.description = description
        self.health_plus = health_plus
        self.hydration_plus = hydration_plus

    def drink(self):