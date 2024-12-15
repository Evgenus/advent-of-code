from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def fill(lines, row, col):
    used = {(row, col)}
    t = lines[row][col]
    queue = {(row, col)}
    while queue:
        nxt = set()
        for i, j in queue:
            for ni, nj in matrix_next4(lines, i, j):
                if (ni, nj) in used:
                    continue
                if lines[ni][nj] != t:
                    continue
                nxt.add((ni, nj))
        used.update(nxt)
        queue = nxt
    return used


def get_spots(lines):
    spots = []
    used = set()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if (i, j) not in used:
                spot = fill(lines, i, j)
                spots.append(spot)
                used.update(spot)
    return spots


def task1(filename):
    lines = read_data(filename)
    result = 0

    spots = get_spots(lines)

    for spot in spots:
        per = 0
        for row, col in spot:
            for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if not 0 <= r < len(lines):
                    per += 1
                    continue
                if not 0 <= c < len(lines[row]):
                    per += 1
                    continue
                if lines[row][col] != lines[r][c]:
                    per += 1
        # print(per, len(spot))
        result += per * len(spot)

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    spots = get_spots(lines)

    for spot in spots:
        fence = defaultdict(set)
        for row, col in spot:
            for r, c, s in ((row - 1, col, 'u'), (row + 1, col, 'd'), (row, col - 1, 'l'), (row, col + 1, 'r')):
                if not 0 <= r < len(lines):
                    fence[s].add((row, col))
                    continue
                if not 0 <= c < len(lines[row]):
                    fence[s].add((row, col))
                    continue
                if lines[row][col] != lines[r][c]:
                    fence[s].add((row, col))

        per = 0
        side = fence['u']
        for row, col in side:
            if (row, col - 1) not in side:
                per += 1
        side = fence['d']
        for row, col in side:
            if (row, col - 1) not in side:
                per += 1
        side = fence['l']
        for row, col in side:
            if (row - 1, col) not in side:
                per += 1
        side = fence['r']
        for row, col in side:
            if (row - 1, col) not in side:
                per += 1
        result += per * len(spot)

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 1930
assert task1('data.txt') == 1533644
assert task2('test.txt') == 1206
assert task2('data.txt') == 936718
