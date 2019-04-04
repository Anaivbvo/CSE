class Player(object):
    def __init__(self, health_level, hydration_level, social_level):
        self.health_level = health_level
        self.hydration_level = hydration_level
        self.social_level = social_level


me = Player(10, 10, 10)


class ConsumableLiquid(object):
    def __init__(self, name, description, hydration_plus):
        self.name = name
        self.description = description
        self.hydration_plus = hydration_plus

    def drink(self):
        print("Would you like to drink:", self.name, "?")
        answer = input(">_")
        if answer.lower() in ['yes']:
            print("You drank: ", self.name)
            me.hydration_level += self.hydration_plus
            print("You've gained: ", self.hydration_plus, "on hydration level!")
        elif answer.lower() in ['no']:
            print("You save", self.name, "for later.")
        else:
            self.drink()


class ConsumableSolid(object):
    def __init__(self, name, description, health_plus):
        self.name = name
        self.description = description
        self.health_plus = health_plus

    def eat(self):
        print("Would you like to eat: ", self.name, "?")
        answer = input(">_")
        if answer.lower() in ['yes']:
            print("You ate:", self.name)
            me.health_level += self.health_plus
            print("You've gained: ", self.health_plus, "on health level!")
        elif answer.lower() in ['no']:
            print("You save", self.name, "for later.")
        else:
            self.eat()


class Items(object):
    def __init__(self, name, description, social_plus):
        self.name = name
        self.description = description
        self.social_plus = social_plus

    def when_trade(self):
        print("You've gained:", self.social_plus, "on your social level!")
        me.social_level += self.social_plus


Water = ConsumableLiquid("Water", "Fresh cold water! perfect for a hot day! a plus 20 on your hydration level!", 20)
Milk = ConsumableLiquid("Milk", "School milk. It's cold too.", -1)
Arizona = ConsumableLiquid("Arizona", "nayeli", 5)
GrossSamwitch = ConsumableSolid("sandwich", "a chicken sandwich from the school food.", -5)
print("%s: %s" % (Water.name, Water.description))

