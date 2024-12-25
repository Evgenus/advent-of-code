from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    lines = read_data(filename)
    result = 0

    connections = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    triples = set()
    for a, bs in connections.items():
        for b in bs:
            for c in connections[b]:
                if a in connections[c]:
                    triples.add(tuple(sorted([a, b, c])))

    for triple in triples:
        if any([t.startswith('t') for t in triple]):
            result += 1

    print(f"1: {filename}, {result}")
    return result


def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)


def task2(filename):
    lines = read_data(filename)
    result = 0

    connections = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    all_cliques = list(bron_kerbosch(set(), set(connections), set(), connections))
    max_clique_size = max(len(clique) for clique in all_cliques)
    for clique in all_cliques:
        if len(clique) == max_clique_size:
            result = ','.join(sorted(clique))

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 7
assert task1('data.txt') == 1098
assert task2('test.txt') == 'co,de,ka,ta'
assert task2('data.txt') == 'ar,ep,ih,ju,jx,le,ol,pk,pm,pp,xf,yu,zg'
