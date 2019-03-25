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
    def __init__(self, name, description, rank, sorry, alright):
        self.name = name
        self.description = description
        self.rank = rank
        self.sorry = sorry
        self.alright = alright
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
