from collections import defaultdict

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


directions = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}


def task1(filename):
    lines = read_data(filename)
    digs = defaultdict(str)
    i, j = 0, 0
    digs[i, j] = '#'
    for line in lines:
        d, l, c = line.split()
        di, dj = directions[d]
        l = int(l)
        for _ in range(l):
            i, j = i + di, j + dj
            digs[i, j] = '#'

    sn = min(i for i, j in digs)
    sm = min(j for i, j in digs)

    n = max(i for i, j in digs) - sn + 1
    m = max(j for i, j in digs) - sm + 1
    matrix = [["."] * m for i in range(n)]

    for (i, j), c in digs.items():
        matrix[i - sn][j - sm] = c

    queue = [(- sn + 1, - sm + 1)]
    while queue:
        next_queue = []
        for i, j in queue:
            for ni, nj in matrix_next4(matrix, i, j):
                if matrix[ni][nj] != '#':
                    matrix[ni][nj] = '#'
                    next_queue.append((ni, nj))
        queue = next_queue

    return sum(
        1
        for i in range(n)
        for j in range(m)
        if matrix[i][j] == '#'
    )


names = 'RDLU'


def area(segments):
    return 0.5 * abs(sum(
        x0 * y1 - x1 * y0
        for ((x0, y0), (x1, y1)) in segments
    ))


def solve(moves):
    x, y = 0, 0
    segments = []
    perimetr = 0
    for d, l in moves:
        dy, dx = directions[d]
        perimetr += l
        nx, ny = x + dx * l, y + dy * l
        segments.append(((x, y), (nx, ny)))
        x, y = nx, ny

    return int(area(segments) + perimetr // 2 + 1)


def task1v2(filename):
    lines = read_data(filename)

    moves = []
    for line in lines:
        d, l, c = line.split()
        l = int(l)
        moves.append((d, l))

    return solve(moves)


def task2(filename):
    lines = read_data(filename)

    moves = []
    for line in lines:
        _, _, c = line.split()
        d = names[int(c[-2], 16)]
        l = int(c[2:-2], 16)
        moves.append((d, l))

    return solve(moves)


assert task1('test.txt') == 62
assert task1('data.txt') == 50746
assert task1v2('test.txt') == 62
assert task1v2('data.txt') == 50746
assert task2('test.txt') == 952408144115
assert task2('data.txt') == 70086216556038
