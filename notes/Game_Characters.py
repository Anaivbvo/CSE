import random
import Game_Items

# Player


class Player(object):
    def __init__(self, name, description, rank, health, hydration, social):
        self.name = name
        self.description = description
        self.rank = rank
        self.health = health
        self.hydration = hydration
        self.social = social
        self.inventory = []


# Characters


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
        print(self.inventory)
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
