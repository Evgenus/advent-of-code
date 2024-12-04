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
    lines = lmap(list, lines)
    print(lines)
    result = 0
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j in range(m):
            for di, dj in (
                    (-1, -1), (0, -1), (1, -1),
                    (-1, 0),           (1, 0),
                    (-1, 1), (0, 1), (1, 1),
            ):
                for k, c in enumerate("XMAS"):
                    ni = i + di * k
                    nj = j + dj * k
                    if not 0 <= ni < n:
                        break
                    if not 0 <= nj < m:
                        break
                    if lines[ni][nj] != c:
                        break
                else:
                    result += 1

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    lines = lmap(list, lines)
    print(lines)
    result = 0
    n = len(lines)
    m = len(lines[0])
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if lines[i][j] != 'A':
                continue
            if lines[i - 1][j - 1] == 'M':
                if lines[i + 1][j + 1] != 'S':
                    continue
            elif lines[i - 1][j - 1] == 'S':
                if lines[i + 1][j + 1] != 'M':
                    continue
            else:
                continue

            if lines[i + 1][j - 1] == 'M':
                if lines[i - 1][j + 1] != 'S':
                    continue
            elif lines[i + 1][j - 1] == 'S':
                if lines[i - 1][j + 1] != 'M':
                    continue
            else:
                continue

            result += 1

    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 18
assert task1('data.txt') == 2427
assert task2('test.txt') == 9
assert task2('data.txt') == 1900
