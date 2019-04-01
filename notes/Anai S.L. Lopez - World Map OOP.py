import extra2


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


class Player(object):
    def __init__(self, starting_location):
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


TREE1 = Room("Band_Tree", "This is the nearest tree to the band room. Nothing too special about it.", "west: "
             "Hang_Out_Tree, north_east: Outside_Band_room", "This is the nearest tree to the band room. A lot of "
             "upperclassmen like to hang around here before school starts. You can often find junior to senior "
             "upperclassmen here.")
TREE2 = Room("Hangout_Tree", "It's the usual tree we hang out at. It has the best shade range, not too big and "
             "definitely not to small. ", "WEST: Lunch_Table, EAST: Band_Tree", "You'de expect there to be a lot of "
             "members hanging here.. Though rarely anyone tends to show up here. That's why it's our hang out tree. ")
TABLE = Room("Lunch_Table", "This is the usual lunch table we hang out at. Enough for our circle to hang out at. "
             "Great shade as well.", "WEST: Amp, EAST: Hang_Out_Tree.", "A small lunch table next to the hangout tree."
             " It's a nice spot for lunch, near the band room as well as the cafeteria.")
OUTER_STAGE = Room("Amp", "The amp. It's stairs and wide stage is the best place to have fun and rest at.", "NORTH: "
                   "Back_Stage, EAST: Lunch_Table.", "Jazz tends to perform for school afternoon events here. Sometimes"
                   " marching band gets to perform songs here as well. We have our visual square practices here. best "
                   "hope no teachers come walking around.. The visuals are awkward to do around others.")
BACK_STAGE = Room("Back_Stage", "It's the back of the stage. There's really no need to be here. ", "NORTH_WEST: "
                  "Stage, NORTH_EAST: Stage.", "Occasionally you can find theatre kids hanging around here.. Something"
                  " had happened between band and theatre kids 2 years ago. Though uperclassmen won't mention what this"
                  " event was about, it seems to have seperated these two groups into almost purely enemies.. You'd "
                  "best hurry out of here..")
STAGE = Room("Stage", "The school's main stage. Band performances, mainly concert happen here! When the lights shine "
             "on you, it's the best feeling! Oh, and theatre kids do their plays here to. ", "NORTH_WEST: Cafeteria, "
             "NORTH_EAST: Cafeteria.", "Saxes  tends to have sectionals here.. They tend to be the only ones close to "
             "theatre kids compared to the rest of the band sections, that's why they get to have sectionals here "
             "peacfully while theatre kids rehaearse and work on the stage.")
CAFETERIA = Room("Cafeteria", "It's the school's cafeteria. The tables and chairs are put away most times.", "TH_WEST:"
                 " Water_Fountains, NORTH: Janitor_Storage_Room, SOUTH_EAST: Band_Hall, NORTH_EAST: Band_Hall.", "A lot"
                 " of sections tend to have practice here. It can get awkward with theatre kids appearing on stage. "
                 "Only groups to show up here are horns and saxes. Tends to be fights on who gets to practice here.")
JANITOR_ROOM = Room("Janitor's_Room", "It's the janitor's storage room. Nothing special about it since it's always "
                                      "closed.. ", "NORTH: Food_Booths.")
WATER_FOUNTAIN = Room("Water_Fountains", " This room has no actual walls but it does have around 5 water fountains! "
                                         "This is the best place to get water at. Sure it's the farthest place from "
                                         "the field, but it's worth it for the water.", "SOUTH: Cafeteria.")
FOOD_BOOTHS = Room("Food_Booths", " This is where you receive the food from the lunch ladies. They have posters of how "
                                  "to eat healthy and nutritious. The posters definitely speak better words than the "
                                  "food itself.. ", "EAST: Cafeteria_Kitchen, SOUTH: Cafeteria.")
KITCHEN = Room("Cafeteria_Kitchen", "The cafeteria's kitchen. They never actually cook anything, but there is always "
                                    "a lot of ingredients here.. ", "WEST: Food_Booths.")
BAND_ROOM = Room("Band_Room_Entrance", "It's the band room! It's our home! Sure it may be your first year but that is "
                                       "alright! The entrance is sometimes the best part! There is a fridge and a lost"
                                       " and found box.", "NORTH: Director_Office, SOUTH: Drum-Line_Lockers, WEST: "
                                                          "Main_Band_Room")
OFFICE = Room("Director's_Office", "It's the director's office. There is music, trophies, awards, photos and... "
                                   "dvd cases..?", "NORTH: Orchestra_Room, SOUTH: Band_Room entrance.")
