from collections import Counter

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    matrix = lmap(list, data.strip().splitlines())
    n = len(matrix)
    m = len(matrix[0])

    return {
        (i, j)
        for i in range(n)
        for j in range(m)
        if matrix[i][j] == '#'
    }


MOVES = [
    ((-1, 0), ((-1, 0), (-1, -1), (-1, 1))),
    ((1, 0), ((1, 0), (1, -1), (1, 1))),
    ((0, -1), ((0, -1), (-1, -1), (1, -1))),
    ((0, 1), ((0, 1), (-1, 1), (1, 1))),
]


ALL_AROUND = [
    (-1, 0), (-1, -1), (-1, 1),
    (0, -1), (0, 1),
    (1, 0), (1, -1), (1, 1),
]


def empty(elves, elf, checks):
    i, j = elf
    for di, dj in checks:
        if (i + di, j + dj) in elves:
            return False
    return True


def move(elves, moves):
    decisions = {}
    used = Counter()
    for elf in elves:
        if empty(elves, elf, ALL_AROUND):
            continue
        i, j = elf
        for (di, dj), checks in moves:
            if empty(elves, elf, checks):
                next_elf = (i + di, j + dj)
                decisions[elf] = next_elf
                used[next_elf] += 1
                break

    decisions = {
        elf: next_elf
        for elf, next_elf in decisions.items()
        if used[next_elf] == 1
    }

    elves = {decisions.get(elf, elf) for elf in elves}
    return elves, decisions


def task1(filename):
    elves = read_data(filename)
    moves = MOVES.copy()

    for _ in range(10):
        elves, _ = move(elves, moves)
        moves.append(moves.pop(0))

    min_i = min(i for i, j in elves)
    min_j = min(j for i, j in elves)
    max_i = max(i for i, j in elves)
    max_j = max(j for i, j in elves)
    return (max_i - min_i + 1) * (max_j - min_j + 1) - len(elves)


def task2(filename):
    elves = read_data(filename)
    moves = MOVES.copy()

    turn = 0
    while True:
        turn += 1
        elves, decisions = move(elves, moves)
        if not decisions:
            break
        moves.append(moves.pop(0))

    return turn


assert task1('test.txt') == 110
assert task1('data.txt') == 4116
assert task2('test.txt') == 20
assert task2('data.txt') == 984
