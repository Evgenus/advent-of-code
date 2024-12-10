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
    n = len(lines)

    lines = [lmap(int, line) for line in lines]

    def calc(col, row):
        queue = {(col, row)}
        for k in range(9):
            nxt = set()
            for i, j in queue:
                for ni, nj in matrix_next4(lines, i, j):
                    if lines[ni][nj] == k + 1:
                        nxt.add((ni, nj))
            queue = nxt
        return len(queue)


    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 0:
                result += calc(i, j)

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    n = len(lines)

    lines = [lmap(int, line) for line in lines]

    def calc(col, row):
        queue = [(col, row)]
        for k in range(9):
            nxt = []
            for i, j in queue:
                for ni, nj in matrix_next4(lines, i, j):
                    if lines[ni][nj] == k + 1:
                        nxt.append((ni, nj))
            queue = nxt
        return len(queue)


    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 0:
                result += calc(i, j)

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 36
assert task1('data.txt') == 667
assert task2('test.txt') == 81
assert task2('data.txt') == 1344