DRUMLINE = Room("Drumline_Lockers", "It's the drum line locker rooms! They are what really hold the band into their "
                                    "top level. Being in their locker room is an honor! But unless you're a member or "
                                    "a god tier level junior/senior player, you best leave now...", "NORTH: Band_Room,"
                                    " SOUTH_WEST: Percussion_Lockers")
PERCUSSION = Room("Percussion_Lockers", "This isn't a room necessarily but more of a section of the room. There are "
                                        "marimbas and drum sets. Never stay here for too long though... The percussion "
                                        "members like their space neat and unoccupied... ", "WEST: Wood-Wind_Lockers, "
                                        "NORTH_EAST: Drum-Line_Lockers, NORTH: Main_Band_Room")
WOODWIND = Room("Woodwind_Lockers", "It's the woodwind lockers! Most everyone hangs around here since there is rarely"
                                    " anyone that takes their instrument from their lockers. Flutes and clarinets "
                                    "always take theirs home.. Saxes though... They always go back and forth from here"
                                    " from lockers to stands.", "EAST: Percussion_Lockers, NORTH: Main_Band_room.")
MAIN_BAND_ROOM = Room("Main_Band_Room", "This is the main band room. This is where most classes and practice takes "
                                        "place. No matter if you're a part of orchestra, choir, jazz, concert, etc, "
                                        "this is the main used room.", "SOUTH_WEST: Wood-Wind_Lockers, SOUTH: "
                                        "Percussion_Lockers, SOUTH_EAST: Drum-Line_Lockers, NORTH: "
                                                                       "Uniform_Storage_Room, WEST: Band_Hall")
UNIFORM = Room("Uniform_Room", "This is where we keep the band uniforms as well as any extra snacks, water bottles, "
               "and other stuff. A storage room of course.", "NORTH: Orchestra_Room, SOUTH: Main_Band_Room")
ORCHESTRA = Room("Orchestra_Room", "The orchestra room isn't always used. Sometimes when we have study hall, half the "
                 "class decides  to practice solo here. There's a piano and lockers here as well. This room is mainly "
                 "used by orchestra members when they practice as well as color guard members.", "NORTH_WEST: "
                 "Brass_Lockers, NORTH_EAST: Color_Guard_Lockers, WEST: Band_Hall, SOUTH_WEST: Uniform_Room, "
                 "SOUTH_EAST: Director_Office, EAST: Outer_Orchestra")
BRASS = Room("Brass_Lockers", "The brass lockers. You see the members always hanging around here having a good time "
             "talking or practicing. The lockers are very neat compared to the woodwinds actually! This may be because "
             "how organized the brass section leaders are!", "SOUTH: Orchestra_Room, EAST: Color_Guard_Lockers")
GUARD = Room("Color_Guard_Lockers", "It's the color guard's locker room. The color guard change into their outfits "
             "here. As well as have their props such as flags and rifles here. The guard don't like waiting, you best "
             "hurry and leave before they catch you in here!", "WEST: Brass_Lockers, SOUTH: Orchestra_Room")
BAND_HALL = Room("Band_Hall", "This is thr band hall. Students have sectionals and solo practices here when ever the "
                 "director lets us. Well, sometimes we just play video games here in groups too.", "SOUTH_WEST: "
                 "Cafeteria, NORTH_WEST: Cafeteria, SOUTH_EAST: Main_Band_room, NORTH_EAST: Orchestra_Room, "
                 "NORTH: Lounge_Hall")
LOUNGE_HALL = Room("Lounge_Hall", "Band members practice here too. But majority of the psace is occupied by old broken"
                   " stands and unused carts.", "SOUTH: Band_Hall, NORTH: Storage_Room, EAST: Outer_Orchestra_Room, "
                                                "NORTH_EAST: Teacher_Lounge_Room")
STORAGE = Room("Storage_Room", "This room has tables and chairs. A lot of them seem to be broken. It's not very bright "
               "in here for the lights are very dim..", "SOUTH: Lounge_Hall")
TEACHER_LOUNGE = Room("Teacher's_Lounge", "It's the teacher's lounge room. A lot of teachers spent there time here "
                      "during lunch. Though why the lounge room is so far from other classes as well as near the band "
                      "room, is a weird placement..", "SOUTH_EAST: Lounge_Hall, EAST: Lounge_Table")
LOUNGE_TABLE = Room("Lounge_Table", "This is an area outside the teacher's lounge table. Sometimes students hang here "
                    "during lunch. Sometimes sectionals happen here too. Well.. it tends to be a battle between low "
                    "brass and saxes for this spot.", "WEST: Teacher_Lounge, SOUTH: Outside_Orchestra_Room")
OUTER_BAND = Room("Outer_Band", "This is outside the band room. A lot of band member hang ut here during lunch and "
                  "Break.", "SOUTH_EAST: Band_Tree, NORTH: Outside_Orchestra_Room, WEST: Band_Room")
