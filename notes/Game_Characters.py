import random
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
    def __init__(self, name, description, rank):
        self.name = name
        self.description = description
        self.rank = rank
        self.inventory = inventory

    def trade(self):
        print("((What would like from ", self.name, "?))")
        print(self.inventory)
        wanted_item = input(">_")
        if wanted_item in self.inventory:
            character_want = random.choice(Player.inventory)
            print("'Alright I see, well in return I would like ", character_want, ".'")
            print("((Do you have the item?))")
            if character_want in Player.inventory:
                print(Player.inventory)
                print("((You do have the item, trade?))")
                yes = ['YES']
                no = ['NO']
                answer = input(">_")
                if answer.upper() in yes:
                    print(self.name, ":")
                    print("'Awesome! Alright then looks like you got a deal!'")
                    Player.inventory.remove(character_want)
                    self.inventory.append(character_want)
                    Player.inventory.append(wanted_item)
                    self.inventory.remove(wanted_item)
                    print("((Awesome! You know have ", wanted_item, " but lost ", character_want, ".")
                    Player.social += 5
                    print("((You gained plus 5 on your social level!")
                elif answer.upper() in no:
                    print(self.name, ":")
                    print("'Aw that's too bad, well maybe someone else might have the item for a different price.")
                    print("'Come back to me when you're ready for a good deal1'")
            elif character_want not in Player.inventory:
                print(Player.inventory)
                print("((Hmm.. Seems like you don't have the item...))")
                print(self.name, ":")
                print("'Oh well... I'm sure someone else might be able to trade ", wanted_item, "for something ya got.")
        elif wanted_item not in self.inventory:
            print(self.name, ":")
            print("'Sorry pal, don't have that on me right now. You can try asking others.")
