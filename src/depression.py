import heapq
import numpy as np


DIRECTIONS = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1)
]


def fill_depressions(height):

    rows, cols = height.shape

    filled = height.copy()

    visited = np.zeros(
        height.shape,
        dtype=bool
    )

    queue = []

    # Add boundary cells
    for x in range(cols):

        heapq.heappush(
            queue,
            (filled[0, x], 0, x)
        )

        heapq.heappush(
            queue,
            (filled[rows - 1, x], rows - 1, x)
        )

        visited[0, x] = True
        visited[rows - 1, x] = True

    for y in range(rows):

        heapq.heappush(
            queue,
            (filled[y, 0], y, 0)
        )

        heapq.heappush(
            queue,
            (filled[y, cols - 1], y, cols - 1)
        )

        visited[y, 0] = True
        visited[y, cols - 1] = True

    while queue:

        current_height, y, x = heapq.heappop(queue)

        for dy, dx in DIRECTIONS:

            ny = y + dy
            nx = x + dx

            if ny < 0 or ny >= rows:
                continue

            if nx < 0 or nx >= cols:
                continue

            if visited[ny, nx]:
                continue

            visited[ny, nx] = True

            neighbor_height = filled[ny, nx]

            if neighbor_height < current_height:

                filled[ny, nx] = current_height

            heapq.heappush(
                queue,
                (filled[ny, nx], ny, nx)
            )

    return filled