import random
import imageio.v3 as iio
import os


def assign_edge_colors(graph, colors):
    """
    Assigns random colors to the edges of a NetworkX graph.

    Args:
        graph (nx.Graph): The input NetworkX graph.
        colors (list): The list of colors to select from.

    Returns:
        list: A list of colors, one for each edge in the graph.
    """

    edge_colors = []

    for u, v in graph.edges():
        color = random.choice(colors)
        edge_colors.append(color)

    return edge_colors


def create_gif(path_gif, output_filename, duration=0.01):
    """
    Creates a looped GIF from PNG images in a folder.

    Args:
        path_gif: Path to the folder containing PNG images.
        output_filename: Name of the output GIF file.
        duration: Duration of each frame in seconds.
    """
    images = []
    filenames = sorted([f for f in os.listdir(path_gif) if f.endswith('.png')])
    for filename in filenames:
        filepath = os.path.join(path_gif, filename)
        images.append(iio.imread(filepath))

    output_path = os.path.join(path_gif, output_filename)
    iio.imwrite(output_path, images, fps=2, loop=0)


