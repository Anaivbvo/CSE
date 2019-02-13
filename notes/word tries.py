main_map = {
    'TREE': {
        'NAME': "Hang_Out_Tree",
        'DESCRIPTION': "It's the usual tree we hang out at. It has the best shade range, not to big and definitely "
                       "not to small. ",
        'AV_DIR': "To the WEST of you is the Lunch_Table.",
        'PATHS': {
            'WEST': "TABLE"
        }
    },  # Outside
    'TABLE': {
        'NAME': "Lunch_Table",
        'DESCRIPTION': "This is the usual lunch table we hang out at. Enough for our circle to hang out at. Great "
                       "shade as well.",
        'AV_DIR': "To the WEST of you is the Amp. Going EAST leads you back to the Hang_Out_Tree.",
        'PATHS': {
            'WEST': 'OUTER_STAGE',
            'EAST': 'TREE'
        }
    },
    'OUTER_STAGE': {
        'NAME': "Amp",
        'DESCRIPTION': "The amp. It's stairs and wide stage is the best place to have fun and rest at.",
        'AV_DIR': " Go NORTH of you is the entrance to the Back_Stage. Going EAST leads you back to the Lunch_Table.",
        'PATHS': {
            'NORTH': 'BACK_STAGE',
            'EAST': 'TABLE'
        }
    },
    'BACK_STAGE': {
        'NAME': "Back_Stage",
        'DESCRIPTION': "It's the back of the stage. There's really no need to be here. ",
        'AV_DIR': "To the NORTH_WEST and NORTH_EAST are entrances to the actual Stage.",
        'PATHS': {
            'NORTH_WEST': 'STAGE',
            'NORTH_EAST': 'STAGE'
        }
    },  # Cafeteria
    'STAGE': {
        'NAME': "Stage",
        'DESCRIPTION': "The school's main stage. Band performances, mainly concert happen here! When the lights shine "
                       "on you, it's the best feeling! Oh, and theatre kids do their plays here to. ",
        'AV_DIR': "To the NORTH_WEST and NORTH_EAST is the stairs down to the floors of the Cafeteria.",
        'PATHS': {
            'NORTH_WEST': 'CAFETERIA',
            'NORTH_EAST': 'CAFETERIA'
        }
    },
    'CAFETERIA': {
        'NAME': "Cafeteria",
        'DESCRIPTION': "It's the school's cafeteria. Though the tables and chairs are put away, so we have sectionals "
                       "in here sometimes. Well it depends on who gets here first, the saxes or anyone else.",
        'AV_DIR': "To the NORTH of you are multiple rooms. To the NORTH_WEST is the Water_Fountains. Going NORTH leads "
                  "you to the Janitor_Storage_Room. Going SOUTH_EAST leads ypu to the Theatre_Hall. Going to the "
                  "NORTH_EAST leads you to the Band_Hall.",
        'PATHS': {
            'NORTH_WEST': 'WATER_FOUNTAIN',
            'NORTH': 'JANITOR_ROOM',
            'SOUTH_WE'
            'ST': 'BAND_HALL',
            'NORTH_EAST': 'THEATRE_HALL',
        }
    },
    'JANITOR_ROOM': {
        'NAME': "Janitor_Storage_Room",
        'DESCRIPTION': "It's the janitor's storage room. Nothing special about it since it's always closed.. ",
        'AV_DIR': "To the NORTH is the Food_Booths.",
        'PATHS': {
            'NORTH': 'FOOD_BOOTHS'
        }
    },
    'WATER_FOUNTAIN': {
        'NAME': "Water_Fountains",
        'DESCRIPTION': " This room has no actual walls but it does have around 5 water fountains! This is the best "
                       "place to get water at. Sure it's the farthest place from the field, but it's worth it for the"
                       " water.",
        'AV_DIR': " Go SOUTH to enter back into the Cafeteria.",
        'PATHS': {
            'SOUTH': 'CAFETERIA'
        }
    },
    'FOOD_BOOTHS': {
        'NAME': "Food_Booths",
        'DESCRIPTION': " This is where you receive the food from the lunch ladies. They have posters of how to eat "
                       "healthy and nutritious. The posters definitely speak better words than the food itself.. ",
        'AV_DIR': "Going EAST will lead you to the Cafeteria_Kitchen. Going SOUTH leads you back out into the "
                  "Cafeteria.",
        'PATHS': {
            'EAST': 'KITCHEN',
            'SOUTH': 'CAFETERIA'
        }
    },
    'KITCHEN': {
        'NAME': "Cafeteria_Kitchen",
        'DESCRIPTION': "The cafeteria's kitchen. They never actually cook anything, but there is always a lot of "
                       "ingredients here.. ",
        'AV_DIR': "Going WEST leads you back to the Food_Booths.",
        'PATHS': {
            'WEST': 'FOOD_BOOTHS'
        }
    },
    'BAND_ROOM': {
        'NAME': "Band_Room",
        'DESCRIPTION': "It's the band room! It's our home! Sure it may be your first year but that is alright! The "
                       "entrance is sometimes the best part! There is a fridge and a lost and found box.",
        'AV_DIR': "Going to NORTH is the director's office. Going SOUTH is the drum line's lockers.",
        'PATHS': {
            'NORTH': 'OFFICE',
            'SOUTH': 'DRUM-LINE'
        }
    },  # Band room
    'OFFICE': {
        'NAME': "Director_Office",
        'DESCRIPTION': "It's the director's office. There is music, trophies, awards, photos and... dvd cases..?",
        'AV_DIR': "Go NORTH to enter the Orchestra_Room or go SOUTH to go back into the Band_Room entrance.",
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
        'AV_DIR': "go NORTH_WEST to enter the Main_Band_Room or go NORTH to go back to the Band_Room entrance.",
        'PATHS': {
            'NORTH': 'BAND_ROOM',
            'NORTH_WEST': 'MAIN_BAND_ROOM'
        }
    },
    'PERCUSSION': {
        'NAME': "Percussion_Lockers",
        'DESCRIPTION': "This isn't a room necessarily but more of a section of the room. There are murambas and drum "
                       "sets. Never stay here for too long though... The percussion members like their space neat and "
                       "unoccupied... ",
        'AV_DIR': "Go WEST for the Wood-Wind_Lockers and NORTH_EAST to enter into the Drum-Line_Lockers. Go NORTH to "
                  "enter the Main_Band_Room.",
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
        'AV_DIR': "Go EAST to visit the Percussion_Lockers. Go NORTH for the Main_Band_room.",
        'PATHS': {
            'EAST': 'PERCUSSION',
            'NORTH': 'MAIN_BAND_ROOM'
        }
    },
    'MAIN_BAND_ROOM': {
        'NAME': "Main_Band_Room",
        'DESCRIPTION': "This is the main band room. This is where most classes and practice takes place. No matter if "
                       "you're a part of orchestra, choir, jazz, concert, etc, this is the main used room.",
        'AV_DIR': "Go SOUTH_WEST for the Wood-Wind_Lockers and SOUTH for the Percussion_Lockers. Going SOUTH_EAST will "
                  "lead you to the Drum-Line_Lockers. Go NORTH to enter the Uniform_Storage_Room.",
        'PATHS': {
            'SOUTH_WEST': 'WOOD-WIND',
            'SOUTH': 'PERCUSSION',
            'SOUTH_EAST': 'DRUM-LINE',
            'NORTH': 'STORAGE'
        }
    },
    'STORAGE': {
        'NAME': "Uniform_Storage_Room",
        'DESCRIPTION': "This is where we keep the band uniforms as well as any extra snacks, water bottles, and other "
                       "stuff. A storage room of course.",
        'AV_DIR': "",
        'PATHS': {}
    },
    'ORCHESTRA': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },
    'BRASS': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },
    'COLOR-GUARD': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },
    'BAND_HALL': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },  # Halls
    'LOUNGE_HALL': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },
    'STORAGE_ROOM': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },
    'TEACHER_LOUNGE': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    },
    'LOUNGE_TABLE': {
        'NAME': "",
        'DESCRIPTION': "",
        'AV_DIR': "",
        'PATHS': {}
    }
}

# Controller
playing = True
current_node = main_map['TREE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH_EAST', 'NORTH_WEST', 'SOUTH_EAST', 'SOUTH_WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print("-"*10)
    print(current_node['DESCRIPTION'])
    print("-" * 10)
    print(current_node['AV_DIR'])
    print("-" * 10)
    command = input(">_ ")
    if command.lower() in ['q', 'quit', 'exit']:
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
