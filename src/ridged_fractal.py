import numpy as np

from octave import generate_octave
from ridged_noise import make_ridged


def generate_ridged_fractal(
    seed,
    world_size,
    octaves=4,
    initial_frequency=5,
    initial_amplitude=1.0,
    persistence=0.5,
    lacunarity=2.0
):

    noise = np.zeros(
        (world_size, world_size)
    )

    frequency = initial_frequency
    amplitude = initial_amplitude

    for octave in range(octaves):

        layer = generate_octave(
            seed=seed + octave,
            world_size=world_size,
            frequency=int(frequency),
            amplitude=1.0
        )

        layer = make_ridged(layer)

        noise += layer * amplitude

        frequency *= lacunarity
        amplitude *= persistence

    minimum = noise.min()
    maximum = noise.max()

    noise = (
        noise - minimum
    ) / (
        maximum - minimum
    )

    return noise