from functools import partial

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(partial(lmap, int), data.strip().splitlines())


def dij(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [
        [inf] * m for _ in range(n)
    ]

    start = (0, 0)
    result[start[0]][start[1]] = 0
    queue = set()
    queue.add(start)
    while queue:
        next_queue = set()
        for i, j in queue:
            v = result[i][j]
            for di, dj in matrix_next4(matrix, i, j):
                if v + matrix[di][dj] < result[di][dj]:
                    result[di][dj] = v + matrix[di][dj]
                    next_queue.add((di, dj))
        queue = next_queue
    return result[-1][-1]


def task1(filename):
    matrix = read_data(filename)
    return dij(matrix)


def task2(filename):
    matrix = read_data(filename)
    n = len(matrix)
    m = len(matrix[0])
    bigger = [
        [0] * m * 5 for _ in range(n * 5)
    ]
    for a in range(5):
        for b in range(5):
            for i in range(n):
                for j in range(m):
                    bigger[i + a * n][j + b * m] = (matrix[i][j] + a + b - 1) % 9 + 1

    return dij(bigger)


assert task1('test.txt') == 40
assert task1('data.txt') == 583
assert task2('test.txt') == 315
assert task2('data.txt') == 2927
