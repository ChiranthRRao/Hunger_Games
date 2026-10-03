import numpy as np


def generate_base_noise(seed, size=10):
    rng = np.random.default_rng(seed)

    return rng.random((size, size))