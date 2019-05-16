class Room(object):
    def __init__(self, name, description, av_dir, long_desc, north=None, north_east=None, north_west=None,
                 south=None, south_east=None, south_west=None, east=None, west=None):
        self.name = name
        self.north = north
        self.north_east = north_east
        self.north_west = north_west
        self.south = south
        self.south_east = south_east
        self.south_west = south_west
        self.east = east
        self.west = west
        self.description = description
        self.av_dir = av_dir
        self.long_desc = long_desc
        self.items = []
        self.characters = []


class Player(object):
    def __init__(self, name, description, starting_location):
        self.name = name
        self.description = description
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room
        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.
        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


ME = Player("me", "it's me",)


class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print("Would you like to pick up this item?")
        answer = input(">_")
        if answer.upper() in ['YES']:
            ME.inventory.append(self)
            print("you picked up:", self.name)
            print(ME.inventory)
        if answer.upper() in ['NO']:
            print("you did not pick up:", self.name)
            print(ME.inventory)
