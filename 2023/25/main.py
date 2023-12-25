import networkx as nx

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    lines = read_data(filename)

    edges = []

    for line in lines:
        node, tail = line.split(': ')
        connections = tail.split()
        for connection in connections:
            edges.append((node, connection))

    g = nx.Graph(edges)
    g.remove_edges_from(nx.minimum_edge_cut(g))
    components = list(nx.connected_components(g))
    return len(components[0]) * len(components[1])


assert task1('test.txt') == 54
assert task1('data.txt') == 600369
