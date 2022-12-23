from collections import Counter

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    segments = []
    for line in data.strip().splitlines():
        a, b = line.split(' -> ')
        a = tuple(map(int, a.split(',')))
        b = tuple(map(int, b.split(',')))
        segments.append((a, b))
    return segments


def iter_line(a, b):
    yield a
    while a != b:
        a = cell_move_towards(a, b)
        yield a


def task1(filename):
    segments = read_data(filename)
    cells = Counter()
    for a, b in segments:
        if a[0] != b[0] and a[1] != b[1]:
            continue
        cells.update(iter_line(a, b))
    return sum(
        used > 1
        for used in cells.values()
    )


def task2(filename):
    segments = read_data(filename)
    cells = Counter()
    for a, b in segments:
        cells.update(iter_line(a, b))
    return sum(
        used > 1
        for used in cells.values()
    )


assert task1('test.txt') == 5
assert task1('data.txt') == 4873
assert task2('test.txt') == 12
assert task2('data.txt') == 19472
