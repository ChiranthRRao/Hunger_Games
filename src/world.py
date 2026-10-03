import numpy as np

from fractal_noise import generate_fractal_noise
from terrain import GRASS, WATER, FOREST, ROCK


def generate_world(seed, size=100):

    height = generate_fractal_noise(
        seed=seed,
        world_size=size,
        octaves=4,
        initial_frequency=5,
        initial_amplitude=1.0,
        persistence=0.5,
        lacunarity=2.0
    )

    water_threshold = np.percentile(
        height,
        15
    )

    forest_threshold = np.percentile(
        height,
        65
    )

    rock_threshold = np.percentile(
        height,
        90
    )

    world = np.full(
        (size, size),
        GRASS,
        dtype=int
    )

    world[
        height < water_threshold
    ] = WATER

    world[
        height >= forest_threshold
    ] = FOREST

    world[
        height >= rock_threshold
    ] = ROCK

    return world