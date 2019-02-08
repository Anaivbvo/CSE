<<<<<<< HEAD
main_map = {
    'OUTSIDE': {
        'OUTER_STAGE_TABLE': {
            'NAME': "Hang Out Table",
            'DESCRIPTION': "This is the table we tend to hang ot during lunch. It's next to the cafeteria and lunch"
                           "room. good shade as well as shine. It's the perfect place to hang out after practice. To "
                           "the WEST is the OUTER_STAGE.",
            'PATHS': {
                'WEST': 'OUTER_STAGE'
            }
        },
        'OUTER_STAGE': {
            'NAME': "AMP Stage",
            'DESCRIPTION': "This is the AMP Stage. School peformances and events happen here. It's really nice to "
                           "hang out at when it's raining. Though the shade does not provide a lot of coolness. To the "
                           "NORTH of you is the entrance to the BACK_STAGE.",
            'PATHS': {
                'NORTH': 'BACK_STAGE'
            }
        }
    },
    'CAFETERIA_BUILDING': {
        'BACK_STAGE': {
            'NAME': "Back Stage",
            'DESCRIPTION': "This is in back of the stage. No one comes here except theatre kids, theatre teachers, and "
                           "stage management. It's always full of wood and forgotten outfits. To the NORTH of you is "
                           "the actual STAGE",
            'PATHS': {
                'NORTH': 'STAGE'
            }
        },
        'STAGE': {
            'NAME': "The School's Stage",
            'DESCRIPTION': "It's the main stage. This is where some band peformances happen. Sometimes the saxes have"
                           "sectionals here after school, it can get loud here with them. The stage is somewhere where "
                           "both the band members and theatre kids can share and not fight over it... all the time.. "
                           "To the NORTH_WEST and NORTH_EAST are stair cases to get off the stage and enter the "
                           "CAFETERIA grounds.",
            'PATHS': {
                'NORTH_WEST': 'CAFETERIA',
                'NORTH_EAST': 'CAFETERIA'
            }
        },
        'CAFETERIA': {
            'NAME': "The School's Cafeteria",
            'DESCRIPTION': "It's the school's cafeteria. ",
            'PATHS': {}
        },
        'JANITOR_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'CART_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'WATER_FOUNTAIN': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'LUNCH_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'KITCHEN': {}
    },
    'HALL': {
        'BAND_HALL': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'STAGE_HALL': {
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
        }
    },
    'BAND_ROOM': {
        'ENTRANCE': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'DRUM_LINE_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'PERCUSSION_PIT_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'WOOD_WIND_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'MAIN_BAND_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'UNIFORM_ROOM': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
        'DIRECTOR_OFFICE': {
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
        'COLOR_GUARD_LOCKERS': {
            'NAME': "",
            'DESCRIPTION': "",
            'PATHS': {}
        },
    }
}
=======
main_map = {}

print("-"*12)
print(" ")
print("Try this out: Basic tips: ")
print("To quit or end the game just type: q, quit, or exit.")
print(" ")
print("-"*12)
print(" ")

# Controller
playing = True
current_node = main_map['Table']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH_EAST', 'NORTH_WEST']

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
>>>>>>> 081cc91c84a764e6bce301574fc7185d9acdce20
