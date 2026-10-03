import numpy as np


def calculate_slope(height):

    dy, dx = np.gradient(height)

    slope = np.sqrt(dx**2 + dy**2)

    return slope