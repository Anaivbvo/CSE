['north', 'south', 'east', 'west', 'north_east', 'north_west', 'south_east', 'south_west']
short_directions =

if command.lower() in short_directions:
    pos = short_directions.index(command.lower())
    command = directions[pos]

