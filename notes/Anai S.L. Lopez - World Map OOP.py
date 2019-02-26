class Room(object):
    def __init__(self, name, description=None, av_dir=None, north=None, north_east=None, north_west=None,
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


TREE1 = Room("Band_Tree", "This is the nearest tree to the band room. Nothing too special about it.", "WEST: "
             "Hang_Out_Tree, NORTH_EAST: Outside_Band_room")
TREE2 = Room("Hangout_Tree", "It's the usual tree we hang out at. It has the best shade range, not to big and "
                             "definitely not to small. ", "WEST: Lunch_Table, EAST: Band_Tree")
TABLE = Room("Lunch_Table", "This is the usual lunch table we hang out at. Enough for our circle to hang out at. "
                            "Great shade as well.", "WEST: Amp, EAST: Hang_Out_Tree.")
OUTER_STAGE = Room("Amp", "The amp. It's stairs and wide stage is the best place to have fun and rest at.", "NORTH: "
                          "Back_Stage, EAST: Lunch_Table.", )
BACK_STAGE = Room("Back_Stage", "It's the back of the stage. There's really no need to be here. ", "NORTH_WEST: "
                                "Stage, NORTH_EAST: Stage.")
STAGE = Room("Stage", "The school's main stage. Band performances, mainly concert happen here! When the lights shine "
                      "on you, it's the best feeling! Oh, and theatre kids do their plays here to. ", "NORTH_WEST: "
                      "Cafeteria, NORTH_EAST: Cafeteria.")
CAFETERIA = Room("Cafeteria", "It's the school's cafeteria. Though the tables and chairs are put away, so we have "
                 "sectionals in here sometimes. Well it depends on who gets here first, the saxes or anyone else.",
                 "NORTH_WEST: Water_Fountains, NORTH: Janitor_Storage_Room, SOUTH_EAST: Band_Hall, NORTH_EAST: "
                 "Band_Hall.")
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
MAIN_BAND_ROOM = Room("Main_Band_Room")
UNIFORM = Room("Uniform_Room")
ORCHESTRA = Room("Orchestra_Room")
BRASS = Room("Brass_Lockers")
GUARD = Room("Color_Guard_Lockers")
BAND_HALL = Room("Band_Hall")
LOUNGE_HALL = Room("Lounge_Hall")
STORAGE = Room("Storage_Room")
TEACHER_LOUNGE = Room("Teacher's_Lounge")
LOUNGE_TABLE = Room("Lounge_Table")
OUTER_BAND = Room("Outer_Band")
OUTER_ORCHESTRA = Room("Outer_Orchestra")

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

print(TREE1.name)
print("-"*5)
print(TREE1.description)
print("-"*5)
print(TREE1.av_dir)
