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
