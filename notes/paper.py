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
me.inventory = ['fries', 'noodles', '2nd chair music', 'water', 'pencil']

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


print("The director has given you a mission to find blank paper, but you don't have any on you at the moment.")
print("determined to impress the director you ask around your section!")
print("oh! there's a member!")
print("-"*10)
Nathaniel = Characters("Nathaniel", "he's part of ur section", "sophomore", "sorry pal,", "Cool!")
print(Nathaniel.name, "-", Nathaniel.description, "-", Nathaniel.rank)
print("You ask Nathaniel in search for paper!")
Nathaniel.inventory = ['sunglasses', '1st chair music', 'spicy noodles', 'energy drink', 'chocolate']
Nathaniel.trade()
print("-"*10)
print("hmm... you go ask someone else..")
print("oh! there's someone else!")
print("-"*10)
Sergio = Characters("Sergio", "sophomore symphonic section leader Sergio", "sophomore", "yeah uh,", "Okay,")
print(Sergio.name, "-", Sergio.description, "-", Sergio.rank)
print("You ask Sergio in search for paper!")
Sergio.inventory = ['alto reed 2.5', 'sports drink', 'empty folder', '1st chair music', 'chips']
Sergio.trade()
print("-"*10)
print("you go off still in search for paper!. seems like neither of the sophomore have that..")
print("hey there's someone else!")
Cody = Characters("Cody", "next year section leader Cody~", "junior", "sorry buddy,", "Nice!")
print(Cody.name, "-", Cody.description, "-", Cody.rank)
print("You ask Cody in search for paper!")
Cody.inventory = ['water', 'alto reed 3.5', 'neck strap', 'cap', 'flip book']
Cody.trade()
print("Seems like they didn't have it either.. You go look for one last person... your section leader..")


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
        if wanted_item.upper() in ['PAPER']:
            print(self.name, ":")
            print("Haha sorry no can do!")
            print("The director asked me first for paper! I'm on my way to giving ")

Andrew = Characters("Andrew", "Senior Section Leader Andrew", "Senior", "Hm,", "Alright,")
print("You ask Andrew in search for paper!")
Andrew.inventory = ['alto reed 4', 'paper', '1st chair music', 'water', 'neck strap']
Andrew.trade()
