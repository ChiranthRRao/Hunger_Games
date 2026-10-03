import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from terrain import GRASS, WATER, FOREST, ROCK


def visualize(world):

    colors = [
        "green",      # GRASS
        "blue",       # WATER
        "darkgreen",  # FOREST
        "gray"        # ROCK
    ]

    cmap = ListedColormap(colors)

    plt.imshow(
        world,
        cmap=cmap,
        interpolation="nearest"
    )

    plt.title("Hunger Games World")

    plt.show()