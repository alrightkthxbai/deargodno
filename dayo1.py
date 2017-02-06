NORTH = 'North'
EAST = 'East'
WEST = 'West'
SOUTH = 'South'

def change_degree(degree, direction):
    """
    WIth the degree ya got find the new one (NORTH, EAST, WEST or SOUTH)
    and a direction (either 'L' or 'R')
    """
    if degree == NORTH:
        if direction == 'L':
            return WEST
        elif direction == 'R':
            return EAST
    elif degree == EAST:
        if direction == 'L':
            return NORTH
        elif direction == 'R':
            return SOUTH
    elif degree == WEST:
        if direction == 'L':
            return SOUTH
        elif direction == 'R':
            return NORTH
    elif degree == SOUTH:
        if direction == 'L':
            return EAST
        elif direction == 'R':
            return WEST

with io.open('inputs/day01.txt','r') as f:
    # here are your orders snake
    instructions = [instruct.strip() for instruct in f.readline().split(', ') if len(instruct.strip()) > 0]

    # initialize that shit
    x, y = 0, 0
    degree = NORTH

    # Initisalition of the history of locations
    last_locations = set()
    last_locations.add((x,y))
    location_visited_twice = None
    def add_location(x, y):
        """
        Helper function to add a location to history and keep track
        of the first visited twice location
        """
        global location_visited_twice
        # DID U COME HERE BEFORE
        if (x,y) in last_locations and location_visited_twice is None:
            location_visited_twice = (x,y)
        # update history
        last_locations.add((x,y))
        
    # moving thingamajig
    for inst in instructions:
        # Determination of the instructions
        move = inst[0]
        quantity = int(inst[1:]) # beware: quantity may be on several digits

        # wanna get das coordinates here we go
        degree = change_degree(degree, move)

        if degree == NORTH:
            for _ in range(quantity):
                y += 1
                add_location(x, y)

        elif degree == WEST:
            for _ in range(quantity):
                x -= 1
                add_location(x, y)

        elif degree == SOUTH:
            for _ in range(quantity):
                y -= 1
                add_location(x, y)

        elif degree == EAST:
            for _ in range(quantity):
                x += 1
                add_location(x, y)

    # 1 part
    # Computing shortest path
    result = abs(x) + abs(y)
    print('[part1] Shortest path from (0,0) to {} is {}'.format((x,y),result))

    # 2 parts
    (x, y) = location_visited_twice
    result = abs(x) + abs(y)
    print('[part2] First location visited twice is {}, dist={}'.format(location_visited_twice, result))
