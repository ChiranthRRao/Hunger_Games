import numpy as np

from octave import generate_octave


def generate_fractal_noise(
    seed,
    world_size,
    octaves=4,
    initial_frequency=5,
    initial_amplitude=1.0,
    persistence=0.5,
    lacunarity=2.0
):
    noise = np.zeros((world_size, world_size))

    frequency = initial_frequency
    amplitude = initial_amplitude

    for octave in range(octaves):

        layer = generate_octave(
            seed=seed + octave,
            world_size=world_size,
            frequency=int(frequency),
            amplitude=amplitude
        )

        noise += layer

        frequency *= lacunarity
        amplitude *= persistence

    minimum = noise.min()
    maximum = noise.max()

    noise = (noise - minimum) / (maximum - minimum)

    return noise