import numpy as np


def lerp(a, b, t):
    return a + (b - a) * t


def resize_noise(noise, new_size):
    old_size = noise.shape[0]

    result = np.zeros((new_size, new_size))

    scale = (old_size - 1) / (new_size - 1)

    for y in range(new_size):
        for x in range(new_size):

            old_x = x * scale
            old_y = y * scale

            x0 = int(np.floor(old_x))
            x1 = min(x0 + 1, old_size - 1)

            y0 = int(np.floor(old_y))
            y1 = min(y0 + 1, old_size - 1)

            tx = old_x - x0
            ty = old_y - y0

            top = lerp(
                noise[y0, x0],
                noise[y0, x1],
                tx
            )

            bottom = lerp(
                noise[y1, x0],
                noise[y1, x1],
                tx
            )

            result[y, x] = lerp(
                top,
                bottom,
                ty
            )

    return result