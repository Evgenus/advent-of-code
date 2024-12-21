from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(list, data.strip().splitlines())


def get_path(lines):
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if c == 'S':
                sI, sJ = i, j
            if c == 'E':
                eI, eJ = i, j

    used = defaultdict(lambda: 10**6)
    used[sI, sJ] = 0

    queue = {(sI, sJ)}
    step = 1
    while queue:
        nxt = set()
        for i, j in queue:
            for ni, nj in matrix_next4(lines, i, j):
                if lines[ni][nj] == '#':
                    continue
                if used[ni, nj] <= step:
                    continue
                used[ni, nj] = step
                nxt.add((ni, nj))
        queue = nxt
        step += 1

    path = [(eI, eJ)]
    for step in range(used[eI, eJ], -1, -1):
        i, j = path[-1]
        for ni, nj in matrix_next4(lines, i, j):
            if used[ni, nj] == used[i, j] - 1:
                path.append((ni, nj))
                break
    return path


def task1(filename):
    lines = read_data(filename)
    result = 0

    path = get_path(lines)

    for i in range(len(path)):
        for j in range(i + 102, len(path)):
            dist = abs(path[j][0] - path[i][0]) + abs(path[j][1] - path[i][1])
            if (j - i) - dist < 100:
                continue

            if dist == 2:
                result += 1

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    path = get_path(lines)

    for i in range(len(path)):
        for j in range(i + 102, len(path)):
            dist = abs(path[j][0] - path[i][0]) + abs(path[j][1] - path[i][1])
            if (j - i) - dist < 100:
                continue

            if dist <= 20:
                result += 1

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('data.txt') == 1389
assert task2('data.txt') == 1005068
