import random


# Player
<<<<<<< HEAD
class Player(object):
=======
class Person(object):
>>>>>>> d354a71ab42e7610245c2c72f0e614ae07b74b86
    def __init__(self, name, description, rank, social):
        self.name = name
        self.description = description
        self.rank = rank
        self.social = social
        self.inventory = []
# Character


class Character(object):
    def __init__(self, name, description, rank, area):
        self.name = name
        self.description = description
        self.rank = rank
        self.inventory = []
<<<<<<< HEAD
=======
        self.want = []
        self.area = area
>>>>>>> d354a71ab42e7610245c2c72f0e614ae07b74b86

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


<<<<<<< HEAD
me = Player("me", "it's me", "freshmen", 10)
me.inventory = ["hat", "glasses", "sax_reed"]
upperclassmen = Character("sophomore", "they're in your section, a 2nd year.", "sophomore")
=======
Player = Person("me", "it's me", "freshmen", 10)
Player.inventory = ["hat", "glasses", "sax_reed"]
upperclassmen = Character("sophomore", "they're in your section, a 2nd year.", "sophomore", None)
>>>>>>> d354a71ab42e7610245c2c72f0e614ae07b74b86
upperclassmen.inventory = ["cork_grease", "sax_strap", "water"]
