from collections import defaultdict

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


TABLE = {
    'N': [-1, 0, {
        '|': 'N',
        'F': 'E',
        '7': 'W',
    }],
    'S': [1, 0, {
        '|': 'S',
        'J': 'W',
        'L': 'E',
    }],
    'W': [0, -1, {
        '-': 'W',
        'L': 'N',
        'F': 'S',
    }],
    'E': [0, 1, {
        '-': 'E',
        'J': 'N',
        '7': 'S',
    }],
}


def task1(filename):
    lines = read_data(filename)

    start = []
    maze = defaultdict(str)
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 'S':
                start.append((i, j))
            maze[i, j] = cell

    si, sj = start[0]
    queue = [(si, sj, d) for d in 'NESW']

    visited = {(si, sj): 0}
    step = 0
    while queue:
        step += 1
        new_queue = []
        for i, j, d in queue:
            di, dj, variants = TABLE[d]
            if (i + di, j + dj) in visited:
                continue
            nd = variants.get(maze[i + di, j + dj])
            if not nd:
                continue
            new_queue.append((i + di, j + dj, nd))
            visited[i + di, j + dj] = step
        queue = new_queue
    return max(visited.values())


def task2(filename):
    lines = read_data(filename)

    n = len(lines)
    m = len(lines[0])
    start = []
    maze = defaultdict(str)
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 'S':
                start.append((i, j))
            maze[i, j] = cell

    si, sj = start[0]
    queue = [(si, sj, d) for d in 'NESW']

    new_maze = defaultdict(str)
    pipe = {(si, sj): 0}
    step = 0
    while queue:
        step += 1
        new_queue = []
        for i, j, d in queue:
            new_maze[i * 2, j * 2] = 'o'
            di, dj, variants = TABLE[d]
            nd = variants.get(maze[i + di, j + dj])
            if not nd:
                continue
            new_maze[i * 2 + di, j * 2 + dj] = 'o'
            if (i + di, j + dj) not in pipe:
                pipe[i + di, j + dj] = step
                new_queue.append((i + di, j + dj, nd))
        queue = new_queue

    queue = []
    for i in range(2 * n):
        if (i, 0) not in new_maze:
            queue.append((i, 0))
        if (i, 2 * m - 1) not in new_maze:
            queue.append((i, 2 * m - 1))
    for j in range(2 * m):
        if (0, j) not in new_maze:
            queue.append((0, j))
        if (2 * n - 1, j) not in new_maze:
            queue.append((2 * n - 1, j))

    while queue:
        new_queue = []
        for i, j in queue:
            for di, dj, variants in TABLE.values():
                if (i + di, j + dj) in new_maze:
                    continue
                if not 0 <= i + di < 2 * n:
                    continue
                if not 0 <= j + dj < 2 * m:
                    continue
                new_queue.append((i + di, j + dj))
                new_maze[i + di, j + dj] = '.'
        queue = new_queue

    free = 0
    for i in range(n):
        for j in range(m):
            if (2 * i, 2 * j) not in new_maze:
                free += 1
                new_maze[2 * i, 2 * j] = 'W'

    for i in range(2 * n):
        s = ''
        for j in range(2 * m):
            s += (new_maze[i, j] or ' ') * 2
        print(s)
    print()

    return free


assert task1('test1.txt') == 8
assert task1('data.txt') == 6867
assert task2('test2.txt') == 10
assert task2('test3.txt') == 8
assert task2('test4.txt') == 4
assert task2('test5.txt') == 4
# assert task2('data.txt') == 595
