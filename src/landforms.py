import numpy as np


LOW = 0
PLAINS = 1
HILLS = 2
MOUNTAINS = 3

def classify_landforms(height, slope):

    hill_threshold = np.percentile(slope, 70)
    mountain_threshold = np.percentile(slope, 90)

    print("Hill slope threshold:", hill_threshold)
    print("Mountain slope threshold:", mountain_threshold)

    landforms = np.full(height.shape, PLAINS, dtype=int)

    landforms[height < 0.30] = LOW

    landforms[
        (height >= 0.30) &
        (height < 0.65) &
        (slope >= hill_threshold)
    ] = HILLS

    landforms[
        (height >= 0.65) &
        (slope >= mountain_threshold)
    ] = MOUNTAINS

    return landforms