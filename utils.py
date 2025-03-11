import random

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