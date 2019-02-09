main_map = {
    'TREE': {
            'NAME': "Hang_Out_Tree",
            'DESCRIPTION': "It's the usual tree we hang out at. It has the best shade range, not to big and definetely "
                           "not to small. To the WEST of you is the Lunch_Table.",
            'PATHS': {
                'WEST': 'Lunch_Table'
            }
        },
    'TABLE': {
            'NAME': "Lunch_Table",
            'DESCRIPTION': "This is the usual lunch table we hang out at. Enough for our circle to hang out at. "
                           "Great shade as well. To the WEST of you is the Amp.",
            'PATHS': {
                'WEST': 'Amp'
            }

        },
    'OUTER_STAGE': {
            'NAME': "Amp",
            'DESCRIPTION': "The amp. It's stairs and wide stage is the best place to have fun and rest at. To the "
                           "NORTH of you is the entrance to the Back_Stage.",
            'PATHS': {
                'NORTH': 'Back_Stage'
            }

        },
    'CAFETERIA': {
        'BACK_STAGE': {
            'NAME': "Back_Stage",
            'DESCRIPTION': "It's the back of the stage. There's really no need to be here. To the NORTH_WEST and "
                           "NORTH_EAST are entrances to the actual Stage.",
            'PATHS': {
                'NORTH_WEST': 'Stage',
                'NORTH_EAST': 'Stage'
            }

        },
        'STAGE': {
            'NAME': "Stage",
            'DESCRIPTION': "The school's main stage. Band performances, mainly concert happen here! When the lights "
                           "shine on you, it's the best feeling! Oh, and theatre kids do their plays here to. To the "
                           "NORTH_WEST and NORTH_EAST is the stairs down to the floors of the Cafeteria.",
            'PATHS': {
                'NORTH_WEST': 'Cafeteria',
                'NORTH_EAST': 'Cafeteria'
            }

        },
        'CAFETERIA': {
            'NAME': "Cafeteria",
            'DESCRIPTION': "It's the school's cafeteria. Though the tables and chairs are put away, so we have "
                           "sectionals in here sometimes. Well it depends on who gets here first, the saxes or anyone"
                           "else. To the NORTH of you are multiple rooms. To the NORTH_WEST is the Water_Fountains. "
                           "Going NORTH leads you to the Janitor_Storage_Room. Going SOUTH_EAST leads ypu to the "
                           "Theatre_Hall. Going to the NORTH_EAST leads you to the Band_Hall.",
            'PATHS': {
                'NORTH_WEST': 'Water_Fountains',
                'NORTH': 'Janitor_Storage_Room',
                'SOUTH_EAST': 'Band_Hall',
                'NORTH_EAST': 'Theatre_Hall',
            }

        },
        'JANITOR_ROOM': {
            'NAME': "Janitor_Storage_Room",
            'DESCRIPTION': "It's the janitor's storage room. Nothing special about it since it's always closed.. To "
                           "the NORTH is the Food_Booths.",
            'PATHS': {
                'NORTH': 'Food_Booths'
            }

        },
        'WATER_FOUNTAIN': {
            'NAME': "Water_Fountains",
            'DESCRIPTION': " This room has no actual walls but it does have around 5 water fountains! This is the best "
                           "place to get water at. Sure it's the farthest place from the field, but it's worth it for "
                           "the water. Go SOUTH to enter back into the Cafeteria.",
            'PATHS': {
                'SOUTH': 'Cafeteria'
            }

        },
        'FOOD_BOOTHS': {
            'NAME': "Food_Booths",
            'DESCRIPTION': " This is where you receive the food from the lunch ladies. They have posters of how to eat "
                           "healthy and nutritious. The posters definitely speak better words than the food itself.. "
                           "Going EAST will lead you to the Cafeteria_Kitchen. Going SOUTH leads you back out into "
                           "the Cafeteria.",
            'PATHS': {
                'EAST': 'Cafeteria_Kitchen',
                'SOUTH': 'Cafeteria'
            }

        },
        'KITCHEN': {
            'NAME': "Cafeteria_Kitchen",
            'DESCRIPTION': "The cafeteria's kitchen. They never actually cook anything, but there is always a lot of"
                           " ingredients here.. Going WEST leads you back to the Food_Booths.",
            'PATHS': {
                'WEST': 'Food_Booths'
            }
        }
    },
    'MUSIC_BUILDING': {
        'ENTRANCE': {
            'NAME': "Band_Room",
            'DESCRIPTION': "It's the band room! It's our home! Sure it may be your first year but that is alright! The "
                           "entrance is sometimes the best part! There is a fridge and a lost and found box. Both are "
                           "good! Going to NORTH is the director's office. Going SOUTH is the drum line's lockers.",
            'PATHS': {
                'NORTH': 'Director_Office',
                'SOUTH': 'Drum-line_Lockers'
            }

        },
        'OFFICE': {
            'NAME': "Director_Office",
            'DESCRIPTION': "It's the director's office. There is music, trophies, awards, photos and... movie dvd "
                           "cases? The director is not here right now, unsure why. Go NORTH to enter the Orchestra_Room"
                           "or go SOUTH to go back into the Band_Room entrance.",
            'PATHS': {
                'NORTH': 'Orchestra_Room',
                'SOUTH': 'Band_Room'
            }

        },
        'DRUM-LINE': {
            'NAME': "Drum-line_Lockers",
            'DESCRIPTION': "It's the drum line locker rooms! They are what really hold the band into their top level."
                           "Being in their locker room is an honor! But unless you're a member or a god tier level "
                           "junior/senior player, you best leave now... go NORTH_WEST to enter the Main_Band_Room or "
                           "go NORTH to go back to the Band_Room entrance.",
            'PATHS': {
                'NORTH': 'Band_Room',
                'NORTH_WEST': 'Main_Band_Room'
            }

        },
        'PERCUSSION': {
            'NAME': "Percussion_Lockers",
            'DESCRIPTION': "This isn't a room necessarily but more of a section of the room. There are murambas and drm"
                           "sets. Never stay here for too long though... The percussion members like their space neat "
                           "and unoccupied... Go WEST for the Wood-Wind_Lockers and NORTH_EAST to enter into the "
                           "Drum-Line_Lockers. Go NORTH to enter the Main_Band_Room.",
            'PATHS': {
                'WEST': 'Wood-Wind_Locker',
                'NORTH': 'Main_Band_Room',
                'NORTH_EAST': 'Drum-Line_Lockers'
            }

        },
        'WOOD-WIND': {
            'NAME': "Wood-Wind_Lockers",
            'DESCRIPTION': "It's the woodwind lockers! Most everyone hangs around here since there is rarely anyone "
                           "that takes their instrument from their lockers. Flutes and clarinets always take theirs "
                           "home.. Saxes though... They always go back and forth from here. Go ",
            'PATHS': {}

        },
        'BAND_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'STORAGE_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'ORCHESTRA': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'BRASS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'COLOR-GUARD': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        }
    },
    'HALLS': {
        'BAND_HALL': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'LOUNGE_HALL': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'STORAGE_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'TEACHER_LOUNGE': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'LOUNGE_TABLE': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        }
    }
}

# Controller
playing = True
current_node = main_map['TREE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper in directions:
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

