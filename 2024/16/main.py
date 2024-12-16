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

    wall = set()
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if c == '#':
                wall.add((i, j))
            if c == 'S':
                sI, sJ = i, j
            if c == 'E':
                eI, eJ = i, j

    DIRS = {
        'E': (0, -1),
        'W': (0, 1),
        'N': (-1, 0),
        'S': (1, 0),
    }

    ROT = {
        'E': 'NS',
        'N': 'EW',
        'W': 'SN',
        'S': 'WE'
    }

    used = defaultdict(lambda: 10**6)

    queue = [(sI, sJ, 'E', 0)]
    while queue:
        nxt = []
        for i, j, dir, score in queue:
            di, dj = DIRS[dir]
            ni = i + di
            nj = j + dj
            if (ni, nj) not in wall:
                if used[ni, nj, dir] > score + 1:
                    used[ni, nj, dir] = score + 1
                    nxt.append((ni, nj, dir, score + 1))
            for nd in ROT[dir]:
                if used[i, j, nd] > score + 1000:
                    used[i, j, nd] = score + 1000
                    nxt.append((i, j, nd, score + 1000))
        queue = nxt

    result = min(
        used[eI, eJ, dir]
        for dir in DIRS
    )

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0


    wall = set()
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if c == '#':
                wall.add((i, j))
            if c == 'S':
                sI, sJ = i, j
            if c == 'E':
                eI, eJ = i, j

    DIRS = {
        'E': (0, -1),
        'W': (0, 1),
        'N': (-1, 0),
        'S': (1, 0),
    }

    ROT = {
        'E': 'NS',
        'N': 'EW',
        'W': 'SN',
        'S': 'WE'
    }

    used = defaultdict(lambda: 10**6)
    paths = defaultdict(list)

    queue = [(sI, sJ, 'E', 0, [(sI, sJ)])]
    while queue:
        nxt = []
        for i, j, dir, score, p in queue:
            di, dj = DIRS[dir]
            ni = i + di
            nj = j + dj
            if (ni, nj) not in wall:
                if used[ni, nj, dir] > score + 1:
                    used[ni, nj, dir] = score + 1
                    np = [*p, (ni, nj)]
                    paths[ni, nj, dir] = [np]
                    nxt.append((ni, nj, dir, score + 1, np))
                elif used[ni, nj, dir] == score + 1:
                    np = [*p, (ni, nj)]
                    paths[ni, nj, dir].append(np)
                    nxt.append((ni, nj, dir, score + 1, np))
            for nd in ROT[dir]:
                if used[i, j, nd] > score + 1000:
                    used[i, j, nd] = score + 1000
                    paths[ni, nj, dir] = [p]
                    nxt.append((i, j, nd, score + 1000, p))
                elif used[i, j, nd] == score + 1000:
                    paths[ni, nj, dir].append(p)
                    nxt.append((i, j, nd, score + 1000, p))
            queue = nxt

    M = min(
        used[eI, eJ, dir]
        for dir in DIRS
    )

    sits = set()
    for dir in DIRS:
        if used[eI, eJ, dir] != M:
            continue
        for path in paths[eI, eJ, dir]:
            sits.update(path)

    result = len(sits)

    # matrix = [
    #     ['.' for _ in line]
    #     for line in lines
    # ]
    # for dir in DIRS:
    #     for path in paths[eI, eJ, dir]:
    #         for i, j in path:
    #             matrix[i][j] = 'O'
    # for i, j in wall:
    #     matrix[i][j] = '#'
    #
    # matrix_print(matrix)

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 7036
assert task1('data.txt') == 109496
assert task2('test.txt') == 45
assert task2('data.txt') == 551
