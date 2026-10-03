import numpy as np


DIRECTIONS = [
    (-1, -1),  # NW
    (-1,  0),  # N
    (-1,  1),  # NE
    ( 0, -1),  # W
    ( 0,  1),  # E
    ( 1, -1),  # SW
    ( 1,  0),  # S
    ( 1,  1)   # SE
]


def trace_river(start_y, start_x, flow):

    rows, cols = flow.shape

    river = []

    y = start_y
    x = start_x

    visited = set()

    while True:

        if y < 0 or y >= rows:
            break

        if x < 0 or x >= cols:
            break

        if (y, x) in visited:
            break

        visited.add((y, x))
        river.append((y, x))

        direction = flow[y, x]

        if direction == -1:
            break

        dy, dx = DIRECTIONS[direction]

        y += dy
        x += dx

    return river


def generate_river_network(
    height,
    flow,
    accumulation,
    source_percentile=85
):

    source_threshold = np.percentile(
        accumulation,
        source_percentile
    )

    sources = (
        (height >= np.percentile(height, 70)) &
        (accumulation >= source_threshold)
    )

    river_map = np.zeros(height.shape, dtype=bool)

    source_positions = np.argwhere(sources)

    for y, x in source_positions:

        river = trace_river(
            y,
            x,
            flow
        )

        for river_y, river_x in river:
            river_map[river_y, river_x] = True

    return river_map