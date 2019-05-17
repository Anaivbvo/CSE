import random


class Player(object):
    def __init__(self, name, description, health_level, hydration_level, social_level,):
        self.name = name
        self.description = description
        self.health_level = health_level
        self.hydration_level = hydration_level
        self.social_level = social_level
        self.inventory = []

    def health_gained(self, amount1):
        self.health_level += amount1

    def hydration_gained(self, amount2):
        self.hydration_level += amount2

    def hydration_level_low(self):
        if self.hydration_level() < 5:
            print("You're hydration levels are low! Be sure you are drinking the necessary amount of water.")
            print("this year's summer is hotter than usual. Drink water next time you have the chance.")
            print(self.hydration_level())

    def health_level_low(self):
        if self.health_level() < 5:
            print("You're hydration levels are low! Be sure you are eating well and healthy!!")
            print("We're doing a lot of work than last year! Eat well when you get the chance.")
            print(self.health_level())


me = Player("me", "it's me", 100, 100, 50)


# Items ----------
class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print("Would you like to pick up this item?")
        answer = input(">_")
        if answer.upper() in ['YES']:
            me.inventory.append(self)
            print("you picked up:", self.name)
            print(me.inventory)
        if answer.upper() in ['NO']:
            print("you did not pick up:", self.name)
            print(me.inventory)


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


class Wearable(HealthItems):
    def __init__(self, name, description, health_plus):
        super(Wearable, self).__init__(name, description, health_plus)
        self.name = name
        self.description = description
        self.health_plus = health_plus


class Music(Items):
    def __init__(self, name, description, section, chair, social_plus):
        super(Music, self).__init__(name, description)
        self.name = name
        self.description = description
        self.section = section
        self.section = section
        self.chair = chair
        self.social_plus = social_plus


# ITEMS ----------------------------------------------------------------------------------------------------------------
# Liquids -----
WATER = ConsumableLiquid("Water", "Fresh and cold water you brought from home! It even has ice!", 15, 5)
MILK = ConsumableLiquid("Milk", "Cold school plain milk. Nothing special about it.", 7, 2)
SPORTS_DRINK = ConsumableLiquid("Sports Drink", "This is the usual brand of sports drink everyone brings to camp. "
                                "Refreshing, fruity, and energy giving!", 10, 15)
ARIZONA = ConsumableLiquid("Arizona", "This is most everyone's favorite juice. This can most definitely bring up your "
                                      "social level, though how sweet it is, it may not be as nice with your health "
                                      "level.", 4, 8)
REBEL = ConsumableLiquid("Rebel Energy Drink", "Every one loves this energy drink! Though it's not as healthy as water,"
                                               " everyone craves for this after practice.", 2, 15)
# Solids -----
APPLE = ConsumableSolid("Apple", "A nice red apple! Sweet but solid! Though everyone likes junk food, no one could "
                                 "decline a nice apple!", 10, 5)
FRIES = ConsumableSolid("Mac's Fries", "Everyone loves fried! Though it'snot the healthiest item, but that doesnt stop"
                                       " anyone from eating them!", 10, 15)
BURGER = ConsumableSolid("Mac's Burger", "A cheese burger! If you'd compare this to Mac's Fries, you'd think the "
                                         "burger was the side option. Though this is a whole meal for anyone after "
                                         "practice!", 8, 12)
SANDWICH = ConsumableSolid("School Sandwich", "Since this is a school food, you never know if this sandwich is any "
                                              "good or bad...", random.randint(-20, 20), random.randint(-5, 5))
SALAD = ConsumableSolid("Salad", "School's salad. This is a surprise whether you feel better or worse after eating "
                                 "this...", random.randint(-10, 10), random.randint(-5, 5))
# Health -----
SUN_SCREEN = HealthItems("Sun Screen", "Sun screen helps you stay protected! This is the type the band provides to "
                         "every student. Safe for every student and very protective!", 25,)
ENERGY_SHOT = HealthItems("Energy", "A mini energy drink! Has the necessary proteins and energy giving for incoming"
                          " activities.", 10)
# Music -----
ALTO1A = Music("First chair Alto", "Alto Section Leader's music. A rare item to get a hold of since they are always"
                                   " organized with their music!", "Saxes", "1st", 20)
ALTO1B = Music("2nd First chair Alto", "Music for the next in command! although this is 1st chair music, it seems to "
                                       "be just a tad different from the Section leader's music.", "Saxes", "1st", 15)
ALTO2A = Music("Second Chair Alto", "Music for the second chairs.. Which seems to be majority of the section. Not too"
                                    "different from the 1st chair.. except everything.", "Saxes", "2nd", 5)
