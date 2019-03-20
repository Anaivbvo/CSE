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


me = Player("me", "it's me", "freshmen", 10, 10, 10)
me.inventory = ['bread', 'noodles', 'water']

# Characters


class Characters(object):
    def __init__(self, name, description, rank, sorry):
        self.name = name
        self.description = description
        self.rank = rank
        self.sorry = sorry
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
                    print("'Awesome! Alright then looks like you got a deal!'")
                    me.inventory.remove(character_want)
                    self.inventory.append(character_want)
                    me.inventory.append(wanted_item)
                    self.inventory.remove(wanted_item)
                    print("((Awesome! You know have ", wanted_item, " but lost ", character_want, ".")
                    me.social += 5
                    print("((You gained plus 5 on your social level!")
                elif answer.upper() in ['NO']:
                    print(self.name, ":")
                    print("'Aw that's too bad, well maybe someone else might have the item for a different price.")
                    print("'Come back to me when you're ready for a good deal1'")
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


print("The director has given you a mission to find blank paper, but you don't have any on you at the moment.")
print("determined to impress the director you ask around your section!")
print("oh! there's a member!")
Nathaniel = Characters("Nathaniel", "he's part of ur section", "sophomore", "sorry pal,")
print(Nathaniel.name, Nathaniel.description, Nathaniel.rank)
Nathaniel.inventory = ['hat', 'ice', 'energy drink']
Nathaniel.trade()
print("hmm... you go ask someone else..")
print("oh! there's someone else!")
Sergio = Characters("Sergio", "sophomore symphonic section leader Sergio", "sophomore", "yeah uh, ")
print(Sergio.name, Sergio.description, Sergio.rank)
Sergio.inventory = ['alto reed 2.5', 'sports drink', 'empty folder']
Sergio.trade()
print("you go off still in search for paper!. seems like neither of the sophomore have that..")
print("hey there's someone else!")
Cody = Characters("Cody", "next year section leader Cody~", "junior", "sorry buddy,")
print(Cody.name, Cody.description, Cody.rank)
Cody.inventory = ['water', 'alto reed 3.5', 'neck strap', 'cap']
Cody.trade()
