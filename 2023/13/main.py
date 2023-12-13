from collections import defaultdict, Counter
from functools import cache, partial

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    patterns = list_split(lines, [''])
    return [lmap(list, pattern) for pattern in patterns]


def find(pattern, wrong=None):
    n = len(pattern)
    m = len(pattern[0])
    for i in range(1, n):
        trim = min(i, n - i)
        if pattern[:i][::-1][:trim] == pattern[i:][:trim]:
            if wrong != 100 * i:
                return 100 * i
    for j in range(1, m):
        trim = min(j, m - j)
        if all(pattern[i][:j][::-1][:trim] == pattern[i][j:][:trim] for i in range(n)):
            if wrong != j:
                return j


def find_replace(pattern):
    n = len(pattern)
    m = len(pattern[0])

    first = find(pattern)

    for a in range(n):
        for b in range(m):
            pattern[a][b] = '#' if pattern[a][b] == '.' else '.'
            result = find(pattern, first)
            pattern[a][b] = '#' if pattern[a][b] == '.' else '.'

            if result is not None:
                return result

    assert False, 'Fail!'


def task1(filename):
    patterns = read_data(filename)

    return sum(
        find(pattern)
        for pattern in patterns
    )


def task2(filename):
    patterns = read_data(filename)

    return sum(
        find_replace(pattern)
        for pattern in patterns
    )


assert task1('test.txt') == 405
assert task1('data.txt') == 35521
assert task2('test.txt') == 400
assert task2('data.txt') == 34795
