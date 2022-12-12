from functools import partial

from utils import (
    chain,
    list_split,
)


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    groups = list_split(lines, [''])
    return map(chain(partial(map, int), sum), groups)


def task1(filename):
    groups = read_data(filename)
    return max(groups)


def task2(filename):
    groups = read_data(filename)
    return sum(sorted(groups)[-3:])


assert task1('test.txt') == 24000
assert task2('test.txt') == 45000
assert task1('data.txt') == 67016
assert task2('data.txt') == 200116
