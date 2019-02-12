main_map = {
    'TREE': {
            'NAME': "Hang_Out_Tree",
            'DESCRIPTION': "It's the usual tree we hang out at. It has the best shade range, not to big and definitely "
                           "not to small. To the WEST of you is the Lunch_Table.",
            'PATHS': {
                'WEST': "TABLE"
            }
        },
    'TABLE': {
            'NAME': "Lunch_Table",
            'DESCRIPTION': "This is the usual lunch table we hang out at. Enough for our circle to hang out at. "
                           "Great shade as well. To the WEST of you is the Amp.",
            'PATHS': {
                'WEST': 'Amp'
            }

        }
}

# Controller
playing = True
current_node = main_map['TREE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH_EAST', 'NORTH_WEST', 'SOUTH_EAST', 'SOUTH_WEST']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        room_name = current_node['PATHS'][command.upper()]
        current_node = main_map[room_name]
    elif KeyError:
        print("I can't go that way.")
    elif AttributeError:
            pass
    elif ArithmeticError:
            pass
    else:
        print("Command not found")
