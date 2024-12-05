from utils import *
from collections import Counter
from itertools import pairwise
# load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    result = 0
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j in range(m):
            for dr, dc in MATRIX_DIR:
                if sum(c == t for c, t in zip("XMAS", matrix_iterdir(lines, i, j, dr, dc))) == 4:
                    result += 1

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    n = len(lines)
    m = len(lines[0])
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if lines[i][j] != 'A':
                continue

            v = ''.join(lines[r][c] for r, c in matrix_nextX(lines, i, j))
            if v in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                result += 1

    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 18
assert task1('data.txt') == 2427
assert task2('test.txt') == 9
assert task2('data.txt') == 1900
