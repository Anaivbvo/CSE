import random


# Player ----------
class Player(object):
    def __init__(self, health_level, hydration_level, social_level):
        self.health_level = health_level
        self.hydration_level = hydration_level
        self.social_level = social_level
        self.inventory = []


me = Player(10, 10, 10)


# Items ----------
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
SportsDrink = ConsumableLiquid("Sports Drink", "This is the usual brand of sports drink everyone brings to camp. "
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
SunScreen = HealthItems("Sun Screen", "Sun screen helps you stay protected! This is the type the band provides to "
                                      "every student. Safe for every student and very protective!", 25,)
EnergyShot = HealthItems("Energy", "A mini energy drink! Has the necessary proteins and energy giving for incoming"
                                   " activities.", 10)
Alto1A = Music("First chair Alto", "Alto Section Leader's music. A rare item to get a hold of since they are always"
                                   " organized with their music!", "Saxes", "1st", 20)
Alto1B = Music("2nd First chair Alto", "Music for the next in command! although this is 1st chair music, it seems to "
                                       "be just a tad different from the Section leader's music.", "Saxes", "1st", 15)
Alto2A = Music("Second Chair Alto", "Music for the second chairs.. Which seems to be majority of the section. Not too"
                                    "different from the 1st chair.. except everything.", "Saxes", "2nd", 5)


class Characters(object):
    def __init__(self, name, description, rank, grade, group, sorry, alright, them, last_year, this_year, section):
        self.name = name
        self.description = description
        self.rank = rank
        self.grade = grade
        self.group = group
        self.sorry = sorry
        self.alright = alright
        self.them = them
        self.last_year = last_year
        self.this_year = this_year
        self.section = section
        self.inventory = []

    def trade(self):
        print("((What would like from ", self.name, "?))")
        for num, item in enumerate(self.inventory):
            print(str(num + 1) + ": " + item.name)
        wanted_item = input(">_")
        if wanted_item in self.inventory:
            character_want = random.choice(me.inventory)
            print("'Alright I see, well in return I would like ", character_want, ".'")
            print("((Do you have the item?))")
            if character_want in me.inventory:
                print(me.inventory)
                print("((You do have the item, trade?))")
                answer = input(">_")
                if answer.upper() in ['YES']:
                    print(self.name, ":")
                    print(self.alright, "looks like you got a deal!'")
                    me.inventory.remove(character_want)
                    self.inventory.append(character_want)
                    me.inventory.append(wanted_item)
                    self.inventory.remove(wanted_item)
                    print("((Awesome! You know have ", wanted_item, " but lost ", character_want, ".")
                    me.social += 5
                    print("((You gained plus 5 on your social level!")
                elif answer.upper() in ['NO']:
                    print(self.name, ":")
                    print(self.sorry, ", well maybe someone else might have", wanted_item, "for a different price.")
            elif character_want not in me.inventory:
                print(me.inventory)
                print("((Hmm.. Seems like you don't have the item...))")
                print(self.name, ":")
                print("'Oh well... I'm sure someone else might be able to trade ", wanted_item, "for something ya got.")
        elif wanted_item not in self.inventory:
            print(self.name, ":")
            print(self.sorry, "don't have that on me right now. You can try asking others.")
            print("is there anything else you want?")
            answer = input(">_")
            if answer.upper() in ['YES']:
                return self.trade()
            elif answer.upper() in ['NO']:
                print(self.sorry, "you're better off asking someone else..")

    def talk_to(self):
        print("You've approached: ", self.name)
        print("What would you like to talk about?")
        print("'1. Them', '2. Band last year', '3. Band this year', '4. Their section'")
        answer = input(">_")
        if answer.lower() in ['Them', 'them', '1']:
            print(self.them)
            print("-"*5)
            print("You've learned more about:", self.name)
            print("You've gained +10 on your social level!")
            print("-"*5)
            Player.social += 10
        elif answer.lower() in ['Band last year', 'Band Last Year', 'band last year', '2']:
            print(self.last_year)
            print("-" * 5)
            print("You know now more about the band and about", self.name, "!")
            print("You've gained +10 on your social level!")
            print("-" * 5)
            Player.social += 10
        elif answer.lower() in ['Band this year', 'Band This Year', 'band this year', '3']:
            print(self.this_year)
            print("-" * 5)
            print("You now know how", self.name, "really thinks of your year, whether its a good or bad thing..")
            print("you've gained +10 on your social level!")
            print("-" * 5)
            Player.social += 10
        elif answer.lower() in ['Their section', 'their section', 'Their Section', '4']:
            print(self.section)
            print("-" * 5)
            print("You now know now more about", self.name, "and the", self.group)
            print("You've gained +10 on your social level!")
            print("-" * 5)
            Player.social += 10
        elif answer.lower() in other:
            print("??? Do you wan't to repeat that again?")
            self.talk_to()

    def check(self):
        print("This is:", self.name)
        print("-"*3)
        print(self.name)
        print("-" * 1)
        print(self.description)
        print("-" * 1)
        print(self.rank)
        print("-" * 1)
        print(self.grade)
        print("-" * 1)
        print(self.group)
        print("-" * 1)


Max = Characters("Max", "Senior High brass section leader", "Section Leader", "Senior/12th", "High brass/Horns",
                 "ah sorry,", "cool then,", "I'm Max! The high brass section leader! I've done marching band all four "
                 "years! Thanks to that i have the best girl by my side and the most talented section!", "Last year "
                 "was great!.. That's a lie.. We won sweeps the year before, but for what ever reason we've all gone "
                 "downhill.. Do your best this year! Who knows! We might win something above 1st!", "This year seems"
                 "to be starting really off.. Don't let that bother you though, just do your best!", "High brass?"
                 "They're the best! We are the best!",)
Max.inventory = [Apple, Water, Milk]
me.inventory = [Alto2A, Arizona, Fries]
Max.trade()
