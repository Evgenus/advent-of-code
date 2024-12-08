from utils import *
from collections import Counter
from itertools import pairwise, permutations
# load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = lmap(list, read_data(filename))
    result = 0

    n = len(lines)
    m = len(lines[0])

    nodes = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == ".":
                continue
            nodes[c].append((i, j))

    anti = set()
    for _, coords in nodes.items():
        for a, b in permutations(coords, 2):
            c = b[0] + (b[0] - a[0])
            d = b[1] + (b[1] - a[1])
            if not 0 <= c < n:
                continue
            if not 0 <= d < m:
                continue
            # lines[c][d] = "#"
            anti.add((c, d))
    # matrix_print(lines)

    result = len(anti)
    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = lmap(list, read_data(filename))
    result = 0


    n = len(lines)
    m = len(lines[0])

    nodes = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == ".":
                continue
            nodes[c].append((i, j))

    anti = set()
    for _, coords in nodes.items():
        for a, b in permutations(coords, 2):
            for k in range(0, 1000):
                c = b[0] + k * (b[0] - a[0])
                d = b[1] + k * (b[1] - a[1])
                if not 0 <= c < n:
                    break
                if not 0 <= d < m:
                    break
                # lines[c][d] = "#"
                anti.add((c, d))
    # matrix_print(lines)

    result = len(anti)
    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 14
assert task1('data.txt') == 361
assert task2('test.txt') == 34
assert task2('data.txt') == 1249
