import numpy as np


DIRECTIONS = [
    (-1, -1),  # NW
    (-1,  0),  # N
    (-1,  1),  # NE
    ( 0, -1),  # W
    ( 0,  1),  # E
    ( 1, -1),  # SW
    ( 1,  0),  # S
    ( 1,  1),  # SE
]


def calculate_flow_direction(height):

    rows, cols = height.shape

    flow = np.full((rows, cols), -1, dtype=int)

    for y in range(rows):
        for x in range(cols):

            current_height = height[y, x]

            lowest_height = current_height
            best_direction = -1

            for direction, (dy, dx) in enumerate(DIRECTIONS):

                ny = y + dy
                nx = x + dx

                if ny < 0 or ny >= rows:
                    continue

                if nx < 0 or nx >= cols:
                    continue

                neighbor_height = height[ny, nx]

                if neighbor_height < lowest_height:
                    lowest_height = neighbor_height
                    best_direction = direction

            flow[y, x] = best_direction

    return flow


def flow_to_vectors(flow):

    rows, cols = flow.shape

    dy = np.zeros((rows, cols))
    dx = np.zeros((rows, cols))

    for direction, (direction_y, direction_x) in enumerate(DIRECTIONS):

        mask = flow == direction

        dy[mask] = direction_y
        dx[mask] = direction_x

    return dy, dx