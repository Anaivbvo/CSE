import random


# Player
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
        self.want = []
        self.area = area


