import math

TABLE_SIZE = 1.3
ARENA_SIZE = 2 + math.sqrt(0.5)

DIAGONAL_TABLE = math.sqrt(2*(0.25**2))
# X,Y,RotfromNorth
markers_table_coords = [
        # South-west
        (0, 0.25, math.pi/2),
        (0, 0.75, math.pi/2),
        (0, 1.25, math.pi/2),
        (0, 1.75, math.pi/2),

        # North-west
        (DIAGONAL_TABLE, 1.75 + DIAGONAL_TABLE, 3*math.pi/4),
        (ARENA_SIZE - 1.75 - DIAGONAL_TABLE, ARENA_SIZE - DIAGONAL_TABLE, 3*math.pi/4),

        # North wall
        (ARENA_SIZE - 1.75, ARENA_SIZE,math.pi), 
        (ARENA_SIZE - 1.25, ARENA_SIZE,math.pi),
        (ARENA_SIZE - 0.75, ARENA_SIZE,math.pi),
        (ARENA_SIZE - 0.25, ARENA_SIZE,math.pi),

        # North-east wall
        (ARENA_SIZE, ARENA_SIZE - 0.25, (math.pi*3)/4),
        (ARENA_SIZE, ARENA_SIZE - 0.75, (math.pi*3)/4),
        (ARENA_SIZE, ARENA_SIZE - 1.25, (math.pi*3)/4),
        (ARENA_SIZE, ARENA_SIZE - 1.75, (math.pi*3)/4),

        # South-east
        (1.75 + DIAGONAL_TABLE, DIAGONAL_TABLE, (2*math.pi)-math.pi/4),
        (ARENA_SIZE - DIAGONAL_TABLE, ARENA_SIZE - 1.75 - DIAGONAL_TABLE, (2*math.pi)-math.pi/4)),

        # South wall
        (0.25, 0, 0),
        (0.75, 0, 0),
        (1.25, 0, 0),
        (1.75, 0, 0),
        ]

markers = []

for coords in _markers_table_coords:
    if coords is not None:
        x, y = coords
        markers.append((x * TABLE_SIZE, y * TABLE_SIZE))
    else:
        markers.append(None)