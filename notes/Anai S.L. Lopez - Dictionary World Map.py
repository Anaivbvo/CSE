main_map = {
    'TREE1': {
        'NAME': "Band_Tree",
        'DESCRIPTION': "This is the nearest tree to the band room. Nothing too special about it.",
        'AV_DIR': "WEST: Hang_Out_Tree, NORTH_EAST: Outside_Band_room",
        'PATHS': {
            'WEST': 'TREE2',
            'NORTH_EAST': 'OUTER_BAND'
        }
    },  # Outside
    'TREE2': {
        'NAME': "Hang_Out_Tree",
        'DESCRIPTION': "It's the usual tree we hang out at. It has the best shade range, not to big and definitely "
                       "not to small. ",
        'AV_DIR': "WEST: Lunch_Table, EAST: Band_Tree",
        'PATHS': {
            'WEST': "TABLE",
            'EAST': 'TREE2'
        }
    },
    'TABLE': {
        'NAME': "Lunch_Table",
        'DESCRIPTION': "This is the usual lunch table we hang out at. Enough for our circle to hang out at. Great "
                       "shade as well.",
        'AV_DIR': "WEST: Amp, EAST: Hang_Out_Tree.",
        'PATHS': {
            'WEST': 'OUTER_STAGE',
            'EAST': 'TREE'
        }
    },
    'OUTER_STAGE': {
        'NAME': "Amp",
        'DESCRIPTION': "The amp. It's stairs and wide stage is the best place to have fun and rest at.",
        'AV_DIR': "NORTH: Back_Stage, EAST: Lunch_Table.",
        'PATHS': {
            'NORTH': 'BACK_STAGE',
            'EAST': 'TABLE'
        }
    },
    'BACK_STAGE': {
        'NAME': "Back_Stage",
        'DESCRIPTION': "It's the back of the stage. There's really no need to be here. ",
        'AV_DIR': "NORTH_WEST: Stage, NORTH_EAST: Stage.",
        'PATHS': {
            'NORTH_WEST': 'STAGE',
            'NORTH_EAST': 'STAGE'
        }
    },  # Cafeteria
    'STAGE': {
        'NAME': "Stage",
        'DESCRIPTION': "The school's main stage. Band performances, mainly concert happen here! When the lights shine "
                       "on you, it's the best feeling! Oh, and theatre kids do their plays here to. ",
        'AV_DIR': "NORTH_WEST: Cafeteria, NORTH_EAST: Cafeteria.",
        'PATHS': {
            'NORTH_WEST': 'CAFETERIA',
            'NORTH_EAST': 'CAFETERIA'
        }
    },
    'CAFETERIA': {
        'NAME': "Cafeteria",
        'DESCRIPTION': "It's the school's cafeteria. Though the tables and chairs are put away, so we have sectionals "
                       "in here sometimes. Well it depends on who gets here first, the saxes or anyone else.",
        'AV_DIR': "NORTH_WEST: Water_Fountains, NORTH: Janitor_Storage_Room, SOUTH_EAST: Band_Hall, NORTH_EAST: "
                  "Band_Hall.",
        'PATHS': {
            'NORTH_WEST': 'WATER_FOUNTAIN',
            'NORTH': 'JANITOR_ROOM',
            'SOUTH_EAST': 'BAND_HALL',
            'NORTH_EAST': 'BAND_HALL',
        }
    },
    'JANITOR_ROOM': {
        'NAME': "Janitor_Storage_Room",
        'DESCRIPTION': "It's the janitor's storage room. Nothing special about it since it's always closed.. ",
        'AV_DIR': "NORTH: Food_Booths.",
        'PATHS': {
            'NORTH': 'FOOD_BOOTHS'
        }
    },
    'WATER_FOUNTAIN': {
        'NAME': "Water_Fountains",
        'DESCRIPTION': " This room has no actual walls but it does have around 5 water fountains! This is the best "
                       "place to get water at. Sure it's the farthest place from the field, but it's worth it for the"
                       " water.",
        'AV_DIR': "SOUTH: Cafeteria.",
        'PATHS': {
            'SOUTH': 'CAFETERIA'
        }
    },
    'FOOD_BOOTHS': {
        'NAME': "Food_Booths",
        'DESCRIPTION': " This is where you receive the food from the lunch ladies. They have posters of how to eat "
                       "healthy and nutritious. The posters definitely speak better words than the food itself.. ",
        'AV_DIR': "EAST: Cafeteria_Kitchen, SOUTH: Cafeteria.",
        'PATHS': {
            'EAST': 'KITCHEN',
            'SOUTH': 'CAFETERIA'
        }
    },
    'KITCHEN': {
        'NAME': "Cafeteria_Kitchen",
        'DESCRIPTION': "The cafeteria's kitchen. They never actually cook anything, but there is always a lot of "
                       "ingredients here.. ",
        'AV_DIR': "WEST: Food_Booths.",
        'PATHS': {
            'WEST': 'FOOD_BOOTHS'
        }
    },
    'BAND_ROOM': {
        'NAME': "Band_Room",
        'DESCRIPTION': "It's the band room! It's our home! Sure it may be your first year but that is alright! The "
                       "entrance is sometimes the best part! There is a fridge and a lost and found box.",
        'AV_DIR': "NORTH: Director_Office, SOUTH: Drum-Line_Lockers, WEST: Main_Band_Room",
        'PATHS': {
            'NORTH': 'OFFICE',
            'SOUTH': 'DRUM-LINE',
            'WEST': 'MAIN_BAND_ROOM'
        }
    },  # Band room
    'OFFICE': {
        'NAME': "Director_Office",
        'DESCRIPTION': "It's the director's office. There is music, trophies, awards, photos and... dvd cases..?",
        'AV_DIR': "NORTH: Orchestra_Room, SOUTH: Band_Room entrance.",
        'PATHS': {
            'NORTH': 'ORCHESTRA',
            'SOUTH': 'BAND_ROOM'
        }
    },
    'DRUM-LINE': {
        'NAME': "Drum-line_Lockers",
        'DESCRIPTION': "It's the drum line locker rooms! They are what really hold the band into their top level. Being"
                       " in their locker room is an honor! But unless you're a member or a god tier level junior/senior"
                       " player, you best leave now...",
        'AV_DIR': "NORTH: Band_Room, SOUTH_WEST: Percussion_Lockers",
        'PATHS': {
            'NORTH': 'BAND_ROOM'
        }
    },
    'PERCUSSION': {
        'NAME': "Percussion_Lockers",
        'DESCRIPTION': "This isn't a room necessarily but more of a section of the room. There are marimbas and drum "
                       "sets. Never stay here for too long though... The percussion members like their space neat and "
                       "unoccupied... ",
        'AV_DIR': "WEST: Wood-Wind_Lockers, NORTH_EAST: Drum-Line_Lockers, NORTH: Main_Band_Room",
        'PATHS': {
            'WEST': 'WOOD-WIND',
            'NORTH': 'MAIN_BAND_ROOM',
            'NORTH_EAST': 'DRUM-LINE'
        }
    },
    'WOOD-WIND': {
        'NAME': "Wood-Wind_Lockers",
        'DESCRIPTION': "It's the woodwind lockers! Most everyone hangs around here since there is rarely anyone that "
                       "takes their instrument from their lockers. Flutes and clarinets always take theirs home.. Saxes"
                       " though... They always go back and forth from here from lockers to stands.",
        'AV_DIR': "EAST: Percussion_Lockers, NORTH: Main_Band_room.",
        'PATHS': {
            'EAST': 'PERCUSSION',
            'NORTH': 'MAIN_BAND_ROOM'
        }
    },
    'MAIN_BAND_ROOM': {
        'NAME': "Main_Band_Room",
        'DESCRIPTION': "This is the main band room. This is where most classes and practice takes place. No matter if "
                       "you're a part of orchestra, choir, jazz, concert, etc, this is the main used room.",
        'AV_DIR': "SOUTH_WEST: Wood-Wind_Lockers, SOUTH: Percussion_Lockers, SOUTH_EAST: Drum-Line_Lockers, NORTH: "
                  "Uniform_Storage_Room, WEST: Band_Hall",
        'PATHS': {
            'SOUTH_WEST': 'WOOD-WIND',
            'SOUTH': 'PERCUSSION',
            'SOUTH_EAST': 'DRUM-LINE',
            'NORTH': 'UNIFORM',
            'WEST': 'BAND_HALL'
        }
    },
    'UNIFORM': {
        'NAME': "Uniform_Storage_Room",
        'DESCRIPTION': "This is where we keep the band uniforms as well as any extra snacks, water bottles, and other "
                       "stuff. A storage room of course.",
        'AV_DIR': "NORTH: Orchestra_Room, SOUTH: Main_Band_Room",
        'PATHS': {
            'NORTH': 'ORCHESTRA',
            'SOUTH': 'MAIN_BAND_ROOM'
        }
    },
    'ORCHESTRA': {
        'NAME': "Orchestra_Room",
        'DESCRIPTION': "The orchestra room isn't always used. Sometimes when we have study hall, half the class decides"
                       " to practice solo here. There's a piano and lockers here as well. This room is mainly used by "
                       "orchestra members when they practice as well as color guard members.",
        'AV_DIR': "NORTH_WEST: Brass_Lockers, NORTH_EAST: Color_Guard_Lockers, WEST: Band_Hall, SOUTH_WEST: "
                  "Uniform_Room, SOUTH_EAST: Director_Office, EAST: ",
        'PATHS': {
            'NORTH_WEST': 'BRASS',
            'NORTH_EAST': 'GUARD',
            'WEST': 'BAND_HALL',
            'SOUTH_WEST': 'UNIFORM',
            'SOUTH_EAST': 'OFFICE'
        }
    },
    'BRASS': {
        'NAME': "Brass_Lockers",
        'DESCRIPTION': "The brass lockers. You see the members always hanging around here having a good time talking or"
                       "practicing. The lockers are very neat compared to the woodwinds actually! This may be because "
                       "how organized the brass section leaders are!",
        'AV_DIR': "SOUTH: Orchestra_Room, EAST: Color_Guard_Lockers",
        'PATHS': {
            'SOUTH': 'ORCHESTRA',
            'EAST': 'GUARD'
        }
    },
    'GUARD': {
        'NAME': "Color_Guard_Lockers",
        'DESCRIPTION': "It's the color guard's locker room. This is much more of a room since the color guard change "
                       "into their outfits here. As well as have their props such as flags and rifles here. The color "
                       "guard are ones who don't like waiting, you best hurry and leave before they catch you in here!",
        'AV_DIR': "WEST: Brass_Lockers, SOUTH: Orchestra_Room",
        'PATHS': {
            'WEST': 'BRASS',
            'SOUTH': 'ORCHESTRA'
        }
    },
    'BAND_HALL': {
        'NAME': "Band_Hall",
        'DESCRIPTION': "This is thr band hall. Students have sectionals and solo practices here when ever the director "
                       "lets us. Well, sometimes we just play video games here in groups too.",
        'AV_DIR': "SOUTH_WEST: Cafeteria, NORTH_WEST: Cafeteria, SOUTH_EAST: Main_Band_room, "
                  "NORTH_EAST: Orchestra_Room, NORTH: Lounge_Hall",
        'PATHS': {
            'SOUTH_WEST': "CAFETERIA",
            'SOUTH_EAST': "MAIN_BAND_ROOM",
            'NORTH_WEST': "CAFETERIA",
            'NORTH_EAST': "ORCHESTRA",
            'NORTH': 'LOUNGE_HALL'
        }
    },  # Halls
    'LOUNGE_HALL': {
        'NAME': "Lounge_Hall",
        'DESCRIPTION': "Band members practice here too. But majority of the psace is occupied by old broken stands and "
                       "unused  carts.",
        'AV_DIR': "SOUTH: Band_Hall, NORTH: Storage_Room, EAST: Outer_Orchestra_Room, NORTH_EAST: Teacher_Lounge_Room",
        'PATHS': {
            'SOUTH': 'BAND_HALL',
            'NORTH': 'STORAGE',
            'EAST': 'OUTER_ORCHESTRA',
            'NORTH_EAST': 'TEACHER_LOUNGE'
        }
    },
    'STORAGE': {
        'NAME': "Storage_Room",
        'DESCRIPTION': "This room has tables and chairs. A lot of them seem to be broken. It's not very bright in here"
                       " for the lights are very dim..",
        'AV_DIR': "SOUTH: Lounge_Hall",
        'PATHS': {
            'SOUTH': 'LOUNGE_HALL'
        }
    },
    'TEACHER_LOUNGE': {
        'NAME': "Teacher_Lounge_Room",
        'DESCRIPTION': "It's the teacher's lounge room. A lot of teachers spent there time here during lunch. Though "
                       "why the lounge room is so far from other classes as well as near the band room, is a weird "
                       "placement..",
        'AV_DIR': "SOUTH_EAST: Lounge_Hall, EAST: Lounge_Table",
        'PATHS': {
            'SOUTH_EAST': 'LOUNGE_HALL',
            'EAST': 'LOUNGE_TABLE'
        }
    },
    'LOUNGE_TABLE': {
        'NAME': "Lounge_Table",
        'DESCRIPTION': "This is an area outside the teacher's lounge table. Sometimes students hang here during lunch. "
                       "Sometimes sectionals happen here too. Well.. it tends to be a battle between low brass and "
                       "saxes for this spot.",
        'AV_DIR': "WEST: Teacher_Lounge, SOUTH: Outside_Orchestra_Room",
        'PATHS': {
            'WEST': 'TEACHER_LOUNGE',
            'SOUTH': 'OUTER_ORCHESTRA'
        }
    },
    'OUTER_BAND': {
        'NAME': "Outside_Band_Room",
        'DESCRIPTION': "This is outside the band room. A lot of band member hang ut here during lunch and break.",
        'AV_DIR': "SOUTH_EAST: Band_Tree, NORTH: Outside_Orchestra_Room, WEST: Band_Room",
        'PATHS': {
            'SOUTH_EAST': 'TREE1',
            'NORTH': 'OUTER_ORCHESTRA',
            'WEST': 'BAND_ROOM'
        }
    },
    'OUTER_ORCHESTRA': {
        'NAME': "Outside_Orchestra_Room",
        'DESCRIPTION': "This is outside the orchestra room. Members don;t hang here as often except during lunch.",
        'AV_DIR': "SOUTH: Outside_Band_Room, WEST: Orchestra_Room, NORTH: Lounge_Table, NORTH_WEST: Lounge_Hall",
        'PATHS': {
            'SOUTH': 'OUTER_BAND',
            'WEST': 'ORCHESTRA',
            'NORTH': 'LOUNGE_TABLE',
            'NORTH_WEST': 'LOUNGE_HALL'
        }
    }
}

# Controller
playing = True
current_node = main_map['TREE1']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH_EAST', 'NORTH_WEST', 'SOUTH_EAST', 'SOUTH_WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print("-"*10)
    print(current_node['DESCRIPTION'])
    print("-" * 10)
    print(current_node['AV_DIR'])
    print("-" * 10)
    command = input(">_ ")
    if command.lower() in ['q', 'quit', 'exit', 'stop']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = main_map[room_name]
        except KeyError:
            print("I can't go that way.")
        except AttributeError:
            pass
        except ArithmeticError:
            pass
    else:
        print("Command not found")
