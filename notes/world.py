main_map = {
    'Table': {
        'NAME': "Outer stage lunch table",
        'DESCRIPTION': "It's the lunch table nearest to both the band room and the outer stage. To the west of you is"
                       "the outer stage.",
        'PATHS': {
            'WEST': "Outer Stage"
        }
    },
    'Outer Stage': {
        'NAME': "Outer Stage",
        'DESCRIPTIONS': "The is the same as the stage inside the cafeteria. The only difference is that it's outside "
                        "where students or staff members do events near the quad area.. that are outside. To the north "
                        "of you is the back stage.",
        'PATHS': {
            'NORTH': "Back Stage"
        }
    },
    'Back Stage': {
        'NAME': "Back Stage",
        'DESCRIPTION': "This is in back of the stage. No one comes here except theatre kids, theatre teachers, and "
                       "stage management. It's always full of wood and forgotten outfits. To the north of you is the "
                       "actual stage.",
        'PATHS': {
            'NORTH': "Stage"
        }
    },
    'Stage': {
        'NAME': "Main Stage",
        'DESCRIPTION': "It's the main stage. This is where some band performances happen. Sometimes the saxes have"
                       "sectionals here after school, it can get loud here with them. The stage is somewhere where both"
                       "the band members and theatre kids can share and not fight over it... all the time.. To the"
                       "north-west and north-east are stair cases to get off the stage.",
        'PATHS': {
            'NORTH EAST': "Cafeteria",
            'NORTH WEST': "Cafeteria"
        }
    },
    'Cafeteria': {
        'NAME': "School's Cafeteria",
        'DESCRIPTION': "The school's cafeteria. When we're lucky, the band instructors have us practice in here with ac"
                       "on. It's very small but as long as it's not out in the field on a hot day, anything is better.."
                       "You can rest here for now until lunch break s over",
        'PATHS': {}
    }
}

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
