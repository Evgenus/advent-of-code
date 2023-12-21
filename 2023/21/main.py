import numpy as np

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename, steps):
    lines = read_data(filename)

    queue = set()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 'S':
                queue.add((i, j))

    for _ in range(steps):
        next_queue = set()
        for i, j in queue:
            for ni, nj in matrix_next4(lines, i, j):
                if lines[ni][nj] != '#':
                    next_queue.add((ni, nj))
        queue = next_queue

    return len(queue)


def matrix_next4i(matrix, row, col):
    for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
        yield r, c


def func(n, a, b, c):
    return a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))


def solve(lines, steps):
    n = len(lines)
    m = len(lines[0])

    queue = set()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 'S':
                queue.add((i, j))

    for _ in range(steps):
        next_queue = set()

        for i, j in queue:
            for ni, nj in matrix_next4i(lines, i, j):
                if lines[ni % n][nj % m] != '#':
                    next_queue.add((ni, nj))
        queue = next_queue

    return len(queue)


def task2(filename, steps):
    lines = read_data(filename)

    n = len(lines)
    h = steps % n

    a0 = solve(lines, h)
    a1 = solve(lines, h + n)
    a2 = solve(lines, h + n * 2)

    vandermonde = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    b = np.array([a0, a1, a2])
    c = np.linalg.solve(vandermonde, b).astype(np.int64)

    x = steps // n

    return c[0] * x * x + c[1] * x + c[2]


assert task1('test.txt', 6) == 16
assert task1('data.txt', 64) == 3658
assert task2('data.txt', 26501365) == 608193767979991
