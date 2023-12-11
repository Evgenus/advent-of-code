from bisect import bisect_left
from itertools import combinations

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task(filename, size):
    lines = lmap(list, read_data(filename))

    n = len(lines)
    m = len(lines[0])

    rows = [
        i for i in range(n)
        if all(lines[i][j] == '.' for j in range(m))
    ]

    cols = [
        j for j in range(m)
        if all(lines[i][j] == '.' for i in range(n))
    ]

    galaxies = [
        (bisect_left(rows, i) * size + i, bisect_left(cols, j) * size + j)
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
        if c == '#'
    ]

    return sum(
        cell_dist4(a, b)
        for a, b in combinations(galaxies, 2)
    )


assert task('test.txt', 1) == 374
assert task('data.txt', 1) == 9214785
assert task('test.txt', 10 - 1) == 1030
assert task('test.txt', 100 - 1) == 8410
assert task('data.txt', 1_000_000 - 1) == 613686987427
