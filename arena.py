import math

TABLE_SIZE = 1.3
ARENA_SIZE_TABLES = 2 + math.sqrt(0.5)
ARENA_SIZE = ARENA_SIZE_TABLES * TABLE_SIZE

markers_table_coords = [
        # South-west
        (0, 0.25),
        (0, 0.75),
        (0, 1.25),
        (0, 1.75),
        None,
        # North-west
        None,
        (ARENA_SIZE_TABLES - 1.75, ARENA_SIZE_TABLES), 
        (ARENA_SIZE_TABLES - 1.25, ARENA_SIZE_TABLES),
        (ARENA_SIZE_TABLES - 0.75, ARENA_SIZE_TABLES),
        (ARENA_SIZE_TABLES - 0.25, ARENA_SIZE_TABLES),
        # North-east wall
        (ARENA_SIZE_TABLES, ARENA_SIZE_TABLES - 0.25),
        (ARENA_SIZE_TABLES, ARENA_SIZE_TABLES - 0.75),
        (ARENA_SIZE_TABLES, ARENA_SIZE_TABLES - 1.25),
        (ARENA_SIZE_TABLES, ARENA_SIZE_TABLES - 1.75),
        None,
        # South-east
        None,
        (1.75, 0),
        (1.25, 0),
        (0.75, 0),
        (0.25, 0),
        ]

markers = []

for coords in markers_table_coords:
    if coords is not None:
        x, y = coords
        markers.append((x * TABLE_SIZE, y * TABLE_SIZE))
    else:
        markers.append(None)

HOME_ZONE = 0
GOAL_ZONE = 1

def get_zone_by_coords((x, y)):
    """
    Return the team letter and zone type of the zone in which the given point
    lies. Will not detect the centre square.
    """
    if x + y > ARENA_SIZE:
        print(x + y, ARENA_SIZE * 2 - TABLE_SIZE)
        if x + y > ARENA_SIZE * 2 - TABLE_SIZE:
            return 'B', HOME_ZONE
        else:
            return 'A', GOAL_ZONE
    else:
        if x + y > TABLE_SIZE:
            return 'B', GOAL_ZONE
        else:
            return 'A', HOME_ZONE

def test():
    for marker in markers:
        if marker is None: print()
        else: print(get_zone_by_coords(marker))
