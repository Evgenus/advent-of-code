from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    field, moves = list_split(lines, [''])
    field = lmap(list, field)
    moves = ''.join(moves)
    result = 0

    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if c == '@':
                rI, rJ = i, j
                field[i][j] = '.'

    def can_move(i, j, di, dj):
        if field[i + di][j + dj] == 'O':
            return can_move(i + di, j + dj, di, dj)
        if field[i + di][j + dj] == '#':
            return False
        return True

    def move(i, j, di, dj):
        if field[i][j] == 'O':
            field[i][j] = '.'
            move(i + di, j + dj, di, dj)
            field[i + di][j + dj] = 'O'

    MOVES = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    for m in moves:
        di, dj = MOVES[m]
        if can_move(rI, rJ, di, dj):
            rI += di
            rJ += dj
            move(rI, rJ, di, dj)

    # matrix_print(field)

    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if c == 'O':
                result += i * 100 + j

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    field1, moves = list_split(lines, [''])
    field1 = lmap(list, field1)
    moves = ''.join(moves)
    result = 0

    field = [
        [] for _ in range(len(field1))
    ]
    for i, row in enumerate(field1):
        for j, c in enumerate(row):
            if c == '#':
                field[i].extend('##')
            if c == 'O':
                field[i].extend('[]')
            if c == '.':
                field[i].extend('..')
            if c == '@':
                field[i].extend('@.')

    # matrix_print(field)

    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if c == '@':
                rI, rJ = i, j
                field[i][j] = '.'

    def can_move(i, j, di, dj):
        if field[i + di][j + dj] == '[':
            if di:
                return can_move(i + di, j + dj, di, dj) and can_move(i + di, j + dj + 1, di, dj)
            else:
                return can_move(i + di, j + dj * 2, di, dj)
        if field[i + di][j + dj] == ']':
            if di:
                return can_move(i + di, j + dj, di, dj) and can_move(i + di, j + dj - 1, di, dj)
            else:
                return can_move(i + di, j + dj * 2, di, dj)
        if field[i + di][j + dj] == '#':
            return False
        return True

    def move(i, j, di, dj):
        if field[i][j] == '[':
            field[i][j] = '.'
            field[i][j + 1] = '.'
            move(i + di, j + dj, di, dj)
            move(i + di, j + dj + 1, di, dj)
            field[i + di][j + dj] = '['
            field[i + di][j + dj + 1] = ']'
        elif field[i][j] == ']':
            field[i][j] = '.'
            field[i][j - 1] = '.'
            move(i + di, j + dj, di, dj)
            move(i + di, j + dj - 1, di, dj)
            field[i + di][j + dj] = ']'
            field[i + di][j + dj - 1] = '['

    MOVES = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    for m in moves:
        di, dj = MOVES[m]
        if can_move(rI, rJ, di, dj):
            rI += di
            rJ += dj
            move(rI, rJ, di, dj)

    # matrix_print(field)

    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if c == '[':
                result += i * 100 + j

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 10092
assert task1('data.txt') == 1446158
assert task2('test.txt') == 9021
assert task2('data.txt') == 1446175