OUTER_ORCHESTRA = Room("Outer_Orchestra", "This is outside the orchestra room. Members don;t hang here as often except "
                       "during lunch.", "SOUTH: Outside_Band_Room, WEST: Orchestra_Room, NORTH: Lounge_Table, "
                                        "NORTH_WEST: Lounge_Hall")

# --

TREE1.north_east = OUTER_BAND
TREE1.west = TREE2
TREE2.east = TREE1
TREE2.west = OUTER_STAGE
OUTER_STAGE.east = TREE2
OUTER_STAGE.north = BACK_STAGE
BACK_STAGE.south = OUTER_STAGE
BACK_STAGE.north = STAGE
STAGE.south = BACK_STAGE
STAGE.north_east = CAFETERIA
STAGE.north_west = CAFETERIA
CAFETERIA.south_east = STAGE
CAFETERIA.south_west = STAGE
CAFETERIA.north_west = WATER_FOUNTAIN
CAFETERIA.north = JANITOR_ROOM
CAFETERIA.south_east = BAND_HALL
CAFETERIA.north_east = LOUNGE_HALL
JANITOR_ROOM.north = FOOD_BOOTHS
JANITOR_ROOM.south = CAFETERIA
WATER_FOUNTAIN.south = CAFETERIA
FOOD_BOOTHS.south = CAFETERIA
FOOD_BOOTHS.east = KITCHEN
KITCHEN.west = FOOD_BOOTHS
BAND_ROOM.north = OFFICE
BAND_ROOM.south = DRUMLINE
BAND_ROOM.west = MAIN_BAND_ROOM
OFFICE.north = ORCHESTRA
OFFICE.south = BAND_ROOM
DRUMLINE.south_west = PERCUSSION
DRUMLINE.north = BAND_ROOM
PERCUSSION.west = WOODWIND
PERCUSSION.north = MAIN_BAND_ROOM
PERCUSSION.north_east = DRUMLINE
WOODWIND.east = PERCUSSION
WOODWIND.north = MAIN_BAND_ROOM
MAIN_BAND_ROOM.south_west = WOODWIND
MAIN_BAND_ROOM.south_east = DRUMLINE
MAIN_BAND_ROOM.south = PERCUSSION
MAIN_BAND_ROOM.north = UNIFORM
MAIN_BAND_ROOM.west = BAND_HALL
UNIFORM.north = ORCHESTRA
UNIFORM.south = MAIN_BAND_ROOM
ORCHESTRA.north_east = GUARD
ORCHESTRA.north_west = BRASS
ORCHESTRA.south_east = OFFICE
ORCHESTRA.south_west = UNIFORM
ORCHESTRA.west = BAND_HALL
ORCHESTRA.east = OUTER_ORCHESTRA
BRASS.south = ORCHESTRA
BRASS.east = GUARD
GUARD.west = BRASS
GUARD.south = ORCHESTRA
BAND_HALL.south_west = CAFETERIA
BAND_HALL.south_east = MAIN_BAND_ROOM
BAND_HALL.north_east = ORCHESTRA
BAND_HALL.north = LOUNGE_HALL
LOUNGE_HALL.north = STORAGE
LOUNGE_HALL.south = BAND_HALL
LOUNGE_TABLE.north_east = TEACHER_LOUNGE
LOUNGE_HALL.east = OUTER_ORCHESTRA
LOUNGE_HALL.west = CAFETERIA
STORAGE.south = LOUNGE_HALL
TEACHER_LOUNGE.south_east = LOUNGE_HALL
TEACHER_LOUNGE.east = LOUNGE_TABLE
LOUNGE_TABLE.west = TEACHER_LOUNGE
LOUNGE_TABLE.south = OUTER_ORCHESTRA
OUTER_BAND.north = OUTER_ORCHESTRA
OUTER_BAND.south_east = TREE1
OUTER_BAND.west = BAND_ROOM
OUTER_ORCHESTRA.north = LOUNGE_TABLE
OUTER_ORCHESTRA.south = OUTER_BAND
OUTER_ORCHESTRA.west = ORCHESTRA
OUTER_ORCHESTRA.north_west = LOUNGE_HALL

player = Player(TREE1)

playing = True
directions = ['north', 'south', 'east', 'west', 'north_east', 'north_west', 'south_east', 'south_west']

while playing:
    print("-", player.current_location.name)
    print("-", player.current_location.description)
    print("-", player.current_location.av_dir)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    if command.lower() in ['i', 'inventory']:
        print(player.inventory)
    if command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command.lower())
            player.move(room_name)
        except KeyError:
            print("Error: Can't go that way")
