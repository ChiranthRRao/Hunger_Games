import numpy as np


def make_ridged(noise):

    ridged = 1 - np.abs(2 * noise - 1)

    return ridged