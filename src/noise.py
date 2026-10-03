import numpy as np


def smooth(array, iterations=1):
    result = array.copy()

    for _ in range(iterations):
        padded = np.pad(result, 1, mode="edge")

        result = (
            padded[:-2, :-2] +
            padded[:-2, 1:-1] +
            padded[:-2, 2:] +
            padded[1:-1, :-2] +
            padded[1:-1, 1:-1] +
            padded[1:-1, 2:] +
            padded[2:, :-2] +
            padded[2:, 1:-1] +
            padded[2:, 2:]
        ) / 9

    return result