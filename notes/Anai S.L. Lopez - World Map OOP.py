class Room(object):
    def __init__(self, name, north=None, north_east=None, north_west=None, south=None, south_east=None,
                 south_west=None, east=None, west=None, description=None, av_dir=None, paths=None):
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
        self.paths = paths


TREE1 = Room("Band_Tree")
TREE2 = Room("Hangout_Tree")
TABLE =
OUTER_STAGE =
BACK_STAGE =
STAGE =
CAFETERIA =
JANITOR_ROOM =
WATER_FOUNTAIN =
FOOD_BOOTHS
KITCHEN =
BAND_ROOM =
OFFICE =
DRUMLINE =
PERCUSSION =
WOODWIND =
MAIN_BAND_ROOM =
UNIFORM =
ORCHESTRA =
