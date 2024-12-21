from utils import *
from collections import Counter
from itertools import pairwise
from functools import cache

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""

NUMS = (
"789",
"456",
"123",
"X0A",
)


"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

ARROWS = (
"X^A",
"<v>",
)


@cache
def find(PAD, a):
    for i, line in enumerate(PAD):
        for j, c in enumerate(line):
            if c == a:
                return i, j


def matrix_next4(matrix, row, col):
    for r, c, d in ((row - 1, col, '^'), (row + 1, col, 'v'), (row, col - 1, '<'), (row, col + 1, '>')):
        if not 0 <= r < len(matrix):
            continue
        if not 0 <= c < len(matrix[row]):
            continue
        yield r, c, d


@cache
def shortest(PAD, a, b, func):
    i, j = find(PAD, a)
    used = defaultdict(lambda: 10**15)

    used[i, j] = func('A')

    queue = [(i, j, '')]
    while queue:
        nxt = []
        for i, j, p in queue:
            for ni, nj, d in matrix_next4(PAD, i, j):
                if PAD[ni][nj] == 'X':
                    continue
                np = p + d
                score = func(np + 'A')
                if used[ni, nj] <= score:
                    continue
                used[ni, nj] = score
                nxt.append((ni, nj, np))
        queue = nxt
    i, j = find(PAD, b)
    return used[i, j]


def shortestp(PAD, seq, func):
    return sum(
        shortest(PAD, a, b, func)
        for a, b in pairwise('A' + seq)
    )


def robot(func):
    def score(path):
        return shortestp(ARROWS, path, func)
    return score


def task1(filename):
    lines = read_data(filename)
    result = 0

    for code in lines:
        value = str_integers(code)[0]
        score = shortestp(NUMS, code, chain(*[robot] * 2)(len))
        result += value * score

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    for code in lines:
        value = str_integers(code)[0]
        score = shortestp(NUMS, code, chain(*[robot] * 25)(len))
        result += value * score

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 126384
assert task1('data.txt') == 174124
assert task2('data.txt') == 216668579770346
