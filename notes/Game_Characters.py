import random


# Person
class Person(object):
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
        self.want = random.choices(Person.inventory)
        self.area = area

    def trade(self):
        print("((What would you like from ", self.name, "?))")
        print(self.inventory)
        wanted_item = input(">_")
        if wanted_item in self.inventory:
            print("'Alright I see, well in return I would like ", self.want, ".'")
            print("((Do you have the item?))")
            if character_want in Person.inventory:
                print(Person.inventory)
                print("((You do have the item, trade?))")
                answer = input(">_")
                if answer.upper() in ['YES']:
                    print(self.name, ":")
                    print("'Awesome! Alright then looks like you got a deal!'")
                    Person.inventory.remove(character_want)
                    self.inventory.append(character_want)
                    Person.inventory.append(wanted_item)
                    self.inventory.remove(wanted_item)
                    print("((Awesome! You know have ", wanted_item, " but lost ", character_want, ".")
                    Person.social += 5
                    print("((You gained plus 5 on your social level!")
                elif answer.upper() in ['NO']:
                    print(self.name, ":")
                    print("'Aw that's too bad, well maybe someone else might have the item for a different price.")
                    print("'Come back to me when you're ready for a good deal1'")
            elif character_want not in Person.inventory:
                print(Person.inventory)
                print("((Hmm.. Seems like you don't have the item...))")
                print(self.name, ":")
                print("'Oh well... I'm sure someone else might be able to trade ", wanted_item, "for something ya got.")
        elif wanted_item not in self.inventory:
            print(self.name, ":")
            print("'Sorry pal, don't have that on me right now. You can try asking others.")


me = Person("me", "it's me", "freshmen", 10)
me.inventory = ["hat", "cookie", "recorder"]
upperclassmen = Character("sophomore", "2nd year", "sophomore", "band_tree")
upperclassmen.inventory = ["sax_reed", "water", "bread"]
upperclassmen.trade()
