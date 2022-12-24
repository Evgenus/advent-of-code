from collections import Counter

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(int, data.strip().split(','))


def task(filename, dist):
    crabs = Counter(read_data(filename))

    m = inf
    for pos in range(min(crabs), max(crabs) + 1):
        s = sum(
            dist(crab - pos) * count
            for crab, count in crabs.items()
        )
        m = min(m, s)
    return m


def sum_num(n):
    n = abs(n)
    return n * (n + 1) // 2


assert task('test.txt', abs) == 37
assert task('data.txt', abs) == 340052
assert task('test.txt', sum_num) == 168
assert task('data.txt', sum_num) == 92948968
