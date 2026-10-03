from world import generate_world
from visualize import visualize


seed = 123456

world = generate_world(
    seed=seed,
    size=100
)

visualize(world)