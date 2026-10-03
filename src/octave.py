from base_noise import generate_base_noise
from interpolation import resize_noise


def generate_octave(seed, world_size, frequency, amplitude):
    frequency = min(frequency, world_size)

    noise = generate_base_noise(seed, frequency)

    noise = resize_noise(noise, world_size)

    noise *= amplitude

    return noise