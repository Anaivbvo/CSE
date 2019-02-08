main_map = {
    'OUTSIDE': {
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
            'DESCRIPTION': "The school's main stage. Band peformances, mainly concert happen here! When the lights "
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
                           "Going NORTH leads you to the Janitor_Storage_Room.",
            'PATHS': {
                'NORTH_WEST': 'Water_Fountains',
                'NORTH': 'Janitor_Storage_Room'
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
                           "healthy and nutritious. The posters definetley speak better words than the food itself.. "
                           "Going EAST will lead you to the Cafeteria's_Kitchen. Going South leads you back out into "
                           "the Cafeteria.",
            'PATHS': {}

        },
        'KITCHEN': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        }
    },
    'MUSIC_BUILDING': {
        'ENTRANCE': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'OFFICE': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'DRUM-LINE_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'PERCUSSION_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'WOOD-WIND_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'MAIN_BAND_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'UNIFORM_STORAGE_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'ORCHESTRA_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'BRASS_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}

        },
        'COLOR-GUARD_LOCKERS': {
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
