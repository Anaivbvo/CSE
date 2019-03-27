import random


class Player(object):
    def __init__(self, health_level, hydration_level, social_level):
        self.health_level = health_level
        self.hydration_level = hydration_level
        self.social_level = social_level


me = Player(10, 10, 10)


class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ConsumableLiquid(Items):
    def __init__(self, name, description, hydration_plus, social_plus):
        super(ConsumableLiquid, self).__init__(name, description)
        self.name = name
        self.description = description
        self.hydration_plus = hydration_plus
        self.social_plus = social_plus

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


class ConsumableSolid(Items):
    def __init__(self, name, description, health_plus, social_plus):
        super(ConsumableSolid, self).__init__(name, description)
        self.name = name
        self.description = description
        self.health_plus = health_plus
        self.social_plus = social_plus

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


class HealthItems(Items):
    def __init__(self, name, description, health_plus):
        super(HealthItems, self).__init__(name, description)
        self.name = name
        self.description = description
        self.health_plus = health_plus

    def use(self):
        print("Would you like to use the item?")
        answer = input(">_")
        if answer in ['yes']:
            print("you used the item: ", self.name)
            me.health_level += self.health_plus
            print("you've gained:", self.health_plus, "in your health level!")


class Music(Items):
    def __init__(self, name, description, section, chair, social_plus):
        super(Music, self).__init__(name, description)
        self.name = name
        self.description = description
        self.section = section
        self.section = section
        self.chair = chair
        self.social_plus = social_plus


Water = ConsumableLiquid("Water", "Fresh and cold water you brought from home! It even has ice!", 15, 5)
Milk = ConsumableLiquid("Milk", "Cold school plain milk. Nothing special about it.", 7, 2)
SportsDrink = ConsumableL4("Sports Drink", "This is the usual brand of sports drink everyone brings to camp. "
                                           "Refreshing, fruity, and energy giving!", 10, 15)
Arizona = ConsumableLiquid("Arizona", "This is most everyone's favorite juice. This can most definitely bring up your "
                                      "social level, though how sweet it is, it may not be as nice with your health "
                                      "level.", 4, 8)
Rebel = ConsumableLiquid("Rebel Energy Drink", "Every one loves this energy drink! Though it's not as healthy as water,"
                                               " everyone craves for this after practice.", 2, 15)
Apple = ConsumableSolid("Apple", "A nice red apple! Sweet but solid! Though everyone likes junk food, no one could "
                                 "decline a nice apple!", 10, 5)
Fries = ConsumableSolid("Mac's Fries", "Everyone loves fried! Though it'snot the healthiest item, but that doesnt stop"
                                       " anyone from eating them!", 10, 15)
Burger = ConsumableSolid("Mac's Burger", "A cheese burger! If you'd compare this to Mac's Fries, you'd think the "
                                         "burger was the side option. Though this is a whole meal for anyone after "
                                         "practice!", 8, 12)
Sandwich = ConsumableSolid("School Sandwich", "Since this is a school food, you never know if this sandwich is any "
                                              "good or bad...", random.randint(-20, 20), random.randint(-5, 5))
Salad = ConsumableSolid("Salad", "School's salad. This is a surprise whether you feel better or worse after eating "
                                 "this...", random.randint(-10, 10), random.randint(-5, 5))
SunScreen = HealthItems()
EnergyShot = HealthItems()
Alto1A = Music()
Alto1B = Music()
Alto2A = Music()