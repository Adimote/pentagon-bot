import math

TABLE_SIZE = 1.3
ARENA_SIZE = 2 + math.sqrt(0.5)

markers_table_coords = [
        # South-west
        (0, 0.25),
        (0, 0.75),
        (0, 1.25),
        (0, 1.75),
        None,
        # North-west
        None,
        (ARENA_SIZE - 1.75, ARENA_SIZE), 
        (ARENA_SIZE - 1.25, ARENA_SIZE),
        (ARENA_SIZE - 0.75, ARENA_SIZE),
        (ARENA_SIZE - 0.25, ARENA_SIZE),
        # North-east wall
        (ARENA_SIZE, ARENA_SIZE - 0.25),
        (ARENA_SIZE, ARENA_SIZE - 0.75),
        (ARENA_SIZE, ARENA_SIZE - 1.25),
        (ARENA_SIZE, ARENA_SIZE - 1.75),
        None,
        # South-east
        None,
        (0.25, 0),
        (0.75, 0),
        (1.25, 0),
        (1.75, 0),
        ]

markers = []

for coords in _markers_table_coords:
    if coords is not None:
        x, y = coords
        markers.append((x * TABLE_SIZE, y * TABLE_SIZE))
    else:
        markers.append(None)
