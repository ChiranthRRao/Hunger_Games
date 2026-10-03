import numpy as np


def calculate_flow_accumulation(height, flow):

    rows, cols = height.shape

    accumulation = np.ones((rows, cols), dtype=float)

    # Process highest cells first
    order = np.argsort(height, axis=None)[::-1]

    for index in order:

        y, x = np.unravel_index(index, height.shape)

        direction = flow[y, x]

        # No downhill neighbor
        if direction == -1:
            continue

        dy, dx = [
            (-1, -1),
            (-1,  0),
            (-1,  1),
            ( 0, -1),
            ( 0,  1),
            ( 1, -1),
            ( 1,  0),
            ( 1,  1)
        ][direction]

        ny = y + dy
        nx = x + dx

        accumulation[ny, nx] += accumulation[y, x]

    return accumulation